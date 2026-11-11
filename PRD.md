# PRODUCT REQUIREMENTS DOCUMENT (PRD)
## Sistem Informasi Laundry Koin

### 1. Ringkasan Produk dan Tujuan

Sistem Informasi Laundry Koin merupakan aplikasi berbasis web untuk membantu pengelolaan operasional usaha laundry. Sistem menyediakan pengelolaan pelanggan, layanan, transaksi, riwayat transaksi, informasi mesin, dan laporan usaha.

**Tujuan produk:**
- Mempermudah pencatatan dan pengelolaan transaksi laundry.
- Membantu pemilik memantau pendapatan dan aktivitas usaha.
- Menyediakan informasi operasional secara terstruktur.
- Membatasi akses berdasarkan peran pengguna.

### 2. Pengguna dan Peran

| Pengguna | Hal yang dapat dilakukan |
|---|---|
| Pemilik | Melihat dashboard, transaksi, dan laporan pendapatan serta mengelola layanan dan harga. |
| Admin/Operator | Mengelola pelanggan, melihat layanan, mencatat dan mengubah transaksi, melihat riwayat, serta memperbarui status mesin. |
| Pelanggan | Memperoleh informasi layanan, harga, dan rincian transaksi. |
| Teknisi | Melihat informasi kondisi mesin dan menangani perawatan mesin. |

Catatan: Akses langsung pelanggan dan teknisi masih menunggu konfirmasi pihak laundry.

### 3. Fitur Berdasarkan Prioritas

#### A. Must Have

**1. Login dan hak akses pengguna**
- Given pengguna memiliki akun yang terdaftar, When memasukkan username/email dan password yang benar, Then sistem mengizinkan pengguna masuk sesuai perannya.
- Given pengguna sudah login, When membuka menu yang tidak sesuai hak aksesnya, Then sistem menolak akses tersebut.

**2. Pengelolaan layanan dan harga**
- Given pemilik sudah login, When menambah, melihat, mengubah, atau menghapus layanan, Then sistem menyimpan perubahan data layanan dan harga.

**3. Pengelolaan data pelanggan**
- Given admin/operator sudah login, When menambah, melihat, mengubah, atau menghapus data pelanggan, Then sistem menampilkan data pelanggan sesuai perubahan.

**4. Pencatatan transaksi**
- Given admin/operator telah memilih pelanggan dan layanan, When menyimpan transaksi dengan data wajib yang valid, Then sistem menyimpan pelanggan, layanan, tanggal, dan total biaya transaksi.

**5. Riwayat transaksi**
- Given transaksi telah tersimpan, When pengguna melakukan pencarian berdasarkan informasi transaksi yang tersedia, Then sistem menampilkan transaksi yang sesuai.

#### B. Should Have

**6. Dashboard**
- Given pemilik sudah login, When membuka dashboard, Then sistem menampilkan ringkasan informasi usaha berdasarkan data tersimpan.

**7. Daftar transaksi**
- Given terdapat transaksi tersimpan, When pengguna membuka daftar transaksi, Then sistem menampilkan transaksi yang tersedia.

**8. Ringkasan pendapatan**
- Given terdapat transaksi yang tercatat, When pemilik membuka ringkasan pendapatan, Then sistem menghitung dan menampilkan pendapatan berdasarkan data transaksi.

**9. Filter periode laporan**
- Given pemilik membuka laporan, When memasukkan tanggal mulai dan tanggal akhir, Then sistem menampilkan laporan sesuai periode tersebut.

**10. Informasi layanan dan harga**
- Given data layanan telah tersedia, When pengguna yang membutuhkan informasi membuka daftar layanan, Then sistem menampilkan jenis layanan dan harga yang berlaku.

**11. Perubahan transaksi**
- Given transaksi telah tersimpan dan pengguna memiliki hak akses, When pengguna mengubah data transaksi yang diizinkan, Then sistem menyimpan perubahan tersebut.

**12. Pembaruan status mesin**
- Given data mesin telah tersedia, When admin/operator memperbarui status mesin, Then sistem menyimpan dan menampilkan status terbaru.

**13. Rincian transaksi**
- Given transaksi telah tersimpan, When pengguna membuka rincian transaksi, Then sistem menampilkan informasi transaksi yang dapat diberikan kepada pelanggan.

#### Persyaratan Kualitas Pendukung

- **Must:** Password disimpan dalam bentuk hash; data wajib divalidasi dan kesalahan formulir ditampilkan kepada pengguna.
- **Should:** Waktu respons halaman utama dan data umum ditargetkan maksimal 3 detik pada 95% pengujian dalam kondisi normal.
- **Should:** Sistem mendukung dua versi terbaru Google Chrome dan Microsoft Edge.
- **Should:** Tampilan menyesuaikan layar komputer dan ponsel tanpa menghilangkan fungsi utama.

### 4. Data Awal

| Entitas | Atribut penting |
|---|---|
| Pengguna | ID pengguna, username/email, password, peran |
| Peran | ID peran, nama peran |
| Pelanggan | ID pelanggan, data identitas pelanggan |
| Layanan | ID layanan, nama layanan, harga |
| Transaksi | ID transaksi, pelanggan, layanan, tanggal, total biaya |
| Mesin | ID mesin, informasi mesin, status mesin |

Catatan: Atribut ini merupakan rancangan awal. Rincian data pelanggan dan mesin masih perlu dikonfirmasi.

### 5. Di Luar Lingkup

**Could Have (belum menjadi prioritas pengerjaan):**
- Pencatatan penggunaan mesin.
- Informasi kondisi mesin khusus teknisi.
- Pencatatan perawatan dan perbaikan mesin.

**Won't Have (tidak dikerjakan dalam proyek ini):**
- Pengendalian mesin laundry otomatis melalui perangkat keras.
- Integrasi pembayaran otomatis melalui bank, e-wallet, atau payment gateway.
- Layanan antar-jemput pakaian.
- Aplikasi mobile Android atau iOS.

### 6. Pertanyaan Terbuka

1. Apakah pelanggan akan memiliki akun dan akses langsung ke sistem?
2. Apakah teknisi benar-benar membutuhkan akses ke sistem?
3. Apakah pencatatan penggunaan dan kondisi mesin diperlukan dalam kegiatan operasional?
4. Apakah pemilik membutuhkan laporan pendapatan harian, mingguan, bulanan, atau seluruhnya?
5. Apakah target waktu respons dan kompatibilitas browser sudah sesuai dengan perangkat yang tersedia?
