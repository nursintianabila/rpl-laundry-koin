# NORMALISASI DATABASE

## Sistem Informasi Laundry Koin

### 1. Pendahuluan

Normalisasi merupakan proses penyusunan struktur tabel database untuk mengurangi pengulangan data dan menghindari masalah dalam penambahan, perubahan, maupun penghapusan data.

Proses normalisasi pada Sistem Informasi Laundry Koin dilakukan secara bertahap mulai dari bentuk tidak normal (UNF), First Normal Form (1NF), Second Normal Form (2NF), hingga Third Normal Form (3NF).

**Catatan:** Data yang digunakan dalam dokumen ini merupakan data simulasi yang dibuat berdasarkan kebutuhan Sistem Informasi Laundry Koin, bukan dokumen transaksi asli dari klien.

### 2. Data Mentah (UNF)

Data mentah berikut menggambarkan contoh pencatatan transaksi laundry yang masih menggabungkan informasi pelanggan, layanan, dan transaksi dalam satu tabel.

| ID Transaksi | Tanggal | ID Pelanggan | Nama Pelanggan | ID Layanan | Nama Layanan | Harga | Berat (kg) | Total Biaya |
|---|---|---|---|---|---|---:|---:|---:|
| TRX001 | 10-11-2026 | P001 | Andi Saputra | L001 | Cuci Kering | 7000 | 3 | 21000 |
| TRX002 | 10-11-2026 | P002 | Siti Aminah | L002 | Cuci Setrika | 9000 | 2 | 18000 |
| TRX003 | 11-11-2026 | P001 | Andi Saputra | L001 | Cuci Kering | 7000 | 4 | 28000 |
| TRX004 | 11-11-2026 | P003 | Budi Santoso | L002 | Cuci Setrika | 9000 | 3 | 27000 |

Pada bentuk awal ini, informasi pelanggan dan layanan dicatat kembali setiap kali transaksi dilakukan.

**Permasalahan pada UNF:**
1. Data pelanggan berulang ketika pelanggan melakukan transaksi lebih dari satu kali.
2. Nama dan harga layanan dicatat berulang pada setiap transaksi.
3. Perubahan informasi pelanggan atau layanan harus diperbarui pada beberapa baris.

### 3. First Normal Form (1NF)

Pada tahap 1NF, setiap kolom harus memiliki nilai yang bersifat tunggal (atomic), tidak mengandung kelompok data berulang, dan setiap baris harus dapat dibedakan.

Berdasarkan data simulasi, setiap transaksi memiliki satu pelanggan dan satu layanan. Oleh karena itu, data dapat disusun dalam bentuk tabel dengan setiap atribut berisi satu nilai.

**Tabel Transaksi_1NF**

| ID Transaksi (PK) | Tanggal | ID Pelanggan | Nama Pelanggan | ID Layanan | Nama Layanan | Harga | Berat (kg) | Total Biaya |
|---|---|---|---|---|---|---:|---:|---:|
| TRX001 | 10-11-2026 | P001 | Andi Saputra | L001 | Cuci Kering | 7000 | 3 | 21000 |
| TRX002 | 10-11-2026 | P002 | Siti Aminah | L002 | Cuci Setrika | 9000 | 2 | 18000 |
| TRX003 | 11-11-2026 | P001 | Andi Saputra | L001 | Cuci Kering | 7000 | 4 | 28000 |
| TRX004 | 11-11-2026 | P003 | Budi Santoso | L002 | Cuci Setrika | 9000 | 3 | 27000 |

**Perbaikan pada 1NF:**
1. Setiap atribut sudah memiliki nilai tunggal.
2. Tidak terdapat kolom yang menyimpan beberapa nilai sekaligus.
3. Setiap transaksi memiliki identitas unik melalui ID Transaksi.

Dengan demikian, tabel telah memenuhi bentuk normal pertama (1NF).

### 4. Second Normal Form (2NF)

Pada tabel Transaksi_1NF, ID Transaksi digunakan sebagai satu-satunya Primary Key. Karena kunci utama hanya terdiri dari satu atribut, tidak terdapat ketergantungan parsial. Dengan demikian, tabel tersebut telah memenuhi bentuk normal kedua (2NF).

**Perbaikan pada 2NF:**
1. Tidak ditemukan ketergantungan parsial karena Primary Key hanya menggunakan satu atribut, yaitu ID Transaksi.
2. Meskipun sudah memenuhi 2NF, masih terdapat ketergantungan transitif. Nama Pelanggan bergantung pada ID Pelanggan, sedangkan Nama Layanan dan Harga bergantung pada ID Layanan.
3. Ketergantungan transitif tersebut akan diperbaiki pada tahap 3NF dengan memisahkan data pelanggan dan layanan ke dalam tabel masing-masing.

