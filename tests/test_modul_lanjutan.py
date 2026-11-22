"""Uji modul lanjutan: Dashboard, Laporan, Status Mesin, dan Riwayat."""
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


class UjiModulLanjutan(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.db_lama = models.DB_PATH
        models.DB_PATH = Path(self.folder.name) / "uji_lanjutan.db"
        self.addCleanup(setattr, models, "DB_PATH", self.db_lama)
        models.init_db()

        auth_service.buat_pengguna("pemilik@example.com", "pemilik123", "Pemilik")
        auth_service.buat_pengguna("admin@example.com", "admin123", "Admin/Operator")

        with models.koneksi() as db:
            id_pel = db.execute("INSERT INTO pelanggan (nama_pelanggan) VALUES (?)", ("Pelanggan Uji",)).lastrowid
            id_lay = db.execute("INSERT INTO layanan (nama_layanan, harga) VALUES (?, ?)", ("Cuci", 10000)).lastrowid
            db.execute(
                "INSERT INTO transaksi (id_pelanggan, id_layanan, tanggal, berat, total_biaya) VALUES (?, ?, ?, ?, ?)",
                (id_pel, id_lay, "2026-11-20", 2.0, 20000),
            )
            db.execute(
                "INSERT INTO mesin (informasi_mesin, status_mesin) VALUES (?, ?)",
                ("Mesin Uji", "Tersedia"),
            )

        self.aplikasi = app.buat_aplikasi()
        self.aplikasi.config.update(TESTING=True)

    def klien_login(self, username, password):
        klien = self.aplikasi.test_client()
        with klien.session_transaction() as sess:
            sess["csrf_token"] = "token"
        klien.post("/login", data={"username_email": username, "password": password, "csrf_token": "token"})
        return klien

    def test_pemilik_dashboard(self):
        klien = self.klien_login("pemilik@example.com", "pemilik123")
        hasil = klien.get("/dashboard")
        teks = hasil.data.decode("utf-8")
        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Rp 20.000", teks)
        self.assertIn("Pelanggan Uji", teks)

    def test_pemilik_laporan(self):
        klien = self.klien_login("pemilik@example.com", "pemilik123")
        hasil = klien.get("/laporan?mulai=2026-11-01&akhir=2026-11-30")
        teks = hasil.data.decode("utf-8")
        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Rp 20.000", teks)
        self.assertIn("Cuci", teks)

    def test_pemilik_laporan_tanggal_salah(self):
        klien = self.klien_login("pemilik@example.com", "pemilik123")
        hasil = klien.get("/laporan?mulai=20-11-2026")
        teks = hasil.data.decode("utf-8")
        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Tanggal mulai harus berformat TTTT-BB-HH.", teks)

    def test_pemilik_tidak_boleh_mesin_dan_transaksi(self):
        klien = self.klien_login("pemilik@example.com", "pemilik123")
        self.assertEqual(klien.get("/mesin").status_code, 403)
        self.assertEqual(klien.get("/transaksi").status_code, 403)

    def test_admin_status_mesin(self):
        klien = self.klien_login("admin@example.com", "admin123")
        hasil = klien.get("/mesin")
        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Mesin Uji", hasil.data.decode("utf-8"))

        with klien.session_transaction() as sess:
            sess["csrf_token"] = "token"
        hasil = klien.post(
            "/mesin/1/status",
            data={"status_mesin": "Rusak", "csrf_token": "token"},
            follow_redirects=True,
        )
        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Status mesin berhasil diperbarui.", hasil.data.decode("utf-8"))
        self.assertEqual(models.ambil_mesin(1)["status_mesin"], "Rusak")

    def test_admin_boleh_dashboard_tidak_boleh_laporan(self):
        klien = self.klien_login("admin@example.com", "admin123")
        self.assertEqual(klien.get("/dashboard").status_code, 200)
        self.assertEqual(klien.get("/laporan").status_code, 403)


if __name__ == "__main__":
    unittest.main()
