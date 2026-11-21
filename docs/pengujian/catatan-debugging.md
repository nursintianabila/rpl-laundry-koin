# CATATAN DEBUGGING — JOBSHEET 10

## Sistem Informasi Laundry Koin

### Catatan 1 — Typo nama fungsi

| Bagian | Isi |
|---|---|
| Gejala | Membuka `/transaksi/tambah` dengan isian valid menghasilkan halaman 500 Internal Server Error. |
| Langkah reproduksi | 1. Jalankan aplikasi. 2. Buka `/transaksi/tambah`. 3. Isi pelanggan, layanan, tanggal, dan berat, lalu kirim. |
| Traceback ringkas | `services/transaksi_service.py`, baris 49, fungsi `periksa_isian`: `AttributeError: module 'models' has no attribute 'ambil_pelangganx'` |
| Hipotesis | Nama fungsi pada pemanggilan salah ketik. |
| Prompt ke AI | Traceback lengkap + potongan `periksa_isian` + langkah reproduksi; minta penjelasan penyebab terlebih dahulu. |
| Penjelasan penyebab dari AI | Pemanggilan `models.ambil_pelangganx` tidak ada pada modul `models`; nama fungsi yang benar adalah `ambil_pelanggan`. |
| Perbaikan | Ganti `ambil_pelangganx` menjadi `ambil_pelanggan` (Terima). |
| Pencegahan | Uji tambah transaksi valid pada `tests/test_transaksi.py` dan `tests/uji_cepat.py`. |

### Catatan 2 — Typo nama kolom pada query

| Bagian | Isi |
|---|---|
| Gejala | Membuka `/transaksi` menghasilkan halaman 500 Internal Server Error. |
| Langkah reproduksi | 1. Jalankan aplikasi. 2. Buka `/transaksi`. |
| Traceback ringkas | `models.py`, fungsi `cari_transaksi`: `sqlite3.OperationalError: no such column: p.nama_pelangganx` |
| Hipotesis | Nama kolom pada query tidak sama dengan skema. |
| Prompt ke AI | Traceback lengkap + potongan query + `schema.sql` tabel `pelanggan`; minta penjelasan penyebab terlebih dahulu. |
| Penjelasan penyebab dari AI | Kolom `nama_pelangganx` tidak ada pada tabel `pelanggan`; kolom yang benar adalah `nama_pelanggan`. |
| Perbaikan | Ganti `nama_pelangganx` menjadi `nama_pelanggan` (Terima). |
| Pencegahan | Uji daftar dan pencarian transaksi pada `tests/test_transaksi.py` dan `tests/uji_cepat.py`. |
