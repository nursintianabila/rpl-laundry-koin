\# SOFTWARE REQUIREMENTS SPECIFICATION (SRS)



\## Sistem Informasi Laundry Koin



\### 1. Pendahuluan



\#### 1.1 Tujuan



Dokumen Software Requirements Specification (SRS) ini menjelaskan kebutuhan fungsional dan nonfungsional Sistem Informasi Laundry Koin. Dokumen digunakan sebagai acuan dalam proses perancangan, pengembangan, dan pengujian sistem.



\#### 1.2 Ruang Lingkup



Sistem Informasi Laundry Koin merupakan aplikasi berbasis web yang dirancang untuk membantu pengelolaan operasional laundry, meliputi:



\- Pengelolaan data pengguna.

\- Pengelolaan data pelanggan.

\- Pengelolaan layanan dan harga.

\- Pencatatan transaksi laundry.

\- Pengelolaan riwayat transaksi.

\- Pencatatan penggunaan dan status mesin.

\- Penyajian laporan pendapatan dan transaksi.



\#### 1.3 Definisi dan Singkatan



| Istilah | Keterangan |

|---|---|

| SRS | Software Requirements Specification |

| KF | Kebutuhan Fungsional |

| KNF | Kebutuhan Nonfungsional |

| US | User Story |

| MoSCoW | Metode penentuan prioritas kebutuhan |

| Admin/Operator | Pengguna yang mengelola operasional laundry |

| Pemilik | Pengguna yang mengelola dan memantau usaha |

| Teknisi | Pengguna yang menangani kondisi dan perawatan mesin |



\### 2. Gambaran Umum Sistem



\#### 2.1 Perspektif Produk



Sistem dikembangkan sebagai aplikasi berbasis web untuk membantu pengelolaan kegiatan operasional laundry. Sistem diharapkan dapat digunakan oleh pemilik, admin/operator, dan teknisi sesuai hak akses masing-masing.



\#### 2.2 Jenis Pengguna



| Pengguna | Hak dan Tanggung Jawab |

|---|---|

| Pemilik Laundry | Memantau informasi usaha, laporan, layanan, harga, dan akun pengguna |

| Admin/Operator | Mengelola pelanggan, layanan, transaksi, dan penggunaan mesin |

| Pelanggan | Memperoleh informasi layanan, harga, dan rincian transaksi |

| Teknisi | Melihat kondisi mesin serta mencatat perawatan atau perbaikan |



Catatan: Bentuk akses pelanggan dan teknisi masih berupa rancangan awal dan perlu dikonfirmasi.



\#### 2.3 Batasan Sistem



Sistem dirancang dengan batasan berikut:



\- Sistem berbentuk aplikasi berbasis web.

\- Pengembangan disesuaikan dengan waktu pengerjaan proyek.

\- Pengendalian mesin secara otomatis melalui perangkat keras tidak termasuk dalam ruang lingkup.

\- Integrasi pembayaran otomatis melalui bank, e-wallet, atau payment gateway tidak termasuk dalam ruang lingkup.

\- Layanan antar-jemput pakaian tidak termasuk dalam ruang lingkup.

\- Aplikasi mobile Android atau iOS tidak termasuk dalam ruang lingkup.



\### 3. Kebutuhan Fungsional (KF)



Kebutuhan fungsional menjelaskan fungsi yang harus disediakan oleh sistem.



| ID | Kebutuhan Fungsional | Sumber | Prioritas |

|---|---|---|---|

| KF-01 | Sistem harus menyediakan halaman login yang menerima username/email dan password. Pengguna dengan data login yang valid dapat masuk ke sistem. | US-01, US-08 | Must |

| KF-02 | Sistem harus membatasi akses menu dan tindakan berdasarkan peran pengguna yang telah ditentukan. | US-01, US-07, US-08 | Must |

| KF-03 | Sistem harus menampilkan dashboard berisi ringkasan informasi usaha berdasarkan data yang tersimpan. | US-02 | Should |

| KF-04 | Sistem harus menampilkan daftar transaksi yang telah tersimpan. | US-03 | Should |

