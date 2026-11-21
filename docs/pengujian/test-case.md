# TEST CASE — SISTEM INFORMASI LAUNDRY KOIN

## Jobsheet 13 Langkah 4

| ID | Fitur | Masukan | Hasil yang diharapkan |
|---|---|---|---|
| TC-01 | Daftar layanan | Buka /layanan saat ada data | Tabel ID, nama, harga, aksi tampil |
| TC-02 | Tambah layanan | Nama "Cuci Kering", harga 7000 | Tersimpan, pesan sukses, tampil |
| TC-03 | Tambah layanan | Nama kosong | Ditolak, pesan "Nama layanan wajib diisi." |
| TC-04 | Tambah layanan | Harga -5 | Ditolak, pesan "Harga tidak boleh negatif." |
| TC-05 | Tambah layanan | Harga "abc" | Ditolak, pesan "Harga harus berupa bilangan bulat..." |
| TC-06 | Tambah layanan | Nama duplikat | Ditolak, pesan "Nama layanan sudah ada." |
| TC-07 | Ubah layanan | Data valid | Perubahan tersimpan |
| TC-08 | Ubah layanan | Nama duplikat | Ditolak |
| TC-09 | Ubah layanan | ID 999 | 404 |
| TC-10 | Hapus layanan | Tidak dipakai transaksi | Terhapus |
| TC-11 | Hapus layanan | Dipakai transaksi | Ditolak, pesan galat |
| TC-12 | Hapus layanan | GET /layanan/1/hapus | 405 |
| TC-13 | Daftar pelanggan | Buka /pelanggan | Tabel tampil |
| TC-14 | Tambah pelanggan | Nama "Nabila" | Tersimpan |
| TC-15 | Tambah pelanggan | Nama kosong | Ditolak |
| TC-16 | Ubah pelanggan | Data valid | Perubahan tersimpan |
| TC-17 | Hapus pelanggan | Dipakai transaksi | Ditolak |
| TC-18 | Tambah transaksi | Data valid | Tersimpan, total dihitung |
| TC-19 | Tambah transaksi | Pelanggan 999 | Ditolak |
| TC-20 | Tambah transaksi | Layanan 999 | Ditolak |
| TC-21 | Tambah transaksi | Berat 0 | Ditolak |
| TC-22 | Tambah transaksi | Tanggal "21-11-2026" | Ditolak |
| TC-23 | Hapus transaksi | ID valid | Terhapus |
| TC-24 | Pencarian transaksi | ?q=Pelanggan | Baris cocok tampil |
| TC-25 | Pencarian transaksi | ?q=zzzz | Pesan "Tidak ada transaksi yang cocok." |
| TC-26 | Informasi layanan | Daftar layanan | Harga format rupiah |
| TC-27 | Validasi | Isian galat | Isian dipertahankan |
| TC-28 | Validasi | Nama "<b>tes</b>" | Tampil ter-escape |
| TC-29 | Validasi | Nama "Robert'); DROP TABLE..." | Tersimpan sebagai teks |
| TC-30 | Autentikasi | Tamu buka /layanan | Redirect ke login |
| TC-31 | Autentikasi | Kredensial salah / user tidak ada | Pesan sama |
| TC-32 | Otorisasi | Pemilik buka /pelanggan | 403 |
| TC-33 | Autentikasi | Akun tersimpan | Hash scrypt/pbkdf2 |
| TC-34 | CSRF | POST tanpa token | 400 |
| TC-35 | Batas login | 6x gagal | 429 |
| TC-36 | Header | Respons HTTP | X-Content-Type-Options, X-Frame-Options, Referrer-Policy |

Total: 36 test case (>= 20).
