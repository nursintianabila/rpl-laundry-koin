# RENCANA PENGUJIAN
## Sistem Informasi Laundry Koin

### 1. Tujuan Pengujian

Pengujian dilakukan untuk memastikan Sistem Informasi Laundry Koin berjalan sesuai kebutuhan yang telah ditetapkan dalam PRD. Pengujian bertujuan untuk:

1. Memastikan fitur utama sistem berjalan sesuai kebutuhan pengguna.
2. Memastikan hak akses pengguna diterapkan dengan benar.
3. Memastikan data yang dimasukkan dapat divalidasi dan disimpan dengan benar.
4. Memastikan sistem menampilkan informasi transaksi dan pendapatan sesuai data tersimpan.
5. Menemukan kesalahan sistem sebelum diterapkan kepada pengguna.
6. Memastikan sistem dapat digunakan dan diterima oleh pihak laundry.

### 2. Ruang Lingkup Pengujian

Ruang lingkup pengujian mencakup kebutuhan fungsional berdasarkan prioritas dalam PRD.

#### A. Fitur Must Have

Fitur berikut wajib diuji dan harus lulus:

1. **Login dan hak akses pengguna:** Menguji proses login menggunakan akun yang benar dan penolakan akses menu yang tidak sesuai dengan peran pengguna.
2. **Pengelolaan layanan dan harga:** Menguji proses menambah, melihat, mengubah, dan menghapus layanan beserta harganya.
3. **Pengelolaan data pelanggan:** Menguji proses menambah, melihat, mengubah, dan menghapus data pelanggan.
4. **Pencatatan transaksi:** Menguji penyimpanan transaksi dengan data pelanggan, layanan, tanggal, dan total biaya yang valid.
5. **Riwayat transaksi:** Menguji pencarian transaksi berdasarkan informasi transaksi yang tersedia.

Persyaratan kualitas Must Have yang turut diuji:
- Password disimpan dalam bentuk hash, bukan teks biasa.
- Data wajib divalidasi.
- Kesalahan pengisian formulir ditampilkan kepada pengguna.

#### B. Fitur Should Have

Fitur berikut diuji setelah fitur Must Have:

1. **Dashboard:** Menguji tampilan ringkasan informasi usaha berdasarkan data tersimpan.
2. **Daftar transaksi:** Menguji tampilan daftar transaksi yang telah tersimpan.
3. **Ringkasan pendapatan:** Menguji perhitungan dan tampilan pendapatan berdasarkan transaksi.
4. **Filter periode laporan:** Menguji penyaringan laporan berdasarkan tanggal mulai dan tanggal akhir.
5. **Informasi layanan dan harga:** Menguji tampilan jenis layanan dan harga yang berlaku.
6. **Perubahan transaksi:** Menguji perubahan data transaksi sesuai hak akses pengguna.
7. **Pembaruan status mesin:** Menguji penyimpanan dan tampilan status mesin terbaru.
8. **Rincian transaksi:** Menguji tampilan informasi lengkap dari transaksi yang dipilih.

Persyaratan kualitas Should Have yang turut diperiksa:
- Waktu respons halaman utama dan data umum ditargetkan maksimal 3 detik pada 95% pengujian dalam kondisi normal.
- Sistem diuji pada dua versi terbaru Google Chrome dan Microsoft Edge.
- Tampilan diuji pada layar komputer dan ponsel.

### 3. Strategi Pengujian

Strategi pengujian yang digunakan terdiri dari:

#### A. Pengujian Black-Box Manual

Pengujian dilakukan dengan mencoba fitur sistem berdasarkan masukan dan keluaran tanpa memeriksa kode program.

Pengujian meliputi:
- Memasukkan data yang valid dan tidak valid.
- Menguji proses login dan hak akses.
- Menguji proses tambah, lihat, ubah, dan hapus data.
- Menguji pencatatan dan pencarian transaksi.
- Memeriksa kesesuaian hasil yang ditampilkan dengan hasil yang diharapkan.

#### B. Pengujian Otomatis Dasar

Pengujian otomatis dilakukan terhadap logika inti sistem menggunakan data uji.

Bagian yang diuji meliputi:
- Validasi data wajib.
- Perhitungan total biaya transaksi.
- Perhitungan ringkasan pendapatan.
- Validasi masukan tanggal pada filter laporan.
- Pemeriksaan logika hak akses pengguna.

