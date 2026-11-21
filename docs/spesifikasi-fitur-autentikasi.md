# SPESIFIKASI FITUR AUTENTIKASI DAN OTORISASI

## Sistem Informasi Laundry Koin

### 1. Peran
- **Pemilik**: melihat transaksi, mengelola layanan dan harga.
- **Admin/Operator**: mengelola pelanggan, layanan, transaksi, dan status mesin.

### 2. Aturan
- Kata sandi disimpan dalam bentuk hash (werkzeug.security).
- Sesi hanya menyimpan `pengguna_id`.
- `secret_key` dari variabel lingkungan `SECRET_KEY`.
- Logout hanya lewat POST.
- Parameter `next` hanya diterima bila dimulai dengan `/` dan bukan `//`.
- Penegakan akses di server melalui decorator `peran_diperlukan`.

### 3. Akun Awal
Akun dibuat dengan skrip `buat_pengguna.py` yang membaca kata sandi dari terminal.
