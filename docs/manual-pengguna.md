# MANUAL PENGGUNA — SISTEM INFORMASI LAUNDRY KOIN

## Sistem Informasi Laundry Koin v1.0.0

### 1. Masuk ke aplikasi

1. Buka alamat aplikasi di peramban.
2. Masukkan nama pengguna (email) dan kata sandi.
3. Klik **Masuk**.
4. Anda akan diarahkan ke halaman sesuai peran.

### 2. Melihat daftar layanan dan harga

1. Pilih menu **Layanan**.
2. Tabel menampilkan ID, nama layanan, harga, dan aksi.

### 3. Menambah layanan (Pemilik)

1. Pada halaman Layanan, klik **+ Tambah Layanan**.
2. Isi nama layanan dan harga.
3. Klik **Simpan**.
4. Pesan "Layanan berhasil ditambahkan." muncul dan data tampil di daftar.

### 4. Mengubah layanan (Pemilik)

1. Pada baris layanan yang ingin diubah, klik **Ubah**.
2. Ubah nama atau harga.
3. Klik **Simpan**.

### 5. Menghapus layanan (Pemilik)

1. Pada baris layanan, klik **Hapus**.
2. Konfirmasi penghapusan.
3. Layanan yang sudah dipakai transaksi tidak dapat dihapus dan akan muncul pesan.

### 6. Mengelola data pelanggan (Admin/Operator)

1. Pilih menu **Pelanggan**.
2. Klik **+ Tambah Pelanggan** untuk menambah data.
3. Isi nama pelanggan, lalu klik **Simpan**.
4. Gunakan tombol **Ubah** atau **Hapus** pada baris yang bersangkutan.

### 7. Mencatat transaksi (Admin/Operator)

1. Pilih menu **Transaksi**.
2. Klik **+ Tambah Transaksi**.
3. Ketik sebagian nama pelanggan pada kolom **Pelanggan** (misal `nur`); daftar saran akan muncul, lalu klik nama yang diinginkan atau tekan Enter untuk memilih saran pertama.
4. Pilih layanan, isi berat (kg) dan tanggal (TTTT-BB-HH).
5. Klik **Simpan**.
6. Total biaya dihitung otomatis dari berat dikali harga layanan.
7. Setelah pakaian selesai dicuci, pada baris transaksi klik **Tandai Selesai**.
### 8. Mencari transaksi

1. Pada halaman Transaksi, ketik nama pelanggan atau layanan pada kolom pencarian.
2. Pilih layanan pada filter jika diperlukan.
3. Klik **Cari**.
4. Gunakan **Atur ulang** untuk menghapus pencarian.

### 9. Melihat dashboard dan laporan (Pemilik)

1. Pilih menu **Dashboard** untuk melihat jumlah layanan, pelanggan, transaksi, total pendapatan, dan transaksi terbaru.
   - Klik **Unduh CSV (Excel)** atau **Unduh PDF** untuk menyimpan data transaksi. CSV langsung dibuka di Excel; PDF untuk arsip.
   - Admin juga melihat notifikasi transaksi yang baru ditandai selesai, misalnya "Nabila — Cuci Kering sudah selesai."
2. Pilih menu **Laporan** untuk melihat total pendapatan. Isi tanggal mulai dan tanggal akhir bila ingin membatasi periode, lalu klik **Tampilkan**.
3. Menu **Riwayat Transaksi** menampilkan daftar transaksi hanya-baca untuk Pemilik.

### 10. Memperbarui status mesin (Admin/Operator)

1. Pilih menu **Status Mesin**.
2. Pilih status baru pada baris mesin yang bersangkutan.
3. Klik **Simpan**. Pesan "Status mesin berhasil diperbarui." akan muncul.

### 11. Keluar dari aplikasi

1. Klik tombol **Keluar** di kanan atas.
2. Anda akan kembali ke halaman login.

### Bila ada masalah

| Pesan / kondisi | Penyebab | Cara mengatasi |
|---|---|---|
| "Nama pengguna atau kata sandi salah." | Kredensial salah | Periksa kembali nama pengguna dan kata sandi. |
| "Terlalu banyak percobaan..." | 5 kali login gagal | Tunggu 5 menit, lalu coba lagi. |
| "Nama layanan wajib diisi." | Nama kosong | Isi nama layanan. |
| "Harga tidak boleh negatif." | Harga minus | Masukkan harga 0 atau lebih. |
| "Nama layanan sudah ada." | Nama duplikat | Gunakan nama lain. |
| "Layanan tidak dapat dihapus karena masih dipakai pada transaksi." | Data dipakai transaksi | Hapus transaksi terkait terlebih dahulu atau jangan hapus layanan. |
| "Tidak ada transaksi yang cocok." | Pencarian tidak menemukan data | Ubah kata kunci atau atur ulang pencarian. |
| Halaman 403 | Hak akses tidak sesuai | Masuk dengan peran yang sesuai. |
| POST tanpa token ditolak (400) | Token CSRF hilang | Muat ulang halaman dan kirim kembali formulir. |

Catatan: seluruh data pada contoh ini adalah data karangan.