| KF-05 | Sistem harus menghitung dan menampilkan ringkasan pendapatan berdasarkan data transaksi yang tercatat. | US-04 | Should |

| KF-06 | Sistem harus menyediakan filter periode laporan berdasarkan tanggal mulai dan tanggal akhir. | US-05 | Should |

| KF-07 | Pemilik harus dapat menambah, melihat, mengubah, dan menghapus data layanan serta harga. | US-06 | Must |

| KF-08 | Admin/operator harus dapat menambah, melihat, mengubah, dan menghapus data pelanggan. | US-09 | Must |

| KF-09 | Sistem harus menampilkan informasi jenis layanan dan harga yang berlaku kepada pengguna yang membutuhkan informasi tersebut. | US-10, US-16, US-17 | Should |

| KF-10 | Admin/operator harus dapat mencatat transaksi laundry dengan menyimpan data pelanggan, layanan, tanggal, dan total biaya sesuai data yang tersedia. | US-11 | Must |

| KF-11 | Sistem harus menyediakan fungsi perubahan data transaksi yang telah tersimpan sesuai hak akses pengguna. | US-12 | Should |

| KF-12 | Sistem harus menyediakan riwayat transaksi yang dapat dicari berdasarkan informasi transaksi yang tersedia. | US-13 | Must |

| KF-13 | Admin/operator harus dapat mencatat informasi penggunaan mesin laundry. | US-14 | Could |

| KF-14 | Sistem harus menyediakan fungsi untuk memperbarui dan menampilkan status mesin laundry. | US-15 | Should |

| KF-15 | Sistem harus dapat menampilkan rincian transaksi agar informasi transaksi dapat diberikan kepada pelanggan. | US-18 | Should |

| KF-16 | Sistem harus menampilkan informasi kondisi mesin yang tercatat agar dapat diperiksa oleh teknisi. | US-19 | Could |

| KF-17 | Sistem harus menyediakan pencatatan hasil perawatan atau perbaikan mesin. | US-20 | Could |



\### 4. Kebutuhan Nonfungsional (KNF)



Kebutuhan nonfungsional menjelaskan kualitas dan batasan teknis sistem. Seluruh target angka pada bagian ini merupakan asumsi awal yang masih perlu disesuaikan dengan kemampuan perangkat dan kebutuhan pengguna.



| ID | Kebutuhan Nonfungsional | Sumber | Prioritas |

|---|---|---|---|

| KNF-01 | Password pengguna harus disimpan dalam bentuk hash dan tidak disimpan sebagai teks biasa. | Asumsi | Must |

| KNF-02 | Sistem ditargetkan menampilkan hasil permintaan halaman utama dan data umum dalam waktu maksimal 3 detik pada 95% pengujian dengan kondisi jaringan dan perangkat normal. | Asumsi | Should |

| KNF-03 | Sistem harus dapat diakses melalui dua versi terbaru browser Google Chrome dan Microsoft Edge. | Asumsi | Should |

| KNF-04 | Sistem harus menampilkan pesan kesalahan ketika pengguna mengirim formulir dengan data wajib yang kosong atau tidak sesuai format, serta tidak menyimpan data yang tidak valid. | Asumsi | Must |

| KNF-05 | Sistem harus menampilkan menu dan tindakan sesuai hak akses pengguna yang sedang login. | Asumsi | Must |

| KNF-06 | Tampilan sistem harus dapat menyesuaikan ukuran layar komputer dan ponsel tanpa menghilangkan fungsi utama halaman. | Asumsi | Should |



\### 5. Prioritas Kebutuhan dengan MoSCoW



Prioritas kebutuhan ditetapkan untuk membantu menentukan fitur yang dikerjakan terlebih dahulu.



\#### 5.1 Must Have



Kebutuhan yang wajib tersedia agar fungsi utama sistem dapat berjalan:



\- KF-01: Login pengguna.

\- KF-02: Pembatasan hak akses.

\- KF-07: Pengelolaan layanan dan harga.

\- KF-08: Pengelolaan data pelanggan.

\- KF-10: Pencatatan transaksi.

\- KF-12: Riwayat transaksi.

\- KNF-01: Keamanan penyimpanan password.

