

# SKENARIO USE CASE



## Sistem Informasi Laundry Koin



### 1. Skenario UC-01 — Login Pengguna



**Aktor:** Pemilik dan Admin/Operator



**KF:** KF-01



**Prasyarat:**

- Pengguna telah memiliki akun yang terdaftar.

- Sistem dapat diakses.



**Alur Utama:**

1. Pengguna membuka halaman login.

2. Sistem menampilkan formulir login.

3. Pengguna memasukkan username/email dan password.

4. Sistem memeriksa kecocokan data login.

5. Sistem mengizinkan pengguna masuk ke aplikasi sesuai perannya.

6. Pengguna berhasil masuk ke halaman sistem.



**Alur Alternatif:**

1. Pengguna memasukkan username atau email yang terdaftar.

2. Pengguna memasukkan password yang benar.

3. Sistem memproses data dan mengizinkan pengguna masuk.



**Pengecualian:**

- Jika username/email atau password tidak sesuai, sistem menolak proses login dan menampilkan informasi kesalahan.

- Jika data wajib belum diisi, sistem menampilkan validasi pada formulir.



**Pascakondisi:**

- Pengguna berhasil masuk ke sistem.

- Sesi pengguna aktif sesuai perannya.



---



### 2. Skenario UC-02 — Mengakses Fitur Sesuai Hak Akses



**Aktor:** Pemilik dan Admin/Operator



**KF:** KF-02



**Prasyarat:**

- Pengguna telah berhasil login.

- Pengguna memiliki peran yang terdaftar dalam sistem.



**Alur Utama:**

1. Pengguna membuka menu atau fitur yang tersedia.

2. Sistem memeriksa peran dan hak akses pengguna.

3. Pengguna memilih fitur yang sesuai dengan perannya.

4. Sistem memeriksa izin akses terhadap fitur tersebut.

5. Sistem menampilkan halaman fitur yang diizinkan.



**Alur Alternatif:**

1. Pemilik memilih fitur pengelolaan layanan dan harga.

2. Sistem memeriksa hak akses Pemilik.

3. Sistem mengizinkan Pemilik membuka fitur tersebut.



**Pengecualian:**

- Jika pengguna mencoba membuka menu yang tidak sesuai dengan hak aksesnya, sistem menolak akses tersebut.

- Sistem tidak menampilkan halaman atau fungsi yang tidak diizinkan kepada pengguna.



**Pascakondisi:**

- Pengguna hanya dapat mengakses fitur sesuai hak akses yang diberikan.

- Hak akses pengguna tetap mengikuti peran yang terdaftar.



---



### 3. Skenario UC-06 — Mengelola Layanan dan Harga



**Aktor:** Pemilik



**KF:** KF-07



**Prasyarat:**

- Pemilik telah berhasil login.

- Pemilik memiliki hak akses untuk mengelola layanan dan harga.



**Alur Utama:**

1. Pemilik membuka menu layanan dan harga.

2. Sistem menampilkan daftar layanan beserta harga yang tersimpan.

3. Pemilik memilih fungsi tambah layanan.

4. Sistem menampilkan formulir data layanan.

5. Pemilik memasukkan nama layanan dan harga.

6. Sistem memvalidasi data yang dimasukkan.

7. Pemilik menyimpan data layanan.

8. Sistem menyimpan data layanan dan harga.

9. Sistem menampilkan data layanan yang telah diperbarui.



**Alur Alternatif:**

1. Pemilik memilih layanan yang sudah tersedia.

2. Pemilik memilih fungsi ubah atau hapus data layanan.

3. Sistem menampilkan data layanan yang dipilih.

4. Pemilik melakukan perubahan atau menghapus data.

5. Sistem menyimpan perubahan atau penghapusan tersebut.



**Pengecualian:**

- Jika data wajib belum diisi atau tidak valid, sistem menolak penyimpanan dan menampilkan informasi kesalahan.

- Jika proses penyimpanan gagal, sistem menampilkan informasi bahwa perubahan belum berhasil disimpan.



**Pascakondisi:**

