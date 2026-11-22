"""Uji autocomplete pelanggan pada form tambah transaksi."""
import sys
import tempfile
from pathlib import Path

import unittest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import app
import models
from services import auth_service


class UjiAutocomplete(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.db_lama = models.DB_PATH
        models.DB_PATH = Path(self.folder.name) / "uji_auto.db"
        self.addCleanup(setattr, models, "DB_PATH", self.db_lama)
        models.init_db()
        auth_service.buat_pengguna("admin@example.com", "admin123", "Admin/Operator")

        with models.koneksi() as db:
            db.execute("INSERT INTO pelanggan (nama_pelanggan) VALUES (?)", ("Nur Sintia Nabila",))
            db.execute("INSERT INTO pelanggan (nama_pelanggan) VALUES (?)", ("Budi Santoso",))
            db.execute("INSERT INTO layanan (nama_layanan, harga) VALUES (?, ?)", ("Cuci", 10000))

        self.aplikasi = app.buat_aplikasi()
        self.aplikasi.config.update(TESTING=True)
        self.klien = self.aplikasi.test_client()
        with self.klien.session_transaction() as sess:
            sess["csrf_token"] = "token"
        self.klien.post("/login", data={"username_email": "admin@example.com", "password": "admin123", "csrf_token": "token"})
        with self.klien.session_transaction() as sess:
            sess["csrf_token"] = "token"

    def test_api_mencocokkan_huruf(self):
        hasil = self.klien.get("/api/pelanggan?q=nur")
        self.assertEqual(hasil.status_code, 200)
        data = hasil.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["nama"], "Nur Sintia Nabila")

    def test_api_tanpa_hasil(self):
        hasil = self.klien.get("/api/pelanggan?q=zzzz")
        self.assertEqual(hasil.get_json(), [])

    def test_api_tamu_dialihkan(self):
        tamu = self.aplikasi.test_client()
        hasil = tamu.get("/api/pelanggan?q=nur")
        self.assertEqual(hasil.status_code, 302)
        self.assertIn("/login", hasil.headers["Location"])

    def test_form_memiliki_kolom_cari(self):
        hasil = self.klien.get("/transaksi/tambah")
        teks = hasil.data.decode("utf-8")
        self.assertEqual(hasil.status_code, 200)
        self.assertIn('id="cari_pelanggan"', teks)
        self.assertIn('id="id_pelanggan"', teks)
        self.assertIn("Ketik nama pelanggan", teks)

    def test_simpan_dengan_id_dari_autocomplete(self):
        hasil = self.klien.post(
            "/transaksi/tambah",
            data={
                "id_pelanggan": "1",
                "id_layanan": "1",
                "tanggal": "2026-11-21",
                "berat": "2",
                "csrf_token": "token",
            },
            follow_redirects=True,
        )
        teks = hasil.data.decode("utf-8")
        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Transaksi berhasil ditambahkan.", teks)


if __name__ == "__main__":
    unittest.main()
