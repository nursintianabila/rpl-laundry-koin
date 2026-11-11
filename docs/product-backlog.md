# Product Backlog – Sistem Informasi Laundry Koin

## 1. Tujuan

Product Backlog berisi daftar kebutuhan dan pekerjaan pengembangan Sistem Informasi Laundry Koin berdasarkan Product Requirements Document (PRD).

Setiap kebutuhan menggunakan ID KF (Kebutuhan Fungsional) dan prioritas MoSCoW:

- **Must Have:** Fitur wajib tersedia.
- **Should Have:** Fitur penting yang dikerjakan setelah kebutuhan Must terpenuhi.
- **Could Have:** Fitur tambahan yang belum menjadi prioritas pengerjaan.
- **Won't Have:** Fitur yang tidak dikerjakan dalam proyek ini.

Proyek direncanakan berlangsung selama empat sprint dengan durasi masing-masing dua minggu. Pembagian pada dokumen ini berfokus pada Sprint 1–3 sesuai kebutuhan perencanaan.

## 2. Daftar Kebutuhan Berdasarkan PRD

| ID | Kebutuhan | Prioritas | Sumber |
|---|---|---|---|
| KF-01 | Login dan hak akses pengguna | Must Have | PRD bagian 3.A.1 |
| KF-02 | Pengelolaan layanan dan harga | Must Have | PRD bagian 3.A.2 |
| KF-03 | Pengelolaan data pelanggan | Must Have | PRD bagian 3.A.3 |
| KF-04 | Pencatatan transaksi | Must Have | PRD bagian 3.A.4 |
| KF-05 | Riwayat transaksi | Must Have | PRD bagian 3.A.5 |
| KF-06 | Dashboard | Should Have | PRD bagian 3.B.6 |
| KF-07 | Daftar transaksi | Should Have | PRD bagian 3.B.7 |
| KF-08 | Ringkasan pendapatan | Should Have | PRD bagian 3.B.8 |
| KF-09 | Filter periode laporan | Should Have | PRD bagian 3.B.9 |
| KF-10 | Informasi layanan dan harga | Should Have | PRD bagian 3.B.10 |
| KF-11 | Perubahan transaksi | Should Have | PRD bagian 3.B.11 |
| KF-12 | Pembaruan status mesin | Should Have | PRD bagian 3.B.12 |
| KF-13 | Rincian transaksi | Should Have | PRD bagian 3.B.13 |

### Persyaratan Kualitas Pendukung

| ID | Persyaratan | Prioritas |
|---|---|---|
| KQ-01 | Password harus disimpan dalam bentuk hash. | Must Have |
| KQ-02 | Data wajib harus divalidasi dan kesalahan formulir ditampilkan kepada pengguna. | Must Have |
| KQ-03 | Waktu respons halaman utama dan data umum ditargetkan maksimal 3 detik pada 95% pengujian dalam kondisi normal. | Should Have |
| KQ-04 | Sistem mendukung dua versi terbaru Google Chrome dan Microsoft Edge. | Should Have |
| KQ-05 | Tampilan menyesuaikan layar komputer dan ponsel tanpa menghilangkan fungsi utama. | Should Have |

## 3. Pembagian Kebutuhan ke Sprint

| Sprint | ID kebutuhan | Fitur | Alasan |
|---|---|---|---|
| Sprint 1 | KF-01 | Login dan hak akses pengguna | Menjadi dasar keamanan dan pembatasan akses sistem. |
| Sprint 1 | KF-02 | Pengelolaan layanan dan harga | Data layanan diperlukan sebagai dasar pencatatan transaksi. |
| Sprint 1 | KF-03 | Pengelolaan data pelanggan | Data pelanggan diperlukan sebelum transaksi dapat dicatat. |
| Sprint 2 | KF-04 | Pencatatan transaksi | Menjadi fungsi utama operasional laundry setelah data dasar tersedia. |
| Sprint 2 | KF-05 | Riwayat transaksi | Memungkinkan pengguna mencari transaksi yang sudah tersimpan. |
| Sprint 2 | KF-07 | Daftar transaksi | Memudahkan pengguna melihat transaksi yang tersedia. |
| Sprint 2 | KF-10 | Informasi layanan dan harga | Menyediakan informasi layanan dan harga yang sudah dikelola. |
| Sprint 2 | KF-13 | Rincian transaksi | Memudahkan penyajian informasi transaksi kepada pelanggan. |
| Sprint 3 | KF-06 | Dashboard | Menyediakan ringkasan informasi usaha berdasarkan data tersimpan. |
| Sprint 3 | KF-08 | Ringkasan pendapatan | Membantu pemilik memantau pendapatan dari transaksi. |
| Sprint 3 | KF-09 | Filter periode laporan | Memungkinkan pemilik melihat laporan berdasarkan rentang tanggal. |
| Sprint 3 | KF-11 | Perubahan transaksi | Mendukung perubahan data transaksi sesuai hak akses. |
| Sprint 3 | KF-12 | Pembaruan status mesin | Mendukung pencatatan dan pemantauan status mesin. |

## 4. Rincian Tugas Sprint 1

Setiap tugas dirancang agar dapat diselesaikan maksimal satu hari kerja. Pengerjaan dilakukan secara mandiri.

