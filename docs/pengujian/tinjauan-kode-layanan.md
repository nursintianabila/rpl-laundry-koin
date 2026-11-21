# TINJAUAN KODE MODUL CRUD LAYANAN

## Sistem Informasi Laundry Koin

### 1. Ruang Lingkup

Tinjauan dilakukan pada seluruh diff branch `fitur/kerangka` terhadap `main`, meliputi `app.py`, `models.py`, `routes/layanan_routes.py`, `services/layanan_service.py`, template, dan pengujian.

### 2. Daftar Periksa

| Butir | Hasil |
|---|---|
| SQL hanya berada di `models.py` | Sesuai |
| Query menggunakan parameter (`?`) | Sesuai |
| Routes tidak membuka koneksi SQLite | Sesuai |
| Validasi dilakukan di server | Sesuai |
| Isian dipertahankan saat galat | Sesuai |
| Hapus hanya melalui POST | Sesuai |
| Data tidak ditemukan menghasilkan 404 | Sesuai |
| Kunci rahasia tidak ditulis di kode | Sesuai |
| Template meng-escape HTML (Jinja2) | Sesuai |
| Struktur folder mengikuti `aturan-proyek.md` | Sesuai |

### 3. Temuan dan Tindakan

| No | Temuan | Kategori | Tindakan |
|---|---|---|---|
| 1 | CSS ditulis inline di `templates/base.html` sehingga sulit dipelihara dan tidak memakai folder `static/` sesuai struktur target. | Keterbacaan | **Diperbaiki sekarang** — dipindahkan ke `static/css/style.css` dan dimuat melalui `url_for('static', ...)`. |
| 2 | Pesan sukses dan pesan galat sama-sama memakai gaya `.pesan` (hijau), sehingga kegagalan hapus karena kunci asing terlihat seperti keberhasilan. | Kesesuaian | **Diperbaiki sekarang** — flash memakai kategori `sukses`/`galat` dan template memilih kelas yang sesuai. |
| 3 | Nama layanan hanya dicek di service; `schema.sql` belum memiliki constraint `UNIQUE` pada `nama_layanan`, sehingga dua permintaan bersamaan masih berpotensi menyimpan nama ganda. | Kebenaran | **Dicatat untuk Minggu 12** — perlu perubahan skema, kamus data, dan migrasi; harus disepakati lebih dahulu. |
| 4 | Form tambah, ubah, dan hapus belum memiliki token CSRF. | Keamanan | **Dicatat untuk Minggu 12** — perlu paket tambahan (butuh persetujuan) atau token khusus; belum dikerjakan pada jobsheet ini. |
| 5 | `app = buat_aplikasi()` di level modul membuat basis data saat modul diimpor, termasuk saat pengujian. | Keterbacaan | **Ditolak untuk sekarang** — pola ini umum untuk aplikasi Flask sederhana dan tidak mengubah data; ditinjau ulang bila application factory penuh diterapkan. |

### 4. Kesimpulan

Tiga temuan sudah ditindaklanjuti atau diputuskan tindakannya. Tidak ada SQL di routes, tidak ada data rahasia di kode, dan seluruh alur CRUD dapat dijelaskan melalui pemisahan routes → services → models → database.
