# DAFTAR USE CASE



## Sistem Informasi Laundry Koin



### 1. Identifikasi Use Case



Use Case merupakan gambaran fungsi atau layanan yang disediakan sistem untuk memenuhi kebutuhan aktor.



Identifikasi Use Case dilakukan berdasarkan kebutuhan fungsional (KF) pada dokumen SRS. Setiap kebutuhan fungsional dengan prioritas Must dan Should harus tercakup dalam daftar Use Case.



### 2. Tabel Use Case



| ID | Nama Use Case | Aktor | KF Terkait | Prioritas |

|---|---|---|---|---|

| UC-01 | Login pengguna | Pemilik, Admin/Operator | KF-01 | Must |

| UC-02 | Mengakses fitur sesuai hak akses | Pemilik | KF-02 | Must |

| UC-03 | Melihat dashboard | Pemilik | KF-03 | Should |

| UC-04 | Melihat daftar dan rincian transaksi | Pemilik, Admin/Operator | KF-04, KF-15 | Should |

| UC-05 | Melihat laporan pendapatan berdasarkan periode | Pemilik | KF-05, KF-06 | Should |

| UC-06 | Mengelola layanan dan harga | Pemilik | KF-07 | Must |

| UC-07 | Mengelola data pelanggan | Admin/Operator | KF-08 | Must |

| UC-08 | Melihat informasi layanan dan harga | Pelanggan* | KF-09 | Should |

| UC-09 | Mengelola transaksi | Admin/Operator | KF-10, KF-11, KF-12 | Must dan Should |

| UC-10 | Memperbarui status mesin | Admin/Operator | KF-14 | Should |



### 3. Catatan Pengelompokan



1. KF-04 dan KF-15 dikelompokkan karena keduanya berkaitan dengan informasi transaksi.

2. KF-05 dan KF-06 dikelompokkan karena filter periode digunakan untuk melihat laporan pendapatan.

3. KF-10, KF-11, dan KF-12 dikelompokkan dalam pengelolaan transaksi yang meliputi pencatatan, perubahan, dan pencarian riwayat transaksi.

4. Prioritas pada setiap Use Case mengikuti prioritas kebutuhan fungsional pada SRS.

5. Akses langsung Pelanggan masih perlu dikonfirmasi kepada pihak laundry.



### 4. Use Case yang Tidak Dimasukkan



Kebutuhan fungsional dengan prioritas Could belum dimasukkan ke dalam tabel Use Case wajib, yaitu:



- KF-13: Pencatatan penggunaan mesin.

- KF-16: Informasi kondisi mesin untuk teknisi.

- KF-17: Pencatatan perawatan dan perbaikan mesin.



Kebutuhan tersebut dapat dipertimbangkan kembali apabila ruang lingkup pengembangan memungkinkan.



### 5. Kesimpulan



Berdasarkan identifikasi kebutuhan fungsional, terdapat 10 Use Case yang mencakup seluruh kebutuhan dengan prioritas Must dan Should. Setiap Use Case memiliki aktor, nama fungsi, dan keterkaitan dengan kebutuhan fungsional pada dokumen SRS.




