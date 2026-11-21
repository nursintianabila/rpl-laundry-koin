import sqlite3
from contextlib import contextmanager
from pathlib import Path

# Lokasi berkas proyek, database, dan skema.
ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "instance" / "laundry_koin.db"
SCHEMA = ROOT / "docs" / "desain" / "schema.sql"


@contextmanager
def koneksi():
    """Buka koneksi SQLite, aktifkan kunci asing, lalu commit dan tutup."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys = ON")
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def init_db():
    """Membuat database dari schema.sql bila database belum ada."""
    if not DB_PATH.exists():
        with koneksi() as db:
            db.executescript(SCHEMA.read_text(encoding="utf-8"))


def semua_layanan():
    """Mengambil seluruh data layanan untuk halaman daftar."""
    with koneksi() as db:
        return db.execute(
            """
            SELECT id_layanan, nama_layanan, harga
            FROM layanan
            ORDER BY id_layanan
            """
        ).fetchall()