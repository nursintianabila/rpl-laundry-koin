# DAFTAR ENTITAS

## Sistem Informasi Laundry Koin

### 1. Identifikasi Entitas

Identifikasi entitas dilakukan berdasarkan kebutuhan fungsional pada dokumen SRS, daftar Use Case, dan skenario Use Case. Entitas merupakan objek yang datanya perlu disimpan dan dikelola oleh sistem.

### 2. Tabel Daftar Entitas

| No. | Entitas (Tabel) | Deskripsi | Sumber (KF/UC) |
|---|---|---|---|
| 1 | Pengguna | Menyimpan data akun pengguna yang dapat masuk ke sistem, seperti pemilik dan admin/operator. | KF-01, KF-02 / UC-01, UC-02 |
| 2 | Peran | Menyimpan informasi peran pengguna untuk mengatur hak akses terhadap fitur sistem. | KF-02 / UC-02 |
| 3 | Pelanggan | Menyimpan informasi pelanggan yang menggunakan layanan laundry. | KF-08 / UC-07 |
| 4 | Layanan | Menyimpan informasi jenis layanan laundry beserta harga yang ditetapkan pemilik. | KF-07, KF-09 / UC-06, UC-08 |
| 5 | Transaksi | Menyimpan catatan transaksi laundry, termasuk pelanggan, layanan, tanggal, dan total biaya. | KF-04, KF-10, KF-11, KF-12, KF-15 / UC-04, UC-09 |
| 6 | Mesin | Menyimpan informasi mesin laundry beserta status operasionalnya. | KF-14 / UC-10 |

### 3. Entitas yang Belum Dimasukkan

Beberapa kebutuhan fungsional belum dijadikan entitas karena masih berprioritas Could dan belum termasuk Use Case wajib, yaitu:

1. Penggunaan mesin (KF-13).
2. Perawatan dan perbaikan mesin (KF-17).

Entitas tersebut dapat ditambahkan apabila kebutuhan pengelolaan penggunaan dan perawatan mesin dimasukkan ke dalam ruang lingkup pengembangan.

### 4. Catatan

1. Entitas Pengguna dan Peran digunakan untuk mendukung proses login serta pengaturan hak akses.
2. Entitas Transaksi menjadi sumber data untuk riwayat transaksi dan laporan pendapatan.
3. Entitas Mesin digunakan untuk menyimpan dan memperbarui status mesin.
4. Rincian atribut setiap entitas akan dijelaskan lebih lanjut dalam dokumen kamus data.

### 5. Sumber

1. Product Requirements Document (PRD) Sistem Informasi Laundry Koin.
2. Software Requirements Specification (SRS) Sistem Informasi Laundry Koin.
3. Dokumen Daftar Use Case.
4. Dokumen Skenario Use Case.
