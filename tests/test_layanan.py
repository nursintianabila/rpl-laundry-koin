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
from services import auth_service  # noqa: E402


class UjiLayanan(unittest.TestCase):
    """Pengujian fitur daftar dan tambah layanan (Sesi 1)."""

    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)

        self.db_lama = models.DB_PATH
        models.DB_PATH = Path(self.folder.name) / "uji_laundry.db"
        self.addCleanup(setattr, models, "DB_PATH", self.db_lama)

        models.init_db()
        auth_service.buat_pengguna("pemilik@example.com", "pemilik123", "Pemilik")
        auth_service.buat_pengguna("admin@example.com", "admin123", "Admin/Operator")
        self.aplikasi = app.buat_aplikasi()
        self.aplikasi.config.update(TESTING=True)
        self.klien = self.aplikasi.test_client()
        with self.klien.session_transaction() as sess:
            sess["csrf_token"] = "test-token"
        self.klien.post("/login", data={"username_email": "pemilik@example.com", "password": "pemilik123", "csrf_token": "test-token"})
        _orig_post = self.klien.post
        def _post(url, **kw):
            d = kw.get("data")
            if not isinstance(d, dict):
                d = {}
            d = dict(d)
            d.setdefault("csrf_token", "test-token")
            kw["data"] = d
            with self.klien.session_transaction() as sess:
                sess["csrf_token"] = "test-token"
            return _orig_post(url, **kw)
        self.klien.post = _post

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

    def test_harga_unicode_ditolak(self):
        hasil = self.klien.post(
            "/layanan/tambah",
            data={"nama_layanan": "Cuci", "harga": "²"},
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Harga harus berupa bilangan bulat", teks)

    def test_form_tambah_dapat_dibuka(self):
        hasil = self.klien.get("/layanan/tambah")
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("TAMBAH LAYANAN", teks)
        self.assertIn("Nama Layanan", teks)

    def tambah_contoh(self, nama="Cuci Kering", harga=7000):
        return models.tambah_layanan(nama, harga)

    def test_form_ubah_menampilkan_data_lama(self):
        id_layanan = self.tambah_contoh()

        hasil = self.klien.get(f"/layanan/{id_layanan}/ubah")
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("UBAH LAYANAN", teks)
        self.assertIn('value="Cuci Kering"', teks)
        self.assertIn('value="7000"', teks)

    def test_ubah_layanan_berhasil(self):
        id_layanan = self.tambah_contoh()

        hasil = self.klien.post(
            f"/layanan/{id_layanan}/ubah",
            data={"nama_layanan": "Cuci Setrika", "harga": "10000"},
            follow_redirects=True,
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Layanan berhasil diubah.", teks)
        self.assertIn("Cuci Setrika", teks)
        self.assertIn("Rp 10.000", teks)

        layanan = models.ambil_layanan(id_layanan)
        self.assertEqual(layanan["nama_layanan"], "Cuci Setrika")
        self.assertEqual(layanan["harga"], 10000)

    def test_ubah_nama_sendiri_tetap_diizinkan(self):
        id_layanan = self.tambah_contoh()

        hasil = self.klien.post(
            f"/layanan/{id_layanan}/ubah",
            data={"nama_layanan": "Cuci Kering", "harga": "8000"},
            follow_redirects=True,
        )

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Layanan berhasil diubah.", hasil.data.decode("utf-8"))
        self.assertEqual(models.ambil_layanan(id_layanan)["harga"], 8000)

    def test_ubah_nama_duplikat_ditolak(self):
        self.tambah_contoh("Cuci Kering", 7000)
        id_kedua = self.tambah_contoh("Setrika", 6000)

        hasil = self.klien.post(
            f"/layanan/{id_kedua}/ubah",
            data={"nama_layanan": "Cuci Kering", "harga": "6500"},
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Nama layanan sudah ada.", teks)
        self.assertEqual(models.ambil_layanan(id_kedua)["nama_layanan"], "Setrika")

    def test_ubah_id_tidak_ditemukan_menghasilkan_404(self):
        hasil = self.klien.get("/layanan/999/ubah")
        self.assertEqual(hasil.status_code, 404)

        hasil = self.klien.post(
            "/layanan/999/ubah",
            data={"nama_layanan": "Tidak Ada", "harga": "1000"},
        )
        self.assertEqual(hasil.status_code, 404)

    def test_hapus_layanan_berhasil(self):
        id_layanan = self.tambah_contoh()

        hasil = self.klien.post(
            f"/layanan/{id_layanan}/hapus",
            follow_redirects=True,
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Layanan berhasil dihapus.", teks)
        self.assertIsNone(models.ambil_layanan(id_layanan))

    def test_hapus_lewat_get_tidak_mengubah_data(self):
        id_layanan = self.tambah_contoh()

        hasil = self.klien.get(f"/layanan/{id_layanan}/hapus")

        self.assertEqual(hasil.status_code, 405)
        self.assertIsNotNone(models.ambil_layanan(id_layanan))

    def test_hapus_id_tidak_ditemukan_menghasilkan_404(self):
        hasil = self.klien.post("/layanan/999/hapus")
        self.assertEqual(hasil.status_code, 404)

    def test_nama_berisi_perintah_sql_tersimpan_sebagai_teks(self):
        nama_uji = "Robert'); DROP TABLE layanan;--"
        hasil = self.klien.post(
            "/layanan/tambah",
            data={"nama_layanan": nama_uji, "harga": "5000"},
            follow_redirects=True,
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Layanan berhasil ditambahkan.", teks)
        data = models.semua_layanan()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["nama_layanan"], nama_uji)

    def test_nama_berisi_html_ditampilkan_ter_escape(self):
        hasil = self.klien.post(
            "/layanan/tambah",
            data={"nama_layanan": "<b>tes</b>", "harga": "5000"},
            follow_redirects=True,
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("&lt;b&gt;tes&lt;/b&gt;", teks)
        self.assertNotIn("<b>tes</b>", teks)

    def test_hapus_layanan_yang_dipakai_transaksi_ditolak(self):
        id_layanan = self.tambah_contoh()

        with models.koneksi() as db:
            hasil_pelanggan = db.execute(
                "INSERT INTO pelanggan (nama_pelanggan) VALUES (?)",
                ("Pelanggan Uji",),
            )
            db.execute(
                """
                INSERT INTO transaksi
                (id_pelanggan, id_layanan, tanggal, berat, total_biaya)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    hasil_pelanggan.lastrowid,
                    id_layanan,
                    "2026-11-21",
                    2.5,
                    17500,
                ),
            )

        hasil = self.klien.post(
            f"/layanan/{id_layanan}/hapus",
            follow_redirects=True,
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("masih dipakai pada transaksi", teks)
        self.assertIn('class="galat"', teks)
        self.assertIsNotNone(models.ambil_layanan(id_layanan))


if __name__ == "__main__":
    unittest.main()