\- KNF-04: Validasi data.

\- KNF-05: Pembatasan hak akses.



\#### 5.2 Should Have



Kebutuhan penting yang sebaiknya tersedia setelah fungsi utama:



\- KF-03: Dashboard.

\- KF-04: Daftar transaksi.

\- KF-05: Ringkasan pendapatan.

\- KF-06: Filter periode laporan.

\- KF-09: Informasi layanan dan harga.

\- KF-11: Perubahan transaksi.

\- KF-14: Pembaruan status mesin.

\- KF-15: Rincian transaksi.

\- KNF-02: Target waktu respons.

\- KNF-03: Kompatibilitas browser.

\- KNF-06: Tampilan responsif.



\#### 5.3 Could Have



Kebutuhan tambahan yang dapat dikerjakan apabila waktu memungkinkan:



\- KF-13: Pencatatan penggunaan mesin.

\- KF-16: Informasi kondisi mesin untuk teknisi.

\- KF-17: Pencatatan perawatan dan perbaikan mesin.



\#### 5.4 Won't Have



Fitur yang tidak dikerjakan dalam ruang lingkup proyek saat ini:



\- Pengendalian mesin laundry secara otomatis melalui perangkat keras.

\- Integrasi pembayaran otomatis melalui bank, e-wallet, atau payment gateway.

\- Layanan antar-jemput pakaian.

\- Aplikasi mobile Android atau iOS.



\### 6. Matriks Keterlacakan Kebutuhan (Traceability Matrix)



Matriks ini menghubungkan setiap user story dengan kebutuhan fungsional, use case, dan kebutuhan nonfungsional yang diturunkan. Sumber US merupakan rancangan awal yang belum divalidasi melalui wawancara nyata. KNF yang bersumber dari asumsi ditandai secara terpisah.



| User Story | Kebutuhan Fungsional | Use Case | Kebutuhan Nonfungsional | Uji |
|---|---|---|---|---|
| US-01 | KF-01, KF-02 | UC-01, UC-02 | KNF-01, KNF-05 | TC-F01, TC-F02, TC-F03 |
| US-02 | KF-03 | UC-03 | KNF-02, KNF-06 | Belum disusun |
| US-03 | KF-04 | UC-04 | KNF-02, KNF-05 | Belum disusun |
| US-04 | KF-05 | UC-05 | KNF-02, KNF-04 | Belum disusun |
| US-05 | KF-06 | UC-05 | KNF-04, KNF-06 | Belum disusun |
| US-06 | KF-07 | UC-06 | KNF-04, KNF-05 | TC-F04, TC-F05, TC-F06, TC-F07 |
| US-07 | KF-02 | UC-02 | KNF-01, KNF-05 | TC-F03 |
| US-08 | KF-01, KF-02 | UC-01, UC-02 | KNF-01, KNF-05 | TC-F01, TC-F02, TC-F03 |
| US-09 | KF-08 | UC-07 | KNF-04, KNF-05 | TC-F08, TC-F09, TC-F10, TC-F11 |
| US-10 | KF-09 | UC-08 | KNF-03, KNF-06 | Belum disusun |
| US-11 | KF-10 | UC-09 | KNF-02, KNF-04, KNF-05 | TC-F12, TC-F13 |
| US-12 | KF-11 | UC-09 | KNF-04, KNF-05 | Belum disusun |
| US-13 | KF-12 | UC-09 | KNF-02, KNF-04 | TC-F14, TC-F15 |
| US-14 | KF-13 | Belum dimodelkan | KNF-04, KNF-05 | — (di luar cakupan) |
| US-15 | KF-14 | UC-10 | KNF-04, KNF-05 | Belum disusun |
| US-16 | KF-09 | UC-08 | KNF-03, KNF-06 | Belum disusun |
| US-17 | KF-09 | UC-08 | KNF-03, KNF-06 | Belum disusun |
| US-18 | KF-15 | UC-04 | KNF-03, KNF-06 | Belum disusun |
| US-19 | KF-16 | Belum dimodelkan | KNF-05 | — (di luar cakupan) |
| US-20 | KF-17 | Belum dimodelkan | KNF-04, KNF-05 | — (di luar cakupan) |



