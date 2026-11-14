# WIREFRAME 08 — LAPORAN PENDAPATAN

## Sistem Informasi Laundry Koin

### 1. Tujuan Halaman

Halaman Laporan Pendapatan digunakan oleh Pemilik untuk melihat ringkasan pendapatan berdasarkan periode tertentu sebagai bahan pemantauan dan evaluasi usaha.

### 2. Sketsa Wireframe

```text
+----------------------------------------------------------+
| SISTEM INFORMASI LAUNDRY KOIN           Pengguna | Logout|
+----------------------------------------------------------+
| Dashboard | Transaksi | Layanan | Laporan                 |
+----------------------------------------------------------+
|                                                          |
|  LAPORAN PENDAPATAN                                      |
|                                                          |
|  Periode:                                                |
|  Dari Tanggal: [ DD-MM-YYYY ]                            |
|  Sampai:       [ DD-MM-YYYY ]                            |
|                                                          |
|  [ Tampilkan Laporan ]                                   |
|                                                          |
|  +----------------------------------------------------+  |
|  | Jumlah Transaksi       : 00                        |  |
|  | Total Pendapatan       : Rp 0.000.000              |  |
|  +----------------------------------------------------+  |
|                                                          |
|  RINCIAN PENDAPATAN                                      |
|  +----------------------------------------------------+  |
|  | Tanggal | Jumlah Transaksi | Total Pendapatan     |  |
|  +----------------------------------------------------+  |
|  |         |                  |                      |  |
|  |         |                  |                      |  |
|  +----------------------------------------------------+  |
|                                                          |
|  PESAN: [Berhasil / Terjadi kesalahan]                   |
|                                                          |
+----------------------------------------------------------+
```

### 3. Komponen Halaman

| No. | Komponen | Fungsi |
|---|---|---|
| 1 | Header | Menampilkan identitas sistem dan pengguna |
| 2 | Navigasi | Menampilkan menu sesuai hak akses |
| 3 | Judul Halaman | Menunjukkan halaman Laporan Pendapatan |
| 4 | Tanggal Awal | Menentukan awal periode laporan |
| 5 | Tanggal Akhir | Menentukan akhir periode laporan |
| 6 | Tombol Tampilkan Laporan | Menampilkan laporan sesuai periode |
| 7 | Ringkasan Transaksi | Menampilkan jumlah transaksi dalam periode |
| 8 | Total Pendapatan | Menampilkan total pendapatan dalam periode |
| 9 | Rincian Pendapatan | Menampilkan rincian pendapatan berdasarkan tanggal |
| 10 | Pesan Sistem | Menampilkan informasi keberhasilan atau kesalahan saat laporan diproses |

### 4. Anotasi

1. Halaman hanya dapat diakses oleh Pemilik.
2. Pemilik menentukan tanggal awal dan tanggal akhir laporan.
3. Sistem menampilkan data berdasarkan periode yang dipilih.
4. Ringkasan menampilkan jumlah transaksi dan total pendapatan.
5. Rincian pendapatan membantu Pemilik melihat hasil usaha berdasarkan tanggal.
6. Sistem perlu memastikan tanggal awal tidak melebihi tanggal akhir.
7. Sistem menampilkan pesan apabila laporan berhasil ditampilkan atau terjadi kesalahan saat pemrosesan.

### 5. Prinsip Desain

- Keterbacaan: ringkasan pendapatan ditampilkan secara jelas.
- Efisiensi: pemilihan periode memudahkan pencarian laporan.
- Konsistensi: format tanggal dan mata uang dibuat seragam.
- Pencegahan kesalahan: sistem memvalidasi rentang tanggal sebelum menampilkan laporan.

### 6. Catatan

Nilai pada sketsa hanya contoh. Perhitungan pendapatan harus mengikuti aturan bisnis dan data transaksi yang telah ditetapkan.