Oleh karena itu, struktur tabel pada tahap 2NF masih sama dengan tahap 1NF.

### 5. Third Normal Form (3NF)

Pada tahap 3NF, tabel harus memenuhi 2NF dan tidak memiliki ketergantungan transitif. Artinya, atribut nonkunci harus bergantung langsung pada Primary Key.

Pada tabel sebelumnya, terdapat informasi pelanggan dan layanan yang sebaiknya disimpan pada tabel masing-masing.

Contohnya:
- Nama pelanggan bergantung pada ID Pelanggan.
- Nama layanan dan harga bergantung pada ID Layanan.
- Informasi transaksi bergantung pada ID Transaksi.

Untuk menghindari pengulangan data, tabel kemudian dipisahkan menjadi tiga tabel berikut.

**A. Tabel Pelanggan**

| ID Pelanggan (PK) | Nama Pelanggan |
|---|---|
| P001 | Andi Saputra |
| P002 | Siti Aminah |
| P003 | Budi Santoso |

**B. Tabel Layanan**

| ID Layanan (PK) | Nama Layanan | Harga |
|---|---|---:|
| L001 | Cuci Kering | 7000 |
| L002 | Cuci Setrika | 9000 |

**C. Tabel Transaksi**

| ID Transaksi (PK) | Tanggal | ID Pelanggan (FK) | ID Layanan (FK) | Berat (kg) | Total Biaya |
|---|---|---|---|---:|---:|
| TRX001 | 10-11-2026 | P001 | L001 | 3 | 21000 |
| TRX002 | 10-11-2026 | P002 | L002 | 2 | 18000 |
| TRX003 | 11-11-2026 | P001 | L001 | 4 | 28000 |
| TRX004 | 11-11-2026 | P003 | L002 | 3 | 27000 |

**Perbaikan pada 3NF:**
1. Data pelanggan dipisahkan ke tabel Pelanggan agar nama pelanggan tidak perlu dicatat berulang kali.
2. Data layanan dipisahkan ke tabel Layanan agar nama dan harga layanan dikelola pada satu tempat.
3. Tabel Transaksi menyimpan ID Pelanggan dan ID Layanan sebagai Foreign Key untuk menghubungkan data.
4. Total Biaya tetap disimpan sebagai nilai transaksi saat transaksi dilakukan agar riwayat biaya tidak berubah ketika harga layanan diperbarui.

Dengan pemisahan tersebut, struktur data telah memenuhi bentuk normal ketiga (3NF).

### 6. Hasil Akhir Normalisasi

Berdasarkan proses normalisasi, diperoleh tiga tabel utama dari data transaksi simulasi:

1. Pelanggan
2. Layanan
3. Transaksi

Selain ketiga tabel tersebut, terdapat tabel Pengguna, Peran, dan Mesin yang ditambahkan berdasarkan kebutuhan fungsional pada dokumen SRS, bukan berasal langsung dari contoh nota transaksi.

Dengan demikian, rancangan akhir database terdiri dari enam tabel:

| No. | Nama Tabel | Keterangan |
|---|---|---|
| 1 | Pengguna | Menyimpan data akun pengguna sistem. |
| 2 | Peran | Menyimpan informasi peran dan hak akses pengguna. |
| 3 | Pelanggan | Menyimpan informasi pelanggan laundry. |
| 4 | Layanan | Menyimpan jenis layanan dan harga laundry. |
| 5 | Transaksi | Menyimpan catatan transaksi laundry. |
| 6 | Mesin | Menyimpan informasi dan status mesin laundry. |

### 7. Kesimpulan

Berdasarkan tahapan normalisasi mulai dari UNF, 1NF, 2NF, hingga 3NF, struktur database Sistem Informasi Laundry Koin telah disusun agar mengurangi pengulangan data dan menjaga konsistensi informasi.

Hasil akhir normalisasi menghasilkan tabel Pelanggan, Layanan, dan Transaksi dari contoh data transaksi. Tabel Pengguna, Peran, dan Mesin ditambahkan berdasarkan kebutuhan sistem. Keenam tabel tersebut disesuaikan dengan entitas yang terdapat pada ERD.

### 8. Sumber

1. Data transaksi laundry simulasi yang disusun berdasarkan kebutuhan Sistem Informasi Laundry Koin.
2. Software Requirements Specification (SRS) Sistem Informasi Laundry Koin.
3. Dokumen Daftar Entitas dan Atribut Entitas.
4. Dokumen ERD Sistem Informasi Laundry Koin.