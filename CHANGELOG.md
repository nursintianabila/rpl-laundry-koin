# CHANGELOG

Semua perubahan penting dicatat dalam berkas ini.
Format mengikuti Keep a Changelog, versi mengikuti Semantic Versioning.

## [1.0.0] - 2026-11-21

### Fitur
- Login dan otorisasi dua peran (Pemilik, Admin/Operator) dengan kata sandi ter-hash.
- Pengelolaan layanan dan harga dengan validasi.
- Pengelolaan data pelanggan dengan validasi.
- Pencatatan transaksi dengan perhitungan total biaya dan foreign key.
- Pencarian dan penyaringan transaksi berparameter.

### Perbaikan
- Perbaikan cacat tanggal tanpa tanda hubung dan angka Unicode pada harga.
- Penambahan token CSRF, batas percobaan login, dan header keamanan.
- Perbaikan diff dan temuan tinjauan kode.

### Keamanan
- Kata sandi tersimpan sebagai hash Werkzeug (scrypt/pbkdf2).
- `SECRET_KEY` dari variabel lingkungan; produksi menolak start tanpa kunci.
- Parameter `next` dibatasi agar tidak redirect ke situs luar.
