# UJI ALUR DAN AKSES — JOBSHEET 13 LANGKAH 9

## Sistem Informasi Laundry Koin

### Alur dua peran (Lampiran D.1)
1. Masuk sebagai Pemilik → tambah layanan "Cuci Express" → keluar.
2. Masuk sebagai Admin/Operator → tambah pelanggan "Pelanggan Integrasi" → catat transaksi → coba aksi terlarang (tambah layanan) → 403 → keluar.
3. Tamu membuka /layanan → dialihkan ke login.

Hasil: alur berjalan tanpa langkah manual di basis data; setiap aksi terlarang menghasilkan 403.

### Uji akses langsung (mengetik alamat)
| Skenario | Hasil diharapkan | Hasil nyata |
|---|---|---|
| Tamu membuka /pelanggan | Dialihkan ke login | Lulus (302 /login?next=/pelanggan) |
| Pemilik membuka /pelanggan | 403 | Lulus |
| Pemilik POST /pelanggan/1/hapus | 403; data tidak berubah | Lulus |
| Admin membuka /layanan/tambah | 403 | Lulus |
| Admin membuka /pelanggan | 200 | Lulus |
