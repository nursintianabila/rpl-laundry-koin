"""Uji ekspor laporan transaksi CSV dan PDF pada menu Laporan."""
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


class UjiEkspor(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.db_lama = models.DB_PATH
        models.DB_PATH = Path(self.folder.name) / "uji_ekspor.db"
        self.addCleanup(setattr, models, "DB_PATH", self.db_lama)
        models.init_db()
        auth_service.buat_pengguna("pemilik@example.com", "pemilik123", "Pemilik")
        auth_service.buat_pengguna("admin@example.com", "admin123", "Admin/Operator")

        with models.koneksi() as db:
            id_pel = db.execute("INSERT INTO pelanggan (nama_pelanggan) VALUES (?)", ("Nabila",)).lastrowid
            id_lay = db.execute("INSERT INTO layanan (nama_layanan, harga) VALUES (?, ?)", ("Cuci Kering", 10000)).lastrowid
            db.execute(
                "INSERT INTO transaksi (id_pelanggan, id_layanan, tanggal, berat, total_biaya) VALUES (?, ?, ?, ?, ?)",
                (id_pel, id_lay, "2026-11-20", 2.0, 20000),
            )
            db.execute(
                "INSERT INTO transaksi (id_pelanggan, id_layanan, tanggal, berat, total_biaya) VALUES (?, ?, ?, ?, ?)",
                (id_pel, id_lay, "2026-11-22", 1.0, 10000),
            )

        self.aplikasi = app.buat_aplikasi()
        self.aplikasi.config.update(TESTING=True)

    def klien_login(self, username, password):
        klien = self.aplikasi.test_client()
        with klien.session_transaction() as sess:
            sess["csrf_token"] = "token"
        klien.post("/login", data={"username_email": username, "password": password, "csrf_token": "token"})
        return klien

    def test_ekspor_csv(self):
        klien = self.klien_login("pemilik@example.com", "pemilik123")
        hasil = klien.get("/laporan/ekspor?format=csv&mulai=2026-11-20&akhir=2026-11-20")
        teks = hasil.data.decode("utf-8-sig")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("text/csv", hasil.content_type)
        self.assertIn("Pelanggan", teks)
        self.assertIn("Nabila", teks)
        self.assertIn("Jumlahtransaksi,1", teks.replace(" ", ""))
        self.assertIn("20000", teks)

    def test_ekspor_pdf(self):
        klien = self.klien_login("pemilik@example.com", "pemilik123")
        hasil = klien.get("/laporan/ekspor?format=pdf&mulai=2026-11-20&akhir=2026-11-22")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("application/pdf", hasil.content_type)
        self.assertTrue(hasil.data.startswith(b"%PDF"))
        self.assertIn(b"%%EOF", hasil.data)

    def test_halaman_laporan_memiliki_tombol_unduh(self):
        klien = self.klien_login("pemilik@example.com", "pemilik123")
        teks = klien.get("/laporan?mulai=2026-11-20&akhir=2026-11-22").data.decode("utf-8")
        self.assertIn("Unduh CSV (Excel)", teks)
        self.assertIn("Unduh PDF", teks)

    def test_format_tidak_dikenal(self):
        klien = self.klien_login("pemilik@example.com", "pemilik123")
        self.assertEqual(klien.get("/laporan/ekspor?format=xls").status_code, 400)

    def test_tanggal_salah_ditolak(self):
        klien = self.klien_login("pemilik@example.com", "pemilik123")
        self.assertEqual(klien.get("/laporan/ekspor?format=csv&mulai=20-11-2026").status_code, 400)

    def test_admin_tidak_boleh_ekspor(self):
        klien = self.klien_login("admin@example.com", "admin123")
        self.assertEqual(klien.get("/laporan/ekspor?format=csv").status_code, 403)

    def test_tamu_dialihkan(self):
        tamu = self.aplikasi.test_client()
        hasil = tamu.get("/laporan/ekspor?format=csv")
        self.assertEqual(hasil.status_code, 302)
        self.assertIn("/login", hasil.headers["Location"])


if __name__ == "__main__":
    unittest.main()
