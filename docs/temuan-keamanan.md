# TEMUAN KEAMANAN — AUTENTIKASI DAN OTORISASI

## Sistem Informasi Laundry Koin

### 1. Ruang Lingkup
Tinjauan dilakukan pada diff autentikasi dan otorisasi (Langkah 7) dengan daftar periksa Lampiran C.2 (Jobsheet 11).

### 2. Temuan dan Tindakan

| No | Temuan | Kategori | Tindakan |
|---|---|---|---|
| 1 | Batas percobaan login belum diterapkan; brute force memungkinkan. | Keamanan | Dicatat untuk Minggu 12 — perlu pembatasan percobaan per IP/akun. |
| 2 | Token CSRF belum ada pada form login, tambah, ubah, dan hapus. | Keamanan | Dicatat untuk Minggu 12 — sama dengan modul sebelumnya. |
| 3 | Cookie sesi belum memakai `Secure` (hanya cocok untuk HTTPS produksi). | Keamanan | Dicatat untuk Minggu 12 — aktifkan saat deploy HTTPS. |
| 4 | Parameter `next` sudah dibatasi agar tidak redirect ke luar situs. | Keamanan | Sudah diperbaiki (fungsi `alamat_next_aman`). |
| 5 | Kata sandi disimpan sebagai hash (scrypt) dengan garam otomatis. | Keamanan | Sesuai; tidak ada kata sandi polos di kode. |
| 6 | Penegakan peran dilakukan di server (decorator), bukan hanya menyembunyikan tautan. | Keamanan | Sesuai; uji 403 pada halaman dan POST lulus. |

### 3. Kesimpulan
Tidak ada kata sandi polos di kode; penegakan akses berjalan di server. Temuan yang belum dapat diperbaiki hari ini dicatat sebagai bahan Pertemuan 12.
