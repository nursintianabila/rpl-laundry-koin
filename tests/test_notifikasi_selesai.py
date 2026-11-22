"""Uji fitur notifikasi transaksi selesai pada dashboard Admin."""
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


class UjiNotifikasiSelesai(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.db_lama = models.DB_PATH
        models.DB_PATH = Path(self.folder.name) / "uji_selesai.db"
        self.addCleanup(setattr, models, "DB_PATH", self.db_lama)
        models.init_db()
        auth_service.buat_pengguna("pemilik@example.com", "pemilik123", "Pemilik")
        auth_service.buat_pengguna("admin@example.com", "admin123", "Admin/Operator")

        with models.koneksi() as db:
            id_pel = db.execute("INSERT INTO pelanggan (nama_pelanggan) VALUES (?)", ("Nabila",)).lastrowid
            id_lay = db.execute("INSERT INTO layanan (nama_layanan, harga) VALUES (?, ?)", ("Cuci Kering", 10000)).lastrowid
            self.id_transaksi = db.execute(
                "INSERT INTO transaksi (id_pelanggan, id_layanan, tanggal, berat, total_biaya) VALUES (?, ?, ?, ?, ?)",
                (id_pel, id_lay, "2026-11-22", 2.0, 20000),
            ).lastrowid

        self.aplikasi = app.buat_aplikasi()
        self.aplikasi.config.update(TESTING=True)

    def klien_login(self, username, password):
        klien = self.aplikasi.test_client()
        with klien.session_transaction() as sess:
            sess["csrf_token"] = "token"
        klien.post("/login", data={"username_email": username, "password": password, "csrf_token": "token"})
        with klien.session_transaction() as sess:
            sess["csrf_token"] = "token"
        return klien

    def test_admin_menandai_selesai_dan_melihat_notifikasi(self):
        klien = self.klien_login("admin@example.com", "admin123")

        hasil = klien.get("/transaksi")
        self.assertIn("Tandai Selesai", hasil.data.decode("utf-8"))

        with klien.session_transaction() as sess:
            sess["csrf_token"] = "token"
        hasil = klien.post(
            f"/transaksi/{self.id_transaksi}/selesai",
            data={"csrf_token": "token"},
            follow_redirects=True,
        )
        teks = hasil.data.decode("utf-8")
        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Transaksi ditandai selesai.", teks)

        dashboard = self.klien_login("admin@example.com", "admin123").get("/dashboard")
        teks_dashboard = dashboard.data.decode("utf-8")
        self.assertIn("Nabila", teks_dashboard)
        self.assertIn("Cuci Kering", teks_dashboard)
        self.assertIn("sudah selesai", teks_dashboard)

    def test_pemilik_tidak_boleh_menandai_selesai(self):
        klien = self.klien_login("pemilik@example.com", "pemilik123")
        hasil = klien.post(
            f"/transaksi/{self.id_transaksi}/selesai",
            data={"csrf_token": "token"},
        )
        self.assertEqual(hasil.status_code, 403)

    def test_pemilik_tidak_melihat_notifikasi_admin(self):
        klien = self.klien_login("pemilik@example.com", "pemilik123")
        hasil = klien.get("/dashboard")
        teks = hasil.data.decode("utf-8")
        self.assertEqual(hasil.status_code, 200)
        self.assertNotIn("Notifikasi transaksi selesai", teks)


if __name__ == "__main__":
    unittest.main()
