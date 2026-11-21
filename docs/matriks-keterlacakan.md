# MATRIKS KETERLACAKAN — SISTEM INFORMASI LAUNDRY KOIN

## Jobsheet 13 Langkah 3

| ID Kebutuhan | Fitur | Test Case | Deskripsi singkat |
|---|---|---|---|
| KF-02 | Pengelolaan layanan dan harga | TC-01 | Daftar layanan menampilkan data yang tersimpan |
| KF-02 | Pengelolaan layanan dan harga | TC-02 | Tambah layanan valid tersimpan |
| KF-02 | Pengelolaan layanan dan harga | TC-03 | Tambah layanan nama kosong ditolak |
| KF-02 | Pengelolaan layanan dan harga | TC-04 | Tambah layanan harga negatif ditolak |
| KF-02 | Pengelolaan layanan dan harga | TC-05 | Tambah layanan harga bukan angka ditolak |
| KF-02 | Pengelolaan layanan dan harga | TC-06 | Tambah layanan nama duplikat ditolak |
| KF-02 | Pengelolaan layanan dan harga | TC-07 | Ubah layanan berhasil |
| KF-02 | Pengelolaan layanan dan harga | TC-08 | Ubah layanan nama duplikat ditolak |
| KF-02 | Pengelolaan layanan dan harga | TC-09 | Ubah layanan ID tidak ada -> 404 |
| KF-02 | Pengelolaan layanan dan harga | TC-10 | Hapus layanan tidak dipakai berhasil |
| KF-02 | Pengelolaan layanan dan harga | TC-11 | Hapus layanan dipakai transaksi ditolak |
| KF-02 | Pengelolaan layanan dan harga | TC-12 | Hapus layanan lewat GET -> 405 |
| KF-03 | Pengelolaan data pelanggan | TC-13 | Daftar pelanggan menampilkan data |
| KF-03 | Pengelolaan data pelanggan | TC-14 | Tambah pelanggan valid |
| KF-03 | Pengelolaan data pelanggan | TC-15 | Tambah pelanggan nama kosong ditolak |
| KF-03 | Pengelolaan data pelanggan | TC-16 | Ubah pelanggan berhasil |
| KF-03 | Pengelolaan data pelanggan | TC-17 | Hapus pelanggan dipakai transaksi ditolak |
| KF-04 | Pencatatan transaksi | TC-18 | Tambah transaksi valid, total dihitung |
| KF-04 | Pencatatan transaksi | TC-19 | Tambah transaksi pelanggan tidak ada ditolak |
| KF-04 | Pencatatan transaksi | TC-20 | Tambah transaksi layanan tidak ada ditolak |
| KF-04 | Pencatatan transaksi | TC-21 | Tambah transaksi berat 0 ditolak |
| KF-04 | Pencatatan transaksi | TC-22 | Tambah transaksi tanggal salah ditolak |
| KF-04 | Pencatatan transaksi | TC-23 | Hapus transaksi berhasil |
| KF-05 | Riwayat transaksi | TC-24 | Pencarian transaksi menampilkan yang cocok |
| KF-05 | Riwayat transaksi | TC-25 | Pencarian transaksi tanpa hasil menampilkan pesan |
| KF-10 | Informasi layanan dan harga | TC-26 | Daftar layanan menampilkan harga format rupiah |
| KQ-02 | Validasi data wajib | TC-27 | Isian dipertahankan saat galat |
| KQ-02 | Validasi data wajib | TC-28 | Masukan HTML tampil ter-escape |
| KQ-02 | Validasi data wajib | TC-29 | Masukan SQL tersimpan sebagai teks |
| H1-H3 | Autentikasi dan otorisasi | TC-30 | Tamu dialihkan ke login |
| H1-H3 | Autentikasi dan otorisasi | TC-31 | Kredensial salah dan pengguna tidak ada pesan sama |
| H1-H3 | Autentikasi dan otorisasi | TC-32 | Peran terbatas mendapat 403 |
| H1-H3 | Autentikasi dan otorisasi | TC-33 | Kata sandi tersimpan sebagai hash |
| H1-H3 | Autentikasi dan otorisasi | TC-34 | POST tanpa token CSRF ditolak 400 |
| H1-H3 | Autentikasi dan otorisasi | TC-35 | Batas percobaan login 429 |
| H1-H3 | Autentikasi dan otorisasi | TC-36 | Header keamanan hadir |

Total: 36 test case.