\#### 6.1 Pemeriksaan Keterlacakan



\- Seluruh 20 user story US-01 sampai US-20 telah memiliki kebutuhan fungsional turunan.

\- Setiap kebutuhan fungsional KF-01 sampai KF-17 memiliki sumber user story.

\- Kebutuhan KF-01, KF-02, KF-04 sampai KF-12, KF-14, dan KF-15 telah memiliki pemetaan ke use case.

\- KF-13, KF-16, dan KF-17 belum dimodelkan dalam daftar use case karena belum dimasukkan ke dalam proses utama yang dipilih.

\- Setiap kebutuhan nonfungsional KNF-01 sampai KNF-06 diberi sumber Asumsi karena belum berasal dari hasil konfirmasi narasumber.

\- Kebutuhan dan prioritas masih dapat berubah setelah dilakukan validasi kepada pemilik atau pengelola laundry.



\### 7. Pemodelan Sistem



Pemodelan sistem dilakukan menggunakan Use Case Diagram, skenario Use Case, dan Activity Diagram untuk menggambarkan interaksi aktor serta alur proses utama Sistem Informasi Laundry Koin.



\#### 7.1 Use Case Diagram dan Skenario



Dokumen pemodelan Use Case dapat dilihat pada berkas berikut:



\- \[Daftar Aktor](uml/daftar-aktor.md)

\- \[Daftar Use Case](uml/daftar-use-case.md)

\- \[Skenario Use Case](uml/skenario-use-case.md)

\- \[Use Case Diagram - Mermaid](uml/use-case.mmd)

\- \[Use Case Diagram - SVG](uml/use-case.svg)



\#### 7.2 Activity Diagram



Activity Diagram dibuat untuk tiga proses utama, yaitu login pengguna, pengelolaan layanan dan harga, serta pengelolaan transaksi.



\*\*Dokumen pemilihan dan verifikasi:\*\*



\- \[Pemilihan Proses Activity Diagram](uml/pemilihan-proses-activity.md)

\- \[Verifikasi Draf Activity Diagram AI](uml/verifikasi-draf-ai.md)



\*\*Diagram Login Pengguna:\*\*



\- \[Activity Diagram Login - PNG](uml/activity/activity-01-login.png)

\- \[Activity Diagram Login - Mermaid](uml/activity/activity-01-login.mmd)



\*\*Diagram Pengelolaan Layanan dan Harga:\*\*



\- \[Activity Diagram Layanan dan Harga - PNG](uml/activity/activity-02-layanan.png)

\- \[Activity Diagram Layanan dan Harga - Mermaid](uml/activity/activity-02-layanan.mmd)



\*\*Diagram Pengelolaan Transaksi:\*\*



\- \[Activity Diagram Transaksi - PNG](uml/activity/activity-03-transaksi.png)

\- \[Activity Diagram Transaksi - Mermaid](uml/activity/activity-03-transaksi.mmd)



\#### 7.3 Hasil Pemodelan



Pemodelan telah menggambarkan tiga proses utama yang dipilih berdasarkan skenario use case, yaitu login pengguna, pengelolaan layanan dan harga, serta pengelolaan transaksi.



Hasil pemodelan menunjukkan bahwa kebutuhan fungsional pada proses-proses tersebut telah memiliki gambaran alur aktivitas dan keputusan. KF-13, KF-16, dan KF-17 belum memiliki use case tersendiri dalam pemodelan saat ini karena belum termasuk dalam proses yang dipilih.



Kebutuhan tersebut tetap tercatat dalam SRS dan dapat dipertimbangkan pada pengembangan berikutnya setelah dilakukan konfirmasi kepada pihak pengelola laundry.



\### 8. Asumsi dan Hal yang Perlu Dikonfirmasi



Hal-hal berikut masih perlu dikonfirmasi sebelum kebutuhan dianggap final:



1\. Apakah pelanggan akan memiliki akses langsung ke sistem atau hanya menerima informasi dari admin/operator?

2\. Apakah teknisi benar-benar akan menggunakan sistem?

