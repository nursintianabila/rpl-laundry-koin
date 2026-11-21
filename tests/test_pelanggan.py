import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import app
import models


class UjiPelanggan(unittest.TestCase):
    """Pengujian fitur daftar, tambah, ubah, dan hapus pelanggan (Langkah 14)."""

    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)

        self.db_lama = models.DB_PATH
        models.DB_PATH = Path(self.folder.name) / "uji_pelanggan.db"
        self.addCleanup(setattr, models, "DB_PATH", self.db_lama)

        models.init_db()
        self.aplikasi = app.buat_aplikasi()
        self.aplikasi.config.update(TESTING=True)
        self.klien = self.aplikasi.test_client()

    def tambah_contoh(self, nama="Pelanggan Uji"):
        return models.tambah_pelanggan(nama)

    def test_daftar_kosong(self):
        hasil = self.klien.get("/pelanggan")
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Belum ada data pelanggan.", teks)

    def test_tambah_pelanggan_valid(self):
        hasil = self.klien.post(
            "/pelanggan/tambah",
            data={"nama_pelanggan": "Nabila"},
            follow_redirects=True,
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Pelanggan berhasil ditambahkan.", teks)
        self.assertIn("Nabila", teks)
        self.assertEqual(len(models.semua_pelanggan()), 1)

    def test_nama_kosong_ditolak(self):
        hasil = self.klien.post(
            "/pelanggan/tambah",
            data={"nama_pelanggan": "   "},
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Nama pelanggan wajib diisi.", teks)
        self.assertEqual(len(models.semua_pelanggan()), 0)

    def test_form_ubah_menampilkan_data_lama(self):
        id_pelanggan = self.tambah_contoh()

        hasil = self.klien.get(f"/pelanggan/{id_pelanggan}/ubah")
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("UBAH PELANGGAN", teks)
        self.assertIn('value="Pelanggan Uji"', teks)

    def test_ubah_pelanggan_berhasil(self):
        id_pelanggan = self.tambah_contoh()

        hasil = self.klien.post(
            f"/pelanggan/{id_pelanggan}/ubah",
            data={"nama_pelanggan": "Pelanggan Baru"},
            follow_redirects=True,
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Pelanggan berhasil diubah.", teks)
        self.assertIn("Pelanggan Baru", teks)
        self.assertEqual(models.ambil_pelanggan(id_pelanggan)["nama_pelanggan"], "Pelanggan Baru")

    def test_ubah_id_tidak_ditemukan_404(self):
        hasil = self.klien.get("/pelanggan/999/ubah")
        self.assertEqual(hasil.status_code, 404)

    def test_hapus_pelanggan_berhasil(self):
        id_pelanggan = self.tambah_contoh()

        hasil = self.klien.post(
            f"/pelanggan/{id_pelanggan}/hapus",
            follow_redirects=True,
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Pelanggan berhasil dihapus.", teks)
        self.assertIsNone(models.ambil_pelanggan(id_pelanggan))

    def test_hapus_lewat_get_405(self):
        id_pelanggan = self.tambah_contoh()

        hasil = self.klien.get(f"/pelanggan/{id_pelanggan}/hapus")

        self.assertEqual(hasil.status_code, 405)
        self.assertIsNotNone(models.ambil_pelanggan(id_pelanggan))

    def test_hapus_pelanggan_yang_dipakai_transaksi_ditolak(self):
        id_pelanggan = self.tambah_contoh()

        with models.koneksi() as db:
            id_layanan = db.execute(
                "INSERT INTO layanan (nama_layanan, harga) VALUES (?, ?)",
                ("Cuci Kering", 7000),
            ).lastrowid
            db.execute(
                """
                INSERT INTO transaksi
                (id_pelanggan, id_layanan, tanggal, berat, total_biaya)
                VALUES (?, ?, ?, ?, ?)
                """,
                (id_pelanggan, id_layanan, "2026-11-21", 2.5, 17500),
            )

        hasil = self.klien.post(
            f"/pelanggan/{id_pelanggan}/hapus",
            follow_redirects=True,
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("masih dipakai pada transaksi", teks)
        self.assertIsNotNone(models.ambil_pelanggan(id_pelanggan))

    def test_nama_berisi_html_ter_escape(self):
        hasil = self.klien.post(
            "/pelanggan/tambah",
            data={"nama_pelanggan": "<b>tes</b>"},
            follow_redirects=True,
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("&lt;b&gt;tes&lt;/b&gt;", teks)

    def test_nama_berisi_perintah_sql_tersimpan_sebagai_teks(self):
        nama_uji = "Robert'); DROP TABLE pelanggan;--"
        hasil = self.klien.post(
            "/pelanggan/tambah",
            data={"nama_pelanggan": nama_uji},
            follow_redirects=True,
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Pelanggan berhasil ditambahkan.", teks)
        self.assertEqual(models.semua_pelanggan()[0]["nama_pelanggan"], nama_uji)


if __name__ == "__main__":
    unittest.main()