Hasil pengujian otomatis dibandingkan dengan hasil yang diharapkan untuk memastikan logika sistem berjalan dengan benar.

#### C. User Acceptance Testing (UAT)

UAT dilakukan bersama klien atau perwakilan pihak laundry untuk mengetahui apakah sistem telah sesuai dengan kebutuhan operasional.

Pengujian meliputi:
- Mencoba login sesuai peran pengguna.
- Melakukan pencatatan transaksi.
- Melihat daftar dan rincian transaksi.
- Melihat informasi layanan dan harga.
- Memeriksa laporan dan ringkasan pendapatan.
- Memberikan penilaian serta masukan terhadap kemudahan penggunaan sistem.

### 4. Lingkungan Pengujian

Pengujian direncanakan menggunakan lingkungan berikut:

#### A. Perangkat dan Perangkat Lunak

- Laptop atau komputer untuk pengembangan dan pengujian.
- Ponsel untuk pemeriksaan tampilan responsif.
- Sistem operasi Windows.
- Browser Google Chrome dan Microsoft Edge.
- Visual Studio Code sebagai editor kode.
- Lingkungan lokal pengembangan sistem.
- Perangkat lunak pengujian otomatis dasar sesuai teknologi yang digunakan.

#### B. Data Pengujian

Pengujian menggunakan data karangan atau data dummy, bukan data pribadi pelanggan sebenarnya.

Contoh data yang digunakan:
- Akun pengguna: Pemilik dan Admin/Operator.
- Data pelanggan: Pelanggan A dan Pelanggan B.
- Data layanan: Cuci Reguler dan Cuci Express.
- Data transaksi: Transaksi dengan variasi layanan, tanggal, dan total biaya.
- Data mesin: Mesin 1 dan Mesin 2 dengan status berbeda.

Data dummy digunakan untuk menguji proses penyimpanan, perubahan, pencarian, perhitungan, dan penampilan informasi.

### 5. Kriteria Lulus Pengujian

Sistem dinyatakan memenuhi kriteria pengujian apabila:

1. Seluruh test case untuk fitur Must Have berhasil lulus.
2. Proses login dan pembatasan hak akses berjalan sesuai peran pengguna.
3. Data wajib divalidasi dan kesalahan formulir ditampilkan dengan benar.
4. Password tersimpan dalam bentuk hash.
5. Proses pencatatan transaksi menghasilkan data dan total biaya yang sesuai.
6. Fitur Should Have diuji dan hasilnya dicatat, termasuk jika masih ditemukan kekurangan.
7. Pengujian otomatis terhadap logika inti menghasilkan keluaran sesuai harapan.
8. Hasil UAT memperoleh tanggapan dan persetujuan dari klien atau perwakilannya sebelum sistem dinyatakan siap digunakan.

Setiap test case harus memiliki hasil aktual dan status pengujian, yaitu Lulus atau Gagal. Test case yang gagal harus dicatat untuk diperbaiki dan diuji ulang.

### 6. Pembagian Tugas Pengujian

Pembagian tugas pengujian direncanakan sebagai berikut:

| Penguji | Tanggung Jawab |
|---|---|
| Mahasiswa/Pengembang | Menyiapkan rencana pengujian, melakukan pengujian black-box, membuat dan menjalankan pengujian otomatis dasar, serta mencatat hasil pengujian. |
| Anggota Kelompok/Reviewer | Membantu memeriksa skenario pengujian, mengulang pengujian fitur, dan memeriksa hasil pengujian. |
| Klien/Perwakilan Laundry | Melakukan UAT, mencoba alur penggunaan sistem, serta memberikan masukan dan penilaian terhadap kesesuaian sistem dengan kebutuhan laundry. |

Pembagian tugas dapat disesuaikan dengan ketersediaan anggota kelompok dan pihak klien.

### 7. Penutup

Rencana pengujian ini menjadi pedoman untuk menguji Sistem Informasi Laundry Koin sebelum diterapkan. Pengujian diprioritaskan pada seluruh fitur Must Have, dilanjutkan dengan fitur Should Have, pengujian otomatis dasar, dan UAT bersama klien. Hasil pengujian digunakan sebagai dasar untuk memperbaiki kekurangan dan memastikan sistem sesuai dengan kebutuhan pengguna.
