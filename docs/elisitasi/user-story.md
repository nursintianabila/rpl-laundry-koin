# USER STORY
## Sistem Informasi Laundry Koin

### A. Deskripsi User Story

User story merupakan gambaran kebutuhan sistem berdasarkan sudut pandang pengguna. User story disusun untuk menjelaskan fitur yang dibutuhkan oleh setiap pengguna serta tujuan dari penggunaan fitur tersebut.

Format user story yang digunakan:

**Sebagai [jenis pengguna], saya ingin [kebutuhan atau fitur], sehingga [manfaat yang diperoleh].**

Catatan: User story berikut merupakan rancangan awal kebutuhan sistem dan masih perlu dikonfirmasi kepada pemilik atau pengelola laundry melalui proses wawancara.

---

### B. Identifikasi Pengguna Sistem

| No. | Jenis Pengguna | Deskripsi |
|---|---|---|
| 1 | Pemilik Laundry | Bertanggung jawab mengelola usaha dan memantau laporan operasional serta pendapatan. |
| 2 | Admin/Operator | Bertanggung jawab mengelola data pelanggan, layanan, transaksi, dan penggunaan mesin. |
| 3 | Pelanggan | Pengguna yang memanfaatkan layanan laundry dan membutuhkan informasi transaksi. |
| 4 | Teknisi | Pihak yang membantu menangani kerusakan dan perawatan mesin apabila diperlukan. |

---

### C. Daftar User Story

#### 1. Pemilik Laundry

| ID | User Story | Prioritas |
|---|---|---|
| US-01 | Sebagai pemilik laundry, saya ingin melakukan login agar dapat mengakses sistem sesuai hak akses saya. | Tinggi |
| US-02 | Sebagai pemilik laundry, saya ingin melihat dashboard agar dapat mengetahui ringkasan informasi usaha. | Tinggi |
| US-03 | Sebagai pemilik laundry, saya ingin melihat data transaksi agar dapat memantau aktivitas laundry. | Tinggi |
| US-04 | Sebagai pemilik laundry, saya ingin melihat laporan pendapatan agar dapat mengetahui hasil usaha. | Tinggi |
| US-05 | Sebagai pemilik laundry, saya ingin melihat laporan transaksi berdasarkan periode tertentu agar dapat mengevaluasi aktivitas usaha. | Tinggi |
| US-06 | Sebagai pemilik laundry, saya ingin mengelola data layanan dan harga agar informasi layanan tetap sesuai dengan ketentuan usaha. | Sedang |
| US-07 | Sebagai pemilik laundry, saya ingin mengelola akun pengguna agar dapat mengatur akses admin/operator. | Sedang |

#### 2. Admin/Operator

| ID | User Story | Prioritas |
|---|---|---|
| US-08 | Sebagai admin/operator, saya ingin melakukan login agar dapat masuk ke dalam sistem. | Tinggi |
| US-09 | Sebagai admin/operator, saya ingin mengelola data pelanggan agar informasi pelanggan tersimpan dengan baik. | Tinggi |
| US-10 | Sebagai admin/operator, saya ingin melihat daftar layanan dan harga agar dapat memberikan informasi kepada pelanggan. | Tinggi |
| US-11 | Sebagai admin/operator, saya ingin mencatat transaksi laundry agar setiap transaksi dapat tersimpan dalam sistem. | Tinggi |
| US-12 | Sebagai admin/operator, saya ingin mengubah data transaksi apabila terjadi kesalahan pencatatan sesuai hak akses yang diberikan. | Sedang |
| US-13 | Sebagai admin/operator, saya ingin melihat riwayat transaksi agar dapat mencari informasi transaksi sebelumnya. | Tinggi |
| US-14 | Sebagai admin/operator, saya ingin mencatat penggunaan mesin agar aktivitas penggunaan mesin dapat dipantau. | Sedang |
| US-15 | Sebagai admin/operator, saya ingin memperbarui status mesin agar informasi kondisi dan ketersediaan mesin dapat diketahui. | Sedang |

#### 3. Pelanggan

| ID | User Story | Prioritas |
|---|---|---|
| US-16 | Sebagai pelanggan, saya ingin mengetahui jenis layanan laundry agar dapat memilih layanan yang sesuai dengan kebutuhan. | Sedang |
| US-17 | Sebagai pelanggan, saya ingin mengetahui harga layanan agar dapat memperkirakan biaya yang harus dibayar. | Sedang |
| US-18 | Sebagai pelanggan, saya ingin memperoleh informasi transaksi agar dapat mengetahui rincian layanan yang digunakan. | Sedang |

#### 4. Teknisi

| ID | User Story | Prioritas |
|---|---|---|
| US-19 | Sebagai teknisi, saya ingin melihat informasi kondisi mesin agar dapat mengetahui mesin yang membutuhkan pemeriksaan. | Rendah |
| US-20 | Sebagai teknisi, saya ingin mencatat hasil perawatan atau perbaikan mesin agar riwayat pemeliharaan dapat terdokumentasi. | Rendah |

