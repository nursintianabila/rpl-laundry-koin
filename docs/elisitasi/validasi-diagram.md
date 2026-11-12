

\# CATATAN VALIDASI DIAGRAM



\## Sistem Informasi Laundry Koin



\### 1. Informasi Validasi



| Keterangan | Isi |

|---|---|

| Jenis kegiatan | Simulasi validasi diagram |

| Narasumber | Klien fiktif (simulasi pembelajaran) |

| Dokumen yang diperiksa | Use Case Diagram dan Activity Diagram Transaksi |

| Tujuan | Memeriksa kesesuaian aktor, fungsi, dan urutan proses berdasarkan rancangan kebutuhan |

| Status | Belum divalidasi oleh klien nyata |



Catatan: Dokumen ini merupakan hasil simulasi pemeriksaan untuk keperluan latihan. Isinya tidak mewakili wawancara atau persetujuan dari pemilik laundry sebenarnya.



\### 2. Diagram yang Diperiksa



1\. Use Case Diagram Sistem Informasi Laundry Koin.

2\. Activity Diagram Pengelolaan Transaksi (UC-09).



\### 3. Penjelasan kepada Klien



\#### 3.1 Use Case Diagram



Penjelasan dengan bahasa awam:



Sistem dirancang untuk digunakan oleh beberapa jenis pengguna.



\- Pemilik dapat mengelola layanan dan harga serta melihat informasi usaha.

\- Admin/operator dapat mengelola data pelanggan dan transaksi laundry.

\- Pelanggan direncanakan dapat melihat informasi layanan, harga, dan rincian transaksi.

\- Teknisi direncanakan dapat melihat kondisi mesin dan mencatat perawatan.



Akses langsung pelanggan dan teknisi masih berupa rancangan dan belum dipastikan.



\#### 3.2 Activity Diagram Pengelolaan Transaksi



Penjelasan dengan bahasa awam:



1\. Admin/operator membuka fitur transaksi.

2\. Admin/operator memilih pelanggan dan layanan.

3\. Admin/operator memasukkan tanggal serta data transaksi yang diperlukan.

4\. Sistem menghitung total biaya berdasarkan data yang tersedia.

5\. Sistem memeriksa kelengkapan dan validitas data.

6\. Jika data valid, transaksi disimpan.

7\. Admin/operator dapat mengubah transaksi sesuai hak akses.

8\. Admin/operator dapat mencari transaksi melalui riwayat transaksi.



\### 4. Hasil Simulasi Pemeriksaan



| No. | Bagian yang Diperiksa | Hasil Pemeriksaan | Tindak Lanjut |

|---|---|---|---|

| 1 | Aktor Pemilik | Sudah sesuai dengan peran pengelolaan usaha dalam PRD. | Dipertahankan sebagai rancangan. |

| 2 | Aktor Admin/Operator | Sudah sesuai dengan peran pengelolaan pelanggan dan transaksi dalam PRD. | Dipertahankan sebagai rancangan. |

| 3 | Aktor Pelanggan | Akses langsung pelanggan belum dapat dipastikan. | Perlu konfirmasi kepada pemilik laundry. |

| 4 | Aktor Teknisi | Penggunaan sistem oleh teknisi belum dapat dipastikan. | Perlu konfirmasi kepada pemilik laundry. |

| 5 | Proses pencatatan transaksi | Urutan pemilihan pelanggan, layanan, pengisian data, validasi, dan penyimpanan telah digambarkan. | Dipertahankan sebagai rancangan awal. |

| 6 | Perubahan transaksi | Perubahan transaksi dibatasi berdasarkan hak akses pengguna. | Aturan perubahan perlu dikonfirmasi. |

| 7 | Pencarian riwayat transaksi | Alur pencarian sudah dicantumkan. | Kriteria pencarian perlu dikonfirmasi. |

| 8 | Penggunaan dan perawatan mesin | Belum termasuk dalam tiga proses Activity Diagram yang dipilih. | Tetap menjadi kebutuhan yang perlu ditinjau. |



\### 5. Daftar Hal yang Masih Perlu Dikonfirmasi



1\. Apakah pelanggan perlu memiliki akun dan mengakses sistem secara langsung?

2\. Apakah teknisi akan menggunakan sistem untuk melihat kondisi dan mencatat perawatan mesin?

3\. Data apa saja yang wajib dicatat ketika transaksi laundry dibuat?

4\. Apakah transaksi yang sudah disimpan boleh diubah, dan siapa yang berhak mengubahnya?

5\. Informasi apa yang digunakan untuk mencari riwayat transaksi?

6\. Bagaimana proses pembayaran dan pencatatan status pembayaran dilakukan?



\### 6. Kesimpulan



Berdasarkan simulasi pemeriksaan dokumen, Use Case Diagram dan Activity Diagram Pengelolaan Transaksi telah menggambarkan rancangan aktor, fungsi, dan urutan proses utama berdasarkan PRD dan SRS yang tersedia.



Belum ditemukan alasan untuk menambahkan kebutuhan fungsional baru hanya berdasarkan pemeriksaan dokumen ini. Namun, beberapa aturan operasional dan akses pengguna masih memerlukan konfirmasi.



Hasil simulasi ini belum dapat dianggap sebagai persetujuan klien. Validasi langsung kepada pemilik atau pengelola laundry tetap diperlukan sebelum kebutuhan sistem ditetapkan sebagai kebutuhan final.



