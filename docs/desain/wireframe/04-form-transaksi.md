\# WIREFRAME 04 — FORM TRANSAKSI



\## Sistem Informasi Laundry Koin



\### 1. Tujuan Halaman



Halaman Form Transaksi digunakan oleh Admin/Operator untuk memasukkan data transaksi laundry baru ke dalam sistem.



\### 2. Sketsa Wireframe



```text

+----------------------------------------------------------+

| SISTEM INFORMASI LAUNDRY KOIN           Pengguna | Logout|

+----------------------------------------------------------+

| Dashboard | Transaksi | Data Pelanggan | Status Mesin     |

+----------------------------------------------------------+

|                                                          |

|  FORM TRANSAKSI BARU                                     |

|                                                          |

|  ID Transaksi:   \[ Otomatis oleh Sistem ]                |

|                                                          |

|  Pelanggan:      \[ Pilih Pelanggan             v ]       |

|                                                          |

|  Layanan:        \[ Pilih Layanan               v ]       |

|                                                          |

|  Tanggal:        \[ DD-MM-YYYY                  ]         |

|                                                          |

|  Total Biaya:    \[ Otomatis berdasarkan layanan ]        |

|                                                          |

|                                                          |

|  \[ Simpan Transaksi ]       \[ Batal ]                    |

|                                                          |

+----------------------------------------------------------+

```



\### 3. Komponen Halaman



| No. | Komponen | Fungsi |

|---|---|---|

| 1 | Header | Menampilkan identitas sistem dan pengguna |

| 2 | Navigasi | Menampilkan menu sesuai hak akses |

| 3 | ID Transaksi | Menampilkan identitas transaksi yang dibuat sistem |

| 4 | Pilihan Pelanggan | Memilih pelanggan yang melakukan transaksi |

| 5 | Pilihan Layanan | Memilih jenis layanan laundry |

| 6 | Tanggal | Menentukan tanggal transaksi |

| 7 | Total Biaya | Menampilkan biaya berdasarkan layanan yang dipilih |

| 8 | Tombol Simpan | Menyimpan transaksi baru |

| 9 | Tombol Batal | Membatalkan pengisian transaksi |



\### 4. Anotasi



1\. Form hanya dapat diakses oleh Admin/Operator sesuai hak akses.

2\. ID transaksi dibuat secara otomatis oleh sistem.

3\. Admin/Operator memilih pelanggan dari data pelanggan yang tersedia.

4\. Admin/Operator memilih layanan yang telah didaftarkan.

5\. Total biaya ditampilkan berdasarkan harga layanan yang dipilih.

6\. Data wajib diisi sebelum transaksi disimpan.

7\. Setelah berhasil disimpan, sistem menampilkan informasi bahwa transaksi berhasil dicatat.



\### 5. Prinsip Desain



\- Konsistensi: bentuk input dibuat seragam.

\- Efisiensi: pilihan pelanggan dan layanan menggunakan daftar pilihan.

\- Pencegahan kesalahan: data wajib diperiksa sebelum disimpan.

\- Umpan balik: sistem memberikan pemberitahuan setelah transaksi berhasil atau gagal.



\### 6. Catatan



Rancangan ini merupakan sketsa awal. Mekanisme perhitungan total biaya dan penentuan ID transaksi perlu disesuaikan dengan aturan bisnis yang telah ditetapkan.