---

### D. Acceptance Criteria (Kriteria Penerimaan)

Acceptance criteria merupakan kriteria yang digunakan untuk menentukan apakah suatu fitur telah berjalan sesuai dengan kebutuhan pengguna.

| ID User Story | Kriteria Penerimaan |
|---|---|
| US-01 | Pengguna dapat memasukkan username dan password yang benar untuk masuk ke sistem. |
| US-02 | Dashboard menampilkan ringkasan informasi usaha sesuai data yang tersedia. |
| US-03 | Sistem menampilkan daftar transaksi yang telah tercatat. |
| US-04 | Sistem dapat menampilkan ringkasan pendapatan berdasarkan data transaksi. |
| US-05 | Pengguna dapat memilih periode laporan dan melihat hasilnya. |
| US-06 | Pemilik dapat menambah, mengubah, dan menghapus data layanan serta harga. |
| US-07 | Pemilik dapat mengelola akun pengguna sesuai hak aksesnya. |
| US-08 | Admin/operator dapat masuk ke sistem menggunakan akun yang terdaftar. |
| US-09 | Admin/operator dapat menambah, melihat, mengubah, dan menghapus data pelanggan sesuai hak akses. |
| US-10 | Sistem menampilkan daftar layanan beserta harga yang berlaku. |
| US-11 | Data transaksi dapat disimpan dan ditampilkan kembali. |
| US-12 | Perubahan transaksi tersimpan dan dapat ditampilkan sesuai hak akses. |
| US-13 | Sistem menyediakan daftar riwayat transaksi yang dapat dicari. |
| US-14 | Sistem dapat menyimpan informasi penggunaan mesin. |
| US-15 | Status mesin dapat diperbarui dan ditampilkan dalam sistem. |
| US-16 | Pelanggan dapat memperoleh informasi jenis layanan laundry. |
| US-17 | Pelanggan dapat mengetahui harga dari setiap layanan. |
| US-18 | Rincian transaksi dapat ditampilkan sebagai informasi bagi pelanggan. |
| US-19 | Teknisi dapat melihat informasi kondisi mesin yang tercatat. |
| US-20 | Hasil perawatan atau perbaikan mesin dapat disimpan dalam sistem. |

---

### E. Pengelompokan Fitur Berdasarkan Prioritas

Berdasarkan daftar user story di atas, kebutuhan sistem dikelompokkan menjadi tiga prioritas:

**1. Prioritas Tinggi**

Fitur yang dianggap penting untuk mendukung proses utama sistem, meliputi:
- Login pengguna.
- Dashboard.
- Pengelolaan data transaksi.
- Pengelolaan data pelanggan.
- Informasi layanan dan harga.
- Riwayat transaksi.
- Laporan pendapatan.
- Laporan transaksi.

**2. Prioritas Sedang**

Fitur yang mendukung pengelolaan dan pemantauan operasional, meliputi:
- Pengelolaan layanan dan harga oleh pemilik.
- Pengelolaan akun pengguna.
- Perubahan data transaksi.
- Pencatatan penggunaan mesin.
- Pembaruan status mesin.
- Informasi layanan dan harga untuk pelanggan.
- Informasi rincian transaksi pelanggan.

**3. Prioritas Rendah**

Fitur tambahan yang dapat dikembangkan sesuai kebutuhan, meliputi:
- Pemantauan kondisi mesin oleh teknisi.
- Pencatatan perawatan dan perbaikan mesin.

---

### F. Catatan Validasi User Story

Daftar user story ini disusun sebagai rancangan awal berdasarkan gambaran umum proyek Sistem Informasi Laundry Koin.
Validasi terhadap kebutuhan pengguna perlu dilakukan melalui wawancara dan observasi kepada pemilik atau pengelola laundry. Perubahan terhadap daftar user story dapat dilakukan apabila ditemukan kebutuhan baru atau terdapat fitur yang tidak sesuai dengan kondisi operasional sebenarnya.

| No. | Kegiatan Validasi | Status |
|---|---|---|
| 1 | Mengidentifikasi jenis pengguna sistem | Belum divalidasi |
| 2 | Mengidentifikasi kebutuhan setiap pengguna | Belum divalidasi |
| 3 | Menentukan fitur utama sistem | Belum divalidasi |
| 4 | Memeriksa kriteria penerimaan fitur | Belum divalidasi |
| 5 | Mengonfirmasi kebutuhan kepada narasumber | Belum dilakukan |

### G. Evaluasi Penggunaan AI

AI digunakan sebagai alat bantu dalam menyusun rancangan awal user story, mengidentifikasi calon pengguna sistem, serta membuat kriteria penerimaan fitur.

Hasil yang diberikan AI kemudian perlu diperiksa dan disesuaikan dengan kebutuhan proyek. Keputusan akhir mengenai fitur yang akan dikembangkan tetap berdasarkan hasil wawancara, observasi, dan persetujuan pihak pengelola laundry.