| ID kebutuhan | Tugas | Alasan |
|---|---|---|
| KF-01 | Menentukan kebutuhan data akun pengguna dan peran berdasarkan PRD. | Menyiapkan dasar pengelolaan akun dan hak akses. |
| KF-01 | Menyusun rancangan tampilan halaman login. | Menentukan tampilan awal untuk pengguna masuk ke sistem. |
| KF-01 | Menyiapkan struktur data pengguna dan peran. | Menyediakan tempat penyimpanan akun serta perannya. |
| KF-01 | Menyiapkan proses autentikasi pengguna. | Memastikan pengguna dapat masuk menggunakan akun terdaftar. |
| KF-01 | Menyiapkan pembatasan akses berdasarkan peran. | Mencegah pengguna membuka menu yang tidak sesuai hak akses. |
| KF-01 | Menguji proses login dan hak akses setiap peran. | Memastikan autentikasi dan pembatasan akses berjalan sesuai kebutuhan. |
| KF-02 | Menentukan struktur data layanan dan harga. | Menyiapkan penyimpanan informasi layanan. |
| KF-02 | Menyusun rancangan tampilan daftar layanan. | Memudahkan pemilik melihat layanan yang tersedia. |
| KF-02 | Menyusun rancangan formulir layanan. | Menyiapkan proses penambahan dan perubahan layanan. |
| KF-02 | Menyiapkan fungsi menambah dan melihat layanan. | Memenuhi kebutuhan pengelolaan layanan. |
| KF-02 | Menyiapkan fungsi mengubah layanan dan harga. | Memenuhi kebutuhan perubahan data layanan dan harga. |
| KF-02 | Menyiapkan fungsi menghapus layanan. | Memenuhi kebutuhan penghapusan layanan. |
| KF-02 | Menguji pengelolaan layanan dan harga. | Memastikan perubahan data layanan tersimpan dengan benar. |
| KF-03 | Menentukan struktur data pelanggan berdasarkan atribut yang telah disepakati. | Menyiapkan penyimpanan data pelanggan. |
| KF-03 | Menyusun rancangan tampilan daftar pelanggan. | Memudahkan admin/operator melihat data pelanggan. |
| KF-03 | Menyusun rancangan formulir pelanggan. | Menyiapkan proses penambahan dan perubahan data pelanggan. |
| KF-03 | Menyiapkan fungsi mengubah data pelanggan. | Memenuhi kebutuhan perubahan data pelanggan. |
| KF-03 | Menyiapkan fungsi menghapus data pelanggan. | Memenuhi kebutuhan penghapusan data pelanggan. |
| KF-03 | Menguji pengelolaan data pelanggan. | Memastikan data pelanggan dapat dikelola sesuai kebutuhan. |
| KQ-01 | Menyiapkan penyimpanan password dalam bentuk hash. | Menjaga keamanan password pengguna. |
| KQ-02 | Menentukan validasi data wajib pada formulir login, layanan, dan pelanggan. | Memastikan data yang dimasukkan sesuai ketentuan. |
| KQ-02 | Menguji validasi dan pesan kesalahan formulir. | Memastikan pengguna memperoleh informasi ketika terjadi kesalahan input. |

## 5. Catatan Pelaksanaan

1. Sprint 1 difokuskan pada kebutuhan Must Have berupa login, layanan, dan pelanggan.
2. Sprint 2 dan Sprint 3 dilaksanakan setelah fondasi kebutuhan sebelumnya tersedia.
3. Setiap tugas ditargetkan selesai maksimal satu hari kerja.
4. Pengembangan dilakukan berdasarkan kebutuhan yang tercantum dalam PRD.
5. Perubahan kebutuhan harus ditinjau terlebih dahulu dan disesuaikan dengan PRD.
6. Persyaratan kualitas KQ tetap diperhatikan selama pengembangan.
7. Pengerjaan dan pemeriksaan hasil dilakukan secara mandiri.

## 6. Kebutuhan yang Tidak Dimasukkan ke Backlog Sprint 1–3

Beberapa butir dari backlog awal tidak dimasukkan karena belum tercantum sebagai kebutuhan Must atau Should dalam PRD:

- Pencatatan laporan mesin rusak dan riwayat perbaikannya.
- Pencatatan jadwal perawatan mesin.
- Pencatatan keluhan atau permintaan pelanggan.
- Pencatatan stok koin.
- Pencatatan stok sabun dan pewangi.
- Pengelolaan data penjaga dan jadwal jaga.

Fitur pencatatan penggunaan mesin, informasi kondisi mesin khusus teknisi, serta pencatatan perawatan dan perbaikan mesin berada pada kategori Could Have dalam PRD dan belum menjadi prioritas pengerjaan.

Fitur pengendalian mesin otomatis, integrasi pembayaran otomatis, layanan antar-jemput, dan aplikasi mobile termasuk Won't Have sehingga tidak dimasukkan ke backlog pengerjaan proyek ini.

## 7. Catatan Konfirmasi

Beberapa kebutuhan masih perlu dikonfirmasi kepada pihak laundry, terutama akses langsung pelanggan dan teknisi, rincian data pelanggan dan mesin, serta bentuk laporan pendapatan yang dibutuhkan.

Product Backlog ini merupakan rencana awal berdasarkan PRD dan dapat diperbarui apabila hasil konfirmasi kebutuhan menghasilkan perubahan yang disepakati.