"""Uji kebersihan rilis: versi, cadangan, .gitignore, changelog, dan dependensi."""
import re
import sqlite3
import sys
import tempfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import cadangkan
import models
from versi import VERSI


@pytest.fixture
def aplikasi_uji():
    folder = tempfile.TemporaryDirectory()
    lama = models.DB_PATH
    models.DB_PATH = Path(folder.name) / "uji.db"
    models.init_db()
    import app
    a = app.buat_aplikasi()
    a.config.update(TESTING=True)
    yield a, folder
    models.DB_PATH = lama
    folder.cleanup()


def test_versi_berformat_semver():
    assert re.fullmatch(r"\d+\.\d+\.\d+", VERSI)


def test_versi_tampil_di_halaman(aplikasi_uji):
    a, _ = aplikasi_uji
    with a.test_client() as c:
        assert f"v{VERSI}" in c.get("/login").text


def test_changelog_memuat_versi_rilis():
    assert f"## [{VERSI}]" in (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")


def test_gitignore_mengecualikan_rahasia_dan_data():
    baris = (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()
    for wajib in (".env", "*.db", "cadangan/"):
        assert wajib in baris


def test_requirements_dikunci_versinya():
    for baris in (ROOT / "requirements.txt").read_text(encoding="utf-8").splitlines():
        if baris.strip() and not baris.startswith("#"):
            assert "==" in baris, baris


def test_cadangan_berisi_data_yang_sama(aplikasi_uji, tmp_path):
    a, _ = aplikasi_uji
    models.tambah_layanan("Cuci Kering", 7000)
    berkas = cadangkan.cadangkan(tmp_path)
    db = sqlite3.connect(berkas)
    try:
        assert db.execute("SELECT nama_layanan, harga FROM layanan").fetchall() == [("Cuci Kering", 7000)]
    finally:
        db.close()
