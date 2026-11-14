# WIREFRAME 02 — DASHBOARD

## Sistem Informasi Laundry Koin

### 1. Tujuan Halaman

Halaman Dashboard merupakan halaman utama Pemilik setelah berhasil login. Halaman ini menampilkan ringkasan informasi operasional laundry agar Pemilik dapat memantau kondisi usaha.

### 2. Sketsa Wireframe

```text
+------------------------------------------------------+
| SISTEM INFORMASI LAUNDRY KOIN       Pemilik | Logout |
+------------------------------------------------------+
| Dashboard | Transaksi | Layanan | Laporan            |
+------------------------------------------------------+
|                                                      |
|  DASHBOARD                                           |
|  Selamat datang, Pemilik                             |
|                                                      |
|  +----------------+  +----------------+              |
|  | Total Transaksi|  | Total Pendapatan|             |
|  |                |  |                |              |
|  +----------------+  +----------------+              |
|                                                      |
|  +----------------+  +----------------+              |
|  | Jumlah Layanan |  | Status Mesin   |              |
|  |                |  |                |              |
|  +----------------+  +----------------+              |
|                                                      |
|  RINGKASAN TRANSAKSI TERBARU                          |
|  +-----------------------------------------------+   |
|  | ID | Pelanggan | Layanan | Tanggal | Total    |   |
|  +-----------------------------------------------+   |
|  |    |          |         |         |          |   |
|  |    |          |         |         |          |   |
|  +-----------------------------------------------+   |
|                                                      |
|  PESAN: [Berhasil / Terjadi kesalahan]               |
|                                                      |
+------------------------------------------------------+
```

### 3. Komponen Halaman

| No. | Komponen | Fungsi |
|---|---|---|
| 1 | Header | Menampilkan nama sistem dan informasi pengguna |
| 2 | Navigasi | Menampilkan menu yang dapat diakses Pemilik |
| 3 | Kartu Total Transaksi | Menampilkan ringkasan jumlah transaksi |
| 4 | Kartu Total Pendapatan | Menampilkan ringkasan pendapatan |
| 5 | Kartu Jumlah Layanan | Menampilkan jumlah layanan yang tersedia |
| 6 | Kartu Status Mesin | Menampilkan ringkasan kondisi mesin |
| 7 | Tabel Transaksi Terbaru | Menampilkan beberapa transaksi terbaru |
| 8 | Pesan Sistem | Menampilkan informasi berhasil atau kesalahan saat sistem memproses permintaan |

### 4. Anotasi

1. Dashboard hanya dapat diakses oleh Pemilik sesuai rancangan hak akses.
2. Informasi ringkasan ditampilkan dalam bentuk kartu agar mudah dibaca.
3. Tabel transaksi terbaru membantu Pemilik melihat aktivitas transaksi.
4. Informasi ditampilkan berdasarkan data yang tersimpan dalam sistem.
5. Menu navigasi memudahkan Pemilik berpindah ke halaman lain.
6. Pesan sistem digunakan untuk memberikan informasi keberhasilan atau kesalahan kepada pengguna.

### 5. Prinsip Desain

- Hierarki visual: informasi penting seperti pendapatan dan transaksi ditempatkan di bagian atas.
- Konsistensi: header dan navigasi mengikuti pola tampilan yang sama.
- Keterbacaan: informasi disusun dalam kartu dan tabel.
- Efisiensi: ringkasan utama dapat dilihat tanpa membuka banyak halaman.

### 6. Catatan

Nilai total transaksi, pendapatan, jumlah layanan, dan status mesin merupakan informasi ringkasan yang dihitung atau diambil dari data sistem. Rincian perhitungannya masih perlu disesuaikan dengan kebutuhan final.