# DAFTAR HALAMAN

## Sistem Informasi Laundry Koin

### 1. Pendahuluan

Daftar halaman ini disusun berdasarkan Use Case pada dokumen `docs/uml/daftar-use-case.md` dan Kamus Data Awal pada dokumen `docs/desain/kamus-data-awal.md`.

Daftar halaman digunakan sebagai dasar untuk merancang struktur navigasi dan wireframe antarmuka Sistem Informasi Laundry Koin.

### 2. Daftar Halaman

| No. | Nama Halaman | Use Case Terkait | Aktor | Data yang Ditampilkan |
|---|---|---|---|---|
| 1 | Login | UC-01 Login pengguna | Pemilik, Admin/Operator | Username/email dan password |
| 2 | Dashboard | UC-02 Mengakses fitur sesuai hak akses, UC-03 Melihat dashboard | Pemilik | Ringkasan informasi transaksi, layanan, pendapatan, dan status mesin |
| 3 | Daftar Transaksi | UC-04 Melihat daftar transaksi, UC-09 Mengelola transaksi | Pemilik, Admin/Operator | ID transaksi, pelanggan, layanan, tanggal, total biaya |
| 4 | Form Transaksi | UC-09 Mengelola transaksi | Admin/Operator | Data pelanggan, layanan, tanggal, dan total biaya |
| 5 | Detail Transaksi | UC-04 Melihat rincian transaksi, UC-09 Mengelola transaksi | Pemilik, Admin/Operator | ID transaksi, pelanggan, layanan, tanggal, total biaya |
| 6 | Layanan dan Harga | UC-06 Mengelola layanan dan harga, UC-08 Melihat informasi layanan dan harga | Pemilik, Pelanggan* | ID layanan, nama layanan, harga |
| 7 | Data Pelanggan | UC-07 Mengelola data pelanggan | Admin/Operator | ID pelanggan dan data identitas pelanggan |
| 8 | Laporan Pendapatan | UC-05 Melihat laporan pendapatan berdasarkan periode | Pemilik | Periode laporan, data transaksi, dan total pendapatan |
| 9 | Status Mesin | UC-10 Memperbarui status mesin | Admin/Operator | ID mesin, informasi mesin, status mesin |

### 3. Hubungan Halaman dengan Hak Akses

1. Pemilik dapat mengakses dashboard, daftar dan detail transaksi, laporan pendapatan, serta pengelolaan layanan dan harga.
2. Admin/Operator dapat mengakses daftar transaksi, form transaksi, detail transaksi, dan pengelolaan data pelanggan.
3. Admin/Operator juga dapat memperbarui status mesin.
4. Halaman login digunakan oleh Pemilik dan Admin/Operator sebelum mengakses sistem.
5. Hak akses diterapkan pada menu dan tindakan sesuai peran masing-masing pengguna.

### 4. Catatan Perancangan

1. UC-02 merupakan pengaturan hak akses yang diterapkan pada navigasi dan halaman sistem, bukan halaman terpisah.
2. Form transaksi digunakan untuk mencatat transaksi baru maupun memperbarui transaksi sesuai hak akses.
3. Halaman Layanan dan Harga dirancang untuk menampilkan informasi layanan. Akses langsung oleh pelanggan masih perlu dikonfirmasi.
4. Tanda bintang (*) menunjukkan bahwa akses pelanggan pada UC-08 masih belum dikonfirmasi.
5. Fitur berprioritas Could Have tidak dimasukkan sebagai kebutuhan halaman wajib pada rancangan awal.

### 5. Kesimpulan

Rancangan awal menghasilkan sembilan halaman utama yang mencakup kebutuhan Use Case dengan prioritas Must dan Should. Daftar ini menjadi acuan untuk menyusun peta navigasi dan wireframe antarmuka.
