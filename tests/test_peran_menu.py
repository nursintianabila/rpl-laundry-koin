"""Uji peran menu: Transaksi untuk Admin, Riwayat untuk Pemilik."""
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


class UjiPeranMenu(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.db_lama = models.DB_PATH
        models.DB_PATH = Path(self.folder.name) / "uji_peran.db"
        self.addCleanup(setattr, models, "DB_PATH", self.db_lama)
        models.init_db()
        auth_service.buat_pengguna("pemilik@example.com", "pemilik123", "Pemilik")
        auth_service.buat_pengguna("admin@example.com", "admin123", "Admin/Operator")
        self.aplikasi = app.buat_aplikasi()
        self.aplikasi.config.update(TESTING=True)

    def klien_login(self, username, password):
        klien = self.aplikasi.test_client()
        with klien.session_transaction() as sess:
            sess["csrf_token"] = "token"
        klien.post("/login", data={"username_email": username, "password": password, "csrf_token": "token"})
        return klien

    def test_pemilik_melihat_riwayat_tanpa_tombol_tambah(self):
        klien = self.klien_login("pemilik@example.com", "pemilik123")
        hasil = klien.get("/riwayat")
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("RIWAYAT TRANSAKSI", teks)
        self.assertNotIn("+ Tambah Transaksi", teks)

    def test_pemilik_tidak_boleh_membuka_transaksi(self):
        klien = self.klien_login("pemilik@example.com", "pemilik123")
        self.assertEqual(klien.get("/transaksi").status_code, 403)

    def test_admin_boleh_membuka_transaksi(self):
        klien = self.klien_login("admin@example.com", "admin123")
        self.assertEqual(klien.get("/transaksi").status_code, 200)

    def test_admin_boleh_melihat_riwayat(self):
        klien = self.klien_login("admin@example.com", "admin123")
        self.assertEqual(klien.get("/riwayat").status_code, 200)

    def test_menu_pemilik_memuat_riwayat_bukan_transaksi(self):
        klien = self.klien_login("pemilik@example.com", "pemilik123")
        teks = klien.get("/layanan").data.decode("utf-8")

        self.assertIn("Riwayat Transaksi", teks)
        self.assertNotIn('href="/transaksi"', teks)


if __name__ == "__main__":
    unittest.main()
