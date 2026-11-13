
# ATRIBUT ENTITAS

## Sistem Informasi Laundry Koin

### 1. Pendahuluan

Dokumen ini berisi daftar atribut dari setiap entitas yang digunakan dalam perancangan Sistem Informasi Laundry Koin. Setiap entitas memiliki kunci utama (Primary Key/PK) sebagai identitas unik data. Atribut yang berhubungan dengan entitas lain menggunakan kunci asing (Foreign Key/FK).

### 2. Daftar Atribut dan Batasan

| Entitas | Atribut | Catatan Batasan |
|---|---|---|
| Pengguna | id_pengguna (PK), username_email (UK), password_hash, id_peran (FK) | ID dibuat otomatis; username/email wajib dan unik; kata sandi disimpan dalam bentuk hash; id_peran harus mengacu pada tabel Peran. |
| Peran | id_peran (PK), nama_peran (UK) | ID dibuat otomatis; nama_peran wajib diisi dan harus unik. |
| Pelanggan | id_pelanggan (PK), nama_pelanggan | ID dibuat otomatis; nama pelanggan wajib diisi. |
| Layanan | id_layanan (PK), nama_layanan, harga | ID dibuat otomatis; nama_layanan wajib diisi; harga tidak boleh negatif. |
| Transaksi | id_transaksi (PK), id_pelanggan (FK), id_layanan (FK), tanggal, berat, total_biaya | ID dibuat otomatis; pelanggan dan layanan wajib dipilih; tanggal dan berat wajib diisi; berat harus lebih besar dari nol; total_biaya tidak boleh negatif. |
| Mesin | id_mesin (PK), informasi_mesin, status_mesin | ID dibuat otomatis; informasi mesin wajib diisi; status mesin harus mengikuti pilihan status yang ditentukan sistem. |

### 3. Keterangan Kunci

1. Primary Key (PK) merupakan atribut yang digunakan sebagai identitas unik setiap data.
2. Foreign Key (FK) merupakan atribut yang menghubungkan satu tabel dengan tabel lainnya.
3. Unique Key (UK) merupakan atribut yang nilainya tidak boleh sama atau duplikat.
4. Atribut id_peran pada tabel Pengguna menjadi FK yang mengacu pada id_peran di tabel Peran.
5. Atribut id_pelanggan pada tabel Transaksi menjadi FK yang mengacu pada id_pelanggan di tabel Pelanggan.
6. Atribut id_layanan pada tabel Transaksi menjadi FK yang mengacu pada id_layanan di tabel Layanan.

### 4. Catatan Perancangan

1. ID pada setiap entitas direncanakan menggunakan nomor otomatis (auto increment).
2. Kata sandi pengguna harus disimpan dalam bentuk hash untuk menjaga keamanan akun.
3. Atribut berat menggunakan satuan kilogram berdasarkan contoh data transaksi laundry simulasi.
4. Atribut total_biaya tetap disimpan sebagai nilai transaksi saat transaksi dilakukan agar riwayat biaya tidak berubah ketika harga layanan diperbarui.
5. Atribut informasi_mesin masih dapat dirinci sesuai informasi mesin yang akan dikelola.
6. Rincian atribut dan batasan dapat diperbarui apabila terdapat perubahan kebutuhan sistem.

### 5. Sumber

1. Product Requirements Document (PRD) Sistem Informasi Laundry Koin.
2. Software Requirements Specification (SRS) Sistem Informasi Laundry Koin.
3. Dokumen Daftar Use Case Sistem Informasi Laundry Koin.
4. Dokumen ERD Sistem Informasi Laundry Koin.
