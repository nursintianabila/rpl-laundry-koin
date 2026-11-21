import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import app
import models
from services import auth_service  # noqa: E402


class UjiTransaksi(unittest.TestCase):
    """Pengujian modul transaksi (Jobsheet 10 Langkah 5-6)."""

    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)

        self.db_lama = models.DB_PATH
        models.DB_PATH = Path(self.folder.name) / "uji_transaksi.db"
        self.addCleanup(setattr, models, "DB_PATH", self.db_lama)

        models.init_db()
        with models.koneksi() as db:
            db.execute("INSERT INTO pelanggan (nama_pelanggan) VALUES (?)", ("Pelanggan Uji",))
            db.execute("INSERT INTO layanan (nama_layanan, harga) VALUES (?, ?)", ("Cuci Kering", 7000))

        auth_service.buat_pengguna("pemilik@example.com", "pemilik123", "Pemilik")
        auth_service.buat_pengguna("admin@example.com", "admin123", "Admin/Operator")
        self.aplikasi = app.buat_aplikasi()
        self.aplikasi.config.update(TESTING=True)
        self.klien = self.aplikasi.test_client()
        with self.klien.session_transaction() as sess:
            sess["csrf_token"] = "test-token"
        self.klien.post("/login", data={"username_email": "admin@example.com", "password": "admin123", "csrf_token": "test-token"})
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

    def test_daftar_kosong(self):
        # hapus data contoh dengan mengosongkan tabel transaksi
        with models.koneksi() as db:
            db.execute("DELETE FROM transaksi")
        hasil = self.klien.get("/transaksi")
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Belum ada transaksi.", teks)

    def test_tambah_transaksi_valid(self):
        hasil = self.klien.post(
            "/transaksi/tambah",
            data={"id_pelanggan": "1", "id_layanan": "1", "tanggal": "2026-11-21", "berat": "2.5"},
            follow_redirects=True,
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Transaksi berhasil ditambahkan.", teks)
        self.assertIn("Pelanggan Uji", teks)
        self.assertIn("Cuci Kering", teks)
        self.assertIn("Rp 17.500", teks)

    def test_pelanggan_tidak_ditemukan_ditolak(self):
        hasil = self.klien.post(
            "/transaksi/tambah",
            data={"id_pelanggan": "999", "id_layanan": "1", "tanggal": "2026-11-21", "berat": "1"},
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Pelanggan tidak ditemukan.", teks)
        self.assertEqual(len(models.semua_transaksi()), 0)

    def test_layanan_tidak_ditemukan_ditolak(self):
        hasil = self.klien.post(
            "/transaksi/tambah",
            data={"id_pelanggan": "1", "id_layanan": "999", "tanggal": "2026-11-21", "berat": "1"},
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Layanan tidak ditemukan.", teks)
        self.assertEqual(len(models.semua_transaksi()), 0)

    def test_berat_nol_ditolak(self):
        hasil = self.klien.post(
            "/transaksi/tambah",
            data={"id_pelanggan": "1", "id_layanan": "1", "tanggal": "2026-11-21", "berat": "0"},
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Berat harus lebih dari 0.", teks)
        self.assertEqual(len(models.semua_transaksi()), 0)

    def test_berat_bukan_angka_ditolak(self):
        hasil = self.klien.post(
            "/transaksi/tambah",
            data={"id_pelanggan": "1", "id_layanan": "1", "tanggal": "2026-11-21", "berat": "abc"},
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Berat harus berupa angka.", teks)
        self.assertEqual(len(models.semua_transaksi()), 0)

    def test_tanggal_salah_format_ditolak(self):
        hasil = self.klien.post(
            "/transaksi/tambah",
            data={"id_pelanggan": "1", "id_layanan": "1", "tanggal": "21-11-2026", "berat": "1"},
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Tanggal harus berformat TTTT-BB-HH.", teks)
        self.assertEqual(len(models.semua_transaksi()), 0)

    def test_pelanggan_belum_dipilih_ditolak(self):
        hasil = self.klien.post(
            "/transaksi/tambah",
            data={"id_pelanggan": "", "id_layanan": "1", "tanggal": "2026-11-21", "berat": "1"},
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Pilih pelanggan.", teks)

    def test_hapus_transaksi_berhasil(self):
        transaksi_id = models.tambah_transaksi(1, 1, "2026-11-21", 1.0, 7000)

        hasil = self.klien.post(
            f"/transaksi/{transaksi_id}/hapus",
            follow_redirects=True,
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Transaksi berhasil dihapus.", teks)
        self.assertIsNone(models.ambil_transaksi(transaksi_id))

    def test_hapus_lewat_get_405(self):
        transaksi_id = models.tambah_transaksi(1, 1, "2026-11-21", 1.0, 7000)

        hasil = self.klien.get(f"/transaksi/{transaksi_id}/hapus")

        self.assertEqual(hasil.status_code, 405)
        self.assertIsNotNone(models.ambil_transaksi(transaksi_id))

    def test_hapus_id_tidak_ditemukan_404(self):
        hasil = self.klien.post("/transaksi/999/hapus")
        self.assertEqual(hasil.status_code, 404)

    def test_pencarian_menampilkan_yang_cocok(self):
        models.tambah_transaksi(1, 1, "2026-11-21", 1.0, 7000)

        hasil = self.klien.get("/transaksi?q=Pelanggan")
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Pelanggan Uji", teks)

    def test_pencarian_tidak_ada_hasil(self):
        models.tambah_transaksi(1, 1, "2026-11-21", 1.0, 7000)

        hasil = self.klien.get("/transaksi?q=zzzz")
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Tidak ada transaksi yang cocok.", teks)

    def test_persen_dicari_sebagai_huruf_biasa(self):
        models.tambah_transaksi(1, 1, "2026-11-21", 1.0, 7000)

        hasil = self.klien.get("/transaksi?q=%25")
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Tidak ada transaksi yang cocok.", teks)

    def test_hapus_pelanggan_yang_dipakai_transaksi_ditolak(self):
        models.tambah_transaksi(1, 1, "2026-11-21", 1.0, 7000)

        hasil = self.klien.post("/pelanggan/1/hapus", follow_redirects=True)
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("masih dipakai pada transaksi", teks)
        self.assertIsNotNone(models.ambil_pelanggan(1))

    def test_hapus_layanan_yang_dipakai_transaksi_ditolak(self):
        # hapus layanan memerlukan peran Pemilik
        self.klien.post("/logout", follow_redirects=True)
        self.klien.post("/login", data={"username_email": "pemilik@example.com", "password": "pemilik123"})

        models.tambah_transaksi(1, 1, "2026-11-21", 1.0, 7000)

        hasil = self.klien.post("/layanan/1/hapus", follow_redirects=True)
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("masih dipakai pada transaksi", teks)
        self.assertIsNotNone(models.ambil_layanan(1))

    def test_nama_berisi_html_ter_escape(self):
        # tambah pelanggan dengan nama HTML lewat modul pelanggan
        from services import pelanggan_service
        pelanggan_service.tambah_pelanggan("<b>tes</b>")

        hasil = self.klien.get("/transaksi/tambah")
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("&lt;b&gt;tes&lt;/b&gt;", teks)

    def test_tanggal_tanpa_tanda_hubung_ditolak(self):
        hasil = self.klien.post(
            "/transaksi/tambah",
            data={"id_pelanggan": "1", "id_layanan": "1", "tanggal": "20261108", "berat": "1"},
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Tanggal harus berformat TTTT-BB-HH.", teks)
        hasil = self.klien.post(
            "/transaksi/tambah",
            data={"id_pelanggan": "1", "id_layanan": "1", "tanggal": "2026-11-21", "berat": "3"},
            follow_redirects=True,
        )
        teks = hasil.data.decode("utf-8")

        self.assertEqual(hasil.status_code, 200)
        self.assertIn("Rp 21.000", teks)


if __name__ == "__main__":
    unittest.main()
