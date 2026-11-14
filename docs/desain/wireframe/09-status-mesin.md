# WIREFRAME 09 — STATUS MESIN

## Sistem Informasi Laundry Koin

### 1. Tujuan Halaman

Halaman Status Mesin digunakan oleh Admin/Operator untuk melihat informasi mesin laundry dan memperbarui status mesin sesuai kondisi yang tersedia.

### 2. Sketsa Wireframe

```text id="m8q3ks"
+----------------------------------------------------------+
| SISTEM INFORMASI LAUNDRY KOIN           Pengguna | Logout|
+----------------------------------------------------------+
| Dashboard | Transaksi | Data Pelanggan | Status Mesin     |
+----------------------------------------------------------+
|                                                          |
|  STATUS MESIN                                            |
|                                                          |
|  +----------------------------------------------------+  |
|  | ID Mesin | Nama Mesin | Status       | Aksi         |  |
|  +----------------------------------------------------+  |
|  | 01       | Mesin A    | Tersedia     | [Ubah]       |  |
|  | 02       | Mesin B    | Digunakan    | [Ubah]       |  |
|  | 03       | Mesin C    | Perawatan    | [Ubah]       |  |
|  +----------------------------------------------------+  |
|                                                          |
|  Keterangan Status:                                      |
|  - Tersedia                                              |
|  - Digunakan                                             |
|  - Perawatan                                             |
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
| 3 | Judul Halaman | Menunjukkan halaman Status Mesin |
| 4 | Tabel Mesin | Menampilkan daftar mesin laundry |
| 5 | ID Mesin | Menampilkan identitas mesin |
| 6 | Nama Mesin | Menampilkan nama atau informasi mesin |
| 7 | Status Mesin | Menampilkan kondisi mesin saat ini |
| 8 | Tombol Ubah | Membuka pilihan untuk memperbarui status mesin |
| 9 | Keterangan Status | Menjelaskan arti setiap status mesin |
| 10 | Pesan Sistem | Menampilkan pemberitahuan setelah perubahan status berhasil atau gagal |

### 4. Anotasi

1. Halaman menampilkan daftar mesin yang terdaftar dalam sistem.
2. Admin/Operator dapat melihat status setiap mesin.
3. Admin/Operator dapat memperbarui status mesin sesuai kondisi sebenarnya.
4. Perubahan status perlu disimpan agar informasi yang ditampilkan selalu diperbarui.
5. Sistem memberikan pemberitahuan setelah perubahan status berhasil atau gagal.

### 5. Prinsip Desain

- Keterbacaan: informasi mesin ditampilkan dalam tabel.
- Konsistensi: format tabel mengikuti halaman lainnya.
- Efisiensi: status mesin dapat dilihat tanpa membuka halaman terpisah.
- Umpan balik: sistem memberikan pemberitahuan setelah status diperbarui.

### 6. Catatan

Nama mesin dan status pada sketsa merupakan contoh. Daftar status sebenarnya perlu disesuaikan dengan kondisi operasional dan aturan yang berlaku pada usaha laundry.