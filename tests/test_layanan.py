import sys
import tempfile
import unittest
from pathlib import Path

# Memastikan folder proyek dapat diimpor saat pengujian dijalankan dari mana pun.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import app
import models  # noqa: E402


class UjiLayanan(unittest.TestCase):
    """Pengujian fitur daftar dan tambah layanan (Sesi 1)."""

    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)

        self.db_lama = models.DB_PATH
        models.DB_PATH = Path(self.folder.name) / "uji_laundry.db"
        self.addCleanup(setattr, models, "DB_PATH", self.db_lama)

        models.init_db()
        self.aplikasi = app.buat_aplikasi()
        self.aplikasi.config.update(TESTING=True)
        self.klien = self.aplikasi.test_client()

    def test_daftar_kosong_menampilkan_pesan(self):
        hasil = self.klien.get("/layanan")
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Belum ada data layanan.", teks)
        self.assertNotIn("<table>", teks)

    def test_tambah_layanan_valid(self):
        hasil = self.klien.post(
            "/layanan/tambah",
            data={"nama_layanan": "Cuci Kering", "harga": "7000"},
            follow_redirects=True,
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Layanan berhasil ditambahkan.", teks)
        self.assertIn("Cuci Kering", teks)
        self.assertIn("Rp 7.000", teks)
        self.assertEqual(len(models.semua_layanan()), 1)

    def test_nama_kosong_ditolak(self):
        hasil = self.klien.post(
            "/layanan/tambah",
            data={"nama_layanan": "   ", "harga": "7000"},
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Nama layanan wajib diisi.", teks)
        self.assertEqual(len(models.semua_layanan()), 0)

    def test_harga_negatif_ditolak(self):
        hasil = self.klien.post(
            "/layanan/tambah",
            data={"nama_layanan": "Cuci Kering", "harga": "-5"},
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Harga tidak boleh negatif.", teks)
        self.assertEqual(len(models.semua_layanan()), 0)

    def test_harga_bukan_angka_ditolak_dan_isian_dipertahankan(self):
        hasil = self.klien.post(
            "/layanan/tambah",
            data={"nama_layanan": "Cuci Kering", "harga": "abc"},
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Harga harus berupa bilangan bulat", teks)
        self.assertIn('value="abc"', teks)
        self.assertIn('value="Cuci Kering"', teks)
        self.assertEqual(len(models.semua_layanan()), 0)

    def test_nama_duplikat_ditolak_tanpa_membedakan_huruf(self):
        self.klien.post(
            "/layanan/tambah",
            data={"nama_layanan": "Cuci Kering", "harga": "7000"},
        )
        hasil = self.klien.post(
            "/layanan/tambah",
            data={"nama_layanan": "cuci kering", "harga": "8000"},
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Nama layanan sudah ada.", teks)
        self.assertEqual(len(models.semua_layanan()), 1)

    def test_form_tambah_dapat_dibuka(self):
        hasil = self.klien.get("/layanan/tambah")
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("TAMBAH LAYANAN", teks)
        self.assertIn("Nama Layanan", teks)


if __name__ == "__main__":
    unittest.main()