3\. Apakah pencatatan penggunaan dan kondisi mesin diperlukan dalam operasional sehari-hari?

4\. Apakah pemilik membutuhkan laporan pendapatan harian, mingguan, bulanan, atau seluruhnya?

5\. Apakah target waktu respons, kompatibilitas browser, dan tampilan responsif sudah sesuai dengan perangkat yang tersedia?



\#### 8.1 Riwayat Konfirmasi dan Validasi Diagram



Pada 12 November 2026 dilakukan simulasi pemeriksaan Use Case Diagram dan Activity Diagram Pengelolaan Transaksi untuk memeriksa kesesuaian aktor, fungsi, dan urutan proses berdasarkan PRD dan SRS.



Hasil simulasi menunjukkan bahwa rancangan proses utama telah tergambarkan. Namun, akses langsung pelanggan dan teknisi, detail pencatatan transaksi, aturan perubahan transaksi, serta kriteria pencarian riwayat masih perlu dikonfirmasi.



Simulasi ini bukan hasil wawancara atau persetujuan klien nyata. Validasi langsung kepada pemilik atau pengelola laundry masih diperlukan.



Dokumen hasil simulasi: \[Catatan Validasi Diagram](elisitasi/validasi-diagram.md).




### 8.2 Daftar Pertanyaan Konfirmasi Aturan Data

Bagian ini berisi daftar pertanyaan untuk memastikan aturan pengelolaan data sesuai dengan kebutuhan pemilik atau pengelola Laundry Koin. Pertanyaan disusun menggunakan bahasa sederhana agar mudah dipahami oleh klien.

| No. | Pertanyaan Konfirmasi | Jawaban Klien | Status |
|---|---|---|---|
| 1 | Apakah harga layanan laundry boleh diubah sewaktu-waktu oleh pemilik? | Belum diisi | Belum dikonfirmasi |
| 2 | Jika harga layanan berubah, apakah biaya transaksi lama harus tetap menggunakan harga saat transaksi dilakukan? | Belum diisi | Belum dikonfirmasi |
| 3 | Apakah data pelanggan yang sudah tersimpan boleh diubah atau dihapus? | Belum diisi | Belum dikonfirmasi |
| 4 | Apakah transaksi yang sudah dicatat boleh diedit atau dibatalkan jika terjadi kesalahan? | Belum diisi | Belum dikonfirmasi |
| 5 | Jika transaksi dibatalkan, apakah catatan transaksi tersebut tetap perlu disimpan sebagai riwayat? | Belum diisi | Belum dikonfirmasi |
| 6 | Berapa lama data pelanggan dan riwayat transaksi perlu disimpan dalam sistem? | Belum diisi | Belum dikonfirmasi |
| 7 | Siapa saja yang boleh menambah, mengubah, dan menghapus data pelanggan, layanan, serta transaksi? | Belum diisi | Belum dikonfirmasi |
| 8 | Apakah pemilik perlu mengelola informasi dan status mesin, misalnya tersedia, digunakan, atau rusak? | Belum diisi | Belum dikonfirmasi |

**Catatan Konfirmasi:**

Daftar pertanyaan ini disiapkan sebagai bahan konfirmasi kepada pemilik atau pengelola Laundry Koin. Jawaban klien belum diperoleh sehingga belum digunakan untuk mengubah aturan atau batasan pada kamus data. Perubahan kebutuhan akan dicatat setelah konfirmasi benar-benar dilakukan.


\### 9. Evaluasi Penggunaan AI



AI digunakan sebagai alat bantu dalam menyusun kerangka SRS, merumuskan kebutuhan fungsional dan nonfungsional, menentukan prioritas MoSCoW, serta menyusun matriks keterlacakan berdasarkan dokumen user story yang tersedia.



Hasil yang diberikan AI diperiksa kembali dengan membandingkannya terhadap dokumen elisitasi dan ruang lingkup proyek. Kebutuhan yang belum didukung hasil wawancara ditandai sebagai asumsi dan tidak dinyatakan sebagai fakta. Keputusan akhir mengenai kebutuhan sistem tetap menjadi tanggung jawab pengembang dan perlu divalidasi kepada pihak pengelola laundry.