- Data layanan dan harga tersimpan sesuai tindakan Pemilik.

- Daftar layanan menampilkan data terbaru.



---



### 4. Skenario UC-07 — Mengelola Data Pelanggan



**Aktor:** Admin/Operator



**KF:** KF-08



**Prasyarat:**

- Admin/Operator telah berhasil login.

- Admin/Operator memiliki hak akses pengelolaan pelanggan.



**Alur Utama:**

1. Admin/Operator membuka menu pelanggan.

2. Sistem menampilkan daftar pelanggan.

3. Admin/Operator memilih fungsi tambah pelanggan.

4. Sistem menampilkan formulir data pelanggan.

5. Admin/Operator memasukkan data pelanggan.

6. Sistem memvalidasi data yang dimasukkan.

7. Admin/Operator menyimpan data pelanggan.

8. Sistem menyimpan data pelanggan.

9. Sistem menampilkan daftar pelanggan yang telah diperbarui.



**Alur Alternatif:**

1. Admin/Operator memilih salah satu data pelanggan.

2. Sistem menampilkan informasi pelanggan yang dipilih.

3. Admin/Operator memilih fungsi ubah atau hapus.

4. Admin/Operator melakukan perubahan atau menghapus data pelanggan.

5. Sistem menyimpan perubahan atau penghapusan data.



**Pengecualian:**

- Jika data wajib belum diisi atau tidak valid, sistem menolak penyimpanan dan menampilkan informasi kesalahan.

- Jika proses penyimpanan gagal, sistem menampilkan informasi bahwa perubahan belum berhasil disimpan.



**Pascakondisi:**

- Data pelanggan tersimpan sesuai tindakan Admin/Operator.

- Daftar pelanggan menampilkan data terbaru.



---



### 5. Skenario UC-09 — Mengelola Transaksi



**Aktor:** Admin/Operator



**KF:** KF-10, KF-11, KF-12



**Prasyarat:**

- Admin/Operator telah berhasil login.

- Data pelanggan dan layanan telah tersedia.

- Admin/Operator memiliki hak akses pengelolaan transaksi.



**Alur Utama:**

1. Admin/Operator membuka menu transaksi.

2. Sistem menampilkan halaman pengelolaan transaksi.

3. Admin/Operator memilih pelanggan dan layanan.

4. Sistem menampilkan informasi pelanggan dan layanan yang dipilih.

5. Admin/Operator memasukkan tanggal dan data wajib transaksi lainnya.

6. Sistem menghitung total biaya berdasarkan data transaksi.

7. Admin/Operator memeriksa dan menyimpan transaksi.

8. Sistem memvalidasi data transaksi.

9. Sistem menyimpan transaksi dan menampilkan informasi transaksi yang berhasil dicatat.



**Alur Alternatif:**

1. Admin/Operator membuka transaksi yang telah tersimpan.

2. Sistem menampilkan rincian transaksi.

3. Admin/Operator memilih fungsi ubah data transaksi yang diizinkan.

4. Admin/Operator memperbarui data transaksi.

5. Sistem menyimpan perubahan transaksi.

6. Admin/Operator melakukan pencarian riwayat berdasarkan informasi transaksi yang tersedia.

7. Sistem menampilkan transaksi yang sesuai dengan pencarian.



**Pengecualian:**

- Jika pelanggan atau layanan belum dipilih, sistem menolak penyimpanan transaksi dan menampilkan validasi.

- Jika data wajib transaksi belum lengkap atau tidak valid, sistem menolak penyimpanan dan menampilkan informasi kesalahan.

- Jika transaksi yang dicari tidak ditemukan, sistem menampilkan bahwa tidak ada transaksi yang sesuai.

- Jika pengguna tidak memiliki hak akses untuk mengubah transaksi, sistem menolak perubahan tersebut.



**Pascakondisi:**

- Data transaksi baru tersimpan apabila proses pencatatan berhasil.

- Perubahan transaksi tersimpan apabila proses perubahan berhasil.

- Riwayat transaksi dapat ditampilkan berdasarkan informasi pencarian yang sesuai.




