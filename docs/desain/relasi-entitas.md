
# RELASI DAN KARDINALITAS ENTITAS

## Sistem Informasi Laundry Koin

### 1. Pendahuluan

Dokumen ini menjelaskan hubungan antarentitas dalam Sistem Informasi Laundry Koin. Setiap hubungan dilengkapi dengan penjelasan dua arah, kardinalitas, dan penempatan Foreign Key (FK).

### 2. Tabel Relasi Entitas

| No. | Entitas A - Relasi - Entitas B | Penjelasan Hubungan Dua Arah | Kardinalitas |
|---|---|---|---|
| 1 | Peran - memiliki - Pengguna | Satu peran dapat dimiliki oleh nol atau banyak pengguna. Satu pengguna memiliki tepat satu peran. | 1 : N |
| 2 | Pelanggan - melakukan - Transaksi | Satu pelanggan dapat melakukan nol atau banyak transaksi. Satu transaksi dilakukan oleh tepat satu pelanggan. | 1 : N |
| 3 | Layanan - digunakan dalam - Transaksi | Satu layanan dapat digunakan dalam nol atau banyak transaksi. Satu transaksi menggunakan tepat satu layanan. | 1 : N |

### 3. Penempatan Foreign Key (FK)

| No. | Relasi | Foreign Key (FK) | Tabel yang Memiliki FK |
|---|---|---|---|
| 1 | Peran - Pengguna | id_peran | Pengguna |
| 2 | Pelanggan - Transaksi | id_pelanggan | Transaksi |
| 3 | Layanan - Transaksi | id_layanan | Transaksi |

### 4. Penjelasan Relasi

1. **Peran dengan Pengguna**

   Hubungan Peran dan Pengguna memiliki kardinalitas satu-ke-banyak (1:N). Satu peran dapat digunakan oleh beberapa pengguna atau belum digunakan sama sekali. Sementara itu, setiap pengguna harus memiliki tepat satu peran. Foreign Key id_peran ditempatkan pada tabel Pengguna.

2. **Pelanggan dengan Transaksi**

   Hubungan Pelanggan dan Transaksi memiliki kardinalitas satu-ke-banyak (1:N). Satu pelanggan dapat melakukan beberapa transaksi atau belum memiliki transaksi. Sementara itu, setiap transaksi harus tercatat atas tepat satu pelanggan. Foreign Key id_pelanggan ditempatkan pada tabel Transaksi.

3. **Layanan dengan Transaksi**

   Hubungan Layanan dan Transaksi memiliki kardinalitas satu-ke-banyak (1:N). Satu layanan dapat digunakan dalam beberapa transaksi atau belum digunakan sama sekali. Sementara itu, setiap transaksi harus menggunakan tepat satu layanan. Foreign Key id_layanan ditempatkan pada tabel Transaksi.

### 5. Catatan Perancangan

1. Seluruh relasi yang telah diidentifikasi menggunakan kardinalitas satu-ke-banyak (1:N).
2. Foreign Key ditempatkan pada tabel yang berada di sisi banyak.
3. Belum ditemukan relasi banyak-ke-banyak (M:N), sehingga belum diperlukan tabel penghubung.
4. Entitas Mesin belum dihubungkan dengan entitas lain karena kebutuhan saat ini hanya mencakup penyimpanan informasi dan pengelolaan status mesin.
5. Relasi dapat diperbarui apabila terdapat perubahan atau penambahan kebutuhan sistem.

### 6. Sumber

1. Software Requirements Specification (SRS) Sistem Informasi Laundry Koin.
2. Dokumen Daftar Use Case Sistem Informasi Laundry Koin.
3. Dokumen Daftar Entitas Sistem Informasi Laundry Koin.
4. Dokumen ERD Sistem Informasi Laundry Koin.
