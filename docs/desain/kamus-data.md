# KAMUS DATA

## Sistem Informasi Laundry Koin

### 1. Pendahuluan

Kamus data merupakan dokumen yang menjelaskan struktur data pada setiap tabel dalam database Sistem Informasi Laundry Koin. Dokumen ini berisi nama kolom, tipe data, ketentuan wajib diisi, jenis kunci, aturan nilai, serta sumber kebutuhan fungsional.

Kamus data disusun berdasarkan hasil normalisasi, ERD, dan kebutuhan fungsional sistem.

### 2. Kamus Data Tabel Pengguna

| Nama Kolom | Tipe Data | Wajib | Kunci | Aturan Nilai | Sumber KF |
|---|---|---|---|---|---|
| id_pengguna | INT | Ya | PK | Dibuat otomatis dan harus unik. | KF-01 |
| username_email | VARCHAR(100) | Ya | UK | Harus unik dan digunakan untuk login. | KF-01 |
| password_hash | VARCHAR(255) | Ya | - | Kata sandi disimpan dalam bentuk hash. | KF-01 |
| id_peran | INT | Ya | FK | Harus mengacu pada id_peran di tabel Peran. | KF-02 |

### 3. Kamus Data Tabel Peran

| Nama Kolom | Tipe Data | Wajib | Kunci | Aturan Nilai | Sumber KF |
|---|---|---|---|---|---|
| id_peran | INT | Ya | PK | Dibuat otomatis dan harus unik. | KF-02 |
| nama_peran | VARCHAR(50) | Ya | UK | Nama peran harus unik, misalnya Pemilik dan Admin/Operator. | KF-02 |

### 4. Kamus Data Tabel Pelanggan

| Nama Kolom | Tipe Data | Wajib | Kunci | Aturan Nilai | Sumber KF |
|---|---|---|---|---|---|
| id_pelanggan | INT | Ya | PK | Dibuat otomatis dan harus unik. | KF-08 |
| nama_pelanggan | VARCHAR(100) | Ya | - | Nama pelanggan harus diisi. | KF-08 |

### 5. Kamus Data Tabel Layanan

| Nama Kolom | Tipe Data | Wajib | Kunci | Aturan Nilai | Sumber KF |
|---|---|---|---|---|---|
| id_layanan | INT | Ya | PK | Dibuat otomatis dan harus unik. | KF-07 |
| nama_layanan | VARCHAR(100) | Ya | - | Nama layanan harus diisi. | KF-07, KF-09 |
| harga | INTEGER | Ya | - | Harga disimpan dalam bilangan bulat rupiah dan tidak boleh bernilai negatif. | KF-07, KF-09 |

### 6. Kamus Data Tabel Transaksi

| Nama Kolom | Tipe Data | Wajib | Kunci | Aturan Nilai | Sumber KF |
|---|---|---|---|---|---|
| id_transaksi | INT | Ya | PK | Dibuat otomatis dan harus unik. | KF-10 |
| id_pelanggan | INT | Ya | FK | Harus mengacu pada id_pelanggan di tabel Pelanggan. | KF-10 |
| id_layanan | INT | Ya | FK | Harus mengacu pada id_layanan di tabel Layanan. | KF-10 |
| tanggal | TEXT | Ya | - | Menyimpan tanggal transaksi dengan format YYYY-MM-DD. | KF-10 |
| berat | REAL | Ya | - | Berat laundry harus lebih besar dari nol dan menggunakan satuan kilogram. | KF-10 |
| total_biaya | INTEGER | Ya | - | Disimpan dalam bilangan bulat rupiah, tidak boleh negatif, dan mencatat biaya saat transaksi dilakukan. | KF-10 |

### 7. Kamus Data Tabel Mesin

| Nama Kolom | Tipe Data | Wajib | Kunci | Aturan Nilai | Sumber KF |
|---|---|---|---|---|---|
| id_mesin | INT | Ya | PK | Dibuat otomatis dan harus unik. | KF-14 |
| informasi_mesin | VARCHAR(150) | Ya | - | Menyimpan informasi atau identitas mesin. | KF-14 |
| status_mesin | VARCHAR(30) | Ya | - | Status wajib diisi dan maksimal 30 karakter. | KF-14 |

### 8. Keterangan Kunci

1. Primary Key (PK) merupakan kunci utama untuk mengidentifikasi setiap data secara unik.
2. Foreign Key (FK) merupakan kunci asing yang menghubungkan satu tabel dengan tabel lainnya.
3. Unique Key (UK) merupakan kunci yang memastikan nilai pada suatu kolom tidak boleh sama atau duplikat.
4. Kolom yang ditandai wajib harus memiliki nilai dan tidak boleh kosong.

### 9. Catatan Perancangan

1. Tipe data disesuaikan dengan SQLite. Kolom harga dan total_biaya menggunakan INTEGER, berat menggunakan REAL, tanggal menggunakan TEXT berformat YYYY-MM-DD, sedangkan kolom teks menggunakan VARCHAR sesuai batas panjang yang ditetapkan.
2. Seluruh ID direncanakan menggunakan nomor otomatis (auto increment).
3. Kata sandi pengguna harus disimpan dalam bentuk hash untuk menjaga keamanan akun.
4. Nilai total_biaya disimpan sebagai catatan biaya pada saat transaksi dilakukan agar riwayat transaksi tidak berubah ketika harga layanan diperbarui.
5. Atribut berat digunakan berdasarkan contoh data transaksi laundry simulasi dengan perhitungan kilogram.
6. Pengelolaan mesin saat ini dibatasi pada informasi dan status mesin sesuai kebutuhan KF-14. Status mesin wajib diisi dan dibatasi maksimal 30 karakter.

### 10. Sumber

1. Software Requirements Specification (SRS) Sistem Informasi Laundry Koin.
2. Dokumen Daftar Entitas.
3. Dokumen Atribut Entitas.
4. Dokumen Relasi dan Kardinalitas Entitas.
5. Dokumen Normalisasi Database Sistem Informasi Laundry Koin.
