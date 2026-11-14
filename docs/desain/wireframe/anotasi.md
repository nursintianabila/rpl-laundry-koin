# ANOTASI WIREFRAME

## Sistem Informasi Laundry Koin

Dokumen ini berisi anotasi elemen penting pada setiap wireframe, meliputi data atau aksi, aturan, pesan yang muncul, dan prinsip antarmuka yang diterapkan.

### 1. Halaman Login

| No | Elemen | Data / Aksi | Aturan / Pesan | Prinsip |
|---|---|---|---|---|
| 1 | Username / Email | Memasukkan username atau email | Wajib diisi; jika kosong muncul pesan "Username atau email wajib diisi" | Pencegahan galat |
| 2 | Password | Memasukkan kata sandi | Wajib diisi; jika salah muncul pesan "Username atau password salah" | Pencegahan galat |
| 3 | Tombol Masuk | Memproses login | Jika berhasil masuk ke halaman sesuai hak akses; jika gagal tampil pesan kesalahan | Umpan balik |

### 2. Halaman Dashboard

| No | Elemen | Data / Aksi | Aturan / Pesan | Prinsip |
|---|---|---|---|---|
| 1 | Menu Navigasi | Berpindah ke halaman sistem | Menu harus konsisten pada halaman lain | Konsistensi |
| 2 | Kartu Ringkasan | Menampilkan total transaksi, pendapatan, layanan, dan status mesin | Data ditampilkan sesuai kondisi terbaru | Keterbacaan |
| 3 | Tabel Transaksi Terbaru | Melihat ringkasan transaksi | Jika belum ada transaksi tampil pesan "Belum ada transaksi" | Umpan balik |
| 4 | Tombol Logout | Mengakhiri sesi pengguna | Pengguna diarahkan kembali ke halaman login | Konsistensi |

### 3. Halaman Daftar Transaksi

| No | Elemen | Data / Aksi | Aturan / Pesan | Prinsip |
|---|---|---|---|---|
| 1 | Kolom Pencarian | Mencari transaksi | Pencarian berdasarkan kata kunci; jika tidak ditemukan tampil "Data transaksi tidak ditemukan" | Pencegahan galat |
| 2 | Tombol Tambah Transaksi | Membuka formulir transaksi | Mengarahkan pengguna ke halaman Form Transaksi | Konsistensi |
| 3 | Tabel Transaksi | Menampilkan data transaksi | Data ditampilkan dalam kolom yang jelas dan mudah dibaca | Keterbacaan |
| 4 | Tombol Detail | Melihat informasi transaksi | Membuka halaman Detail Transaksi | Umpan balik |

### 4. Halaman Form Transaksi

| No | Elemen | Data / Aksi | Aturan / Pesan | Prinsip |
|---|---|---|---|---|
| 1 | ID Transaksi | Nomor transaksi otomatis | Dibuat oleh sistem dan tidak diisi manual | Pencegahan galat |
| 2 | Data Pelanggan | Memilih atau memasukkan pelanggan | Data pelanggan wajib dipilih atau diisi sesuai ketentuan | Pencegahan galat |
| 3 | Layanan | Memilih layanan laundry | Layanan harus dipilih dari daftar yang tersedia | Pencegahan galat |
| 4 | Tanggal Transaksi | Menentukan tanggal transaksi | Format tanggal harus valid | Pencegahan galat |
| 5 | Total Biaya | Menampilkan total biaya otomatis | Dihitung berdasarkan layanan dan ketentuan harga | Konsistensi |
| 6 | Tombol Simpan | Menyimpan transaksi | Jika berhasil tampil "Transaksi berhasil disimpan"; jika gagal tampil pesan kesalahan | Umpan balik |
| 7 | Tombol Batal | Membatalkan pengisian | Kembali ke halaman sebelumnya tanpa menyimpan data | Konsistensi |

### 5. Halaman Detail Transaksi

| No | Elemen | Data / Aksi | Aturan / Pesan | Prinsip |
|---|---|---|---|---|
| 1 | Informasi ID Transaksi | Melihat nomor transaksi | Ditampilkan sesuai transaksi yang dipilih | Keterbacaan |
| 2 | Informasi Pelanggan | Melihat data pelanggan | Data sesuai dengan transaksi | Konsistensi |
| 3 | Informasi Layanan dan Tanggal | Melihat layanan serta tanggal transaksi | Informasi ditampilkan dengan jelas | Keterbacaan |
| 4 | Total Biaya dan Status | Melihat jumlah biaya dan status transaksi | Nilai dan status harus sesuai data transaksi | Umpan balik |
| 5 | Tombol Kembali | Kembali ke daftar transaksi | Mengarahkan pengguna ke halaman Daftar Transaksi | Konsistensi |

### 6. Halaman Layanan dan Harga

| No | Elemen | Data / Aksi | Aturan / Pesan | Prinsip |
|---|---|---|---|---|
| 1 | Tombol Tambah Layanan | Menambahkan layanan baru | Data layanan wajib diisi sesuai ketentuan | Konsistensi |
| 2 | Tabel Layanan | Menampilkan nama dan harga layanan | Informasi disusun dalam kolom yang mudah dibaca | Keterbacaan |
| 3 | Tombol Ubah | Mengubah data layanan | Perubahan disimpan setelah validasi berhasil | Umpan balik |
| 4 | Tombol Hapus | Menghapus layanan | Sistem meminta konfirmasi sebelum menghapus | Pencegahan galat |
| 5 | Pesan Sistem | Menampilkan hasil pengelolaan layanan | Contoh: "Layanan berhasil disimpan" atau "Harga tidak valid" | Umpan balik |

### 7. Halaman Data Pelanggan

| No | Elemen | Data / Aksi | Aturan / Pesan | Prinsip |
|---|---|---|---|---|
| 1 | Kolom Pencarian | Mencari data pelanggan | Jika tidak ditemukan tampil "Data pelanggan tidak ditemukan" | Umpan balik |
| 2 | Tombol Tambah Pelanggan | Menambahkan pelanggan | Data pelanggan wajib diisi sesuai ketentuan | Konsistensi |
| 3 | Tabel Pelanggan | Menampilkan data pelanggan | Data ditampilkan dalam kolom yang jelas | Keterbacaan |
| 4 | Tombol Ubah / Hapus | Mengelola data pelanggan | Hapus data harus melalui konfirmasi | Pencegahan galat |
| 5 | Pesan Sistem | Menampilkan hasil pengelolaan data | Contoh: "Data pelanggan berhasil disimpan" | Umpan balik |

### 8. Halaman Laporan Pendapatan

| No | Elemen | Data / Aksi | Aturan / Pesan | Prinsip |
|---|---|---|---|---|
| 1 | Filter Tanggal | Menentukan periode laporan | Tanggal awal tidak boleh melebihi tanggal akhir | Pencegahan galat |
| 2 | Tombol Tampilkan Laporan | Menampilkan laporan berdasarkan periode | Jika data kosong tampil "Tidak ada data pada periode ini" | Umpan balik |
| 3 | Ringkasan Pendapatan | Melihat jumlah pendapatan dan transaksi | Nilai disesuaikan dengan periode yang dipilih | Keterbacaan |
| 4 | Tabel Laporan | Melihat rincian transaksi | Data ditampilkan secara terstruktur | Keterbacaan |
| 5 | Tombol Cetak / Unduh | Mencetak atau mengunduh laporan | Sistem memberikan hasil atau pesan jika proses gagal | Umpan balik |

### 9. Halaman Status Mesin

| No | Elemen | Data / Aksi | Aturan / Pesan | Prinsip |
|---|---|---|---|---|
| 1 | Tabel Mesin | Menampilkan daftar mesin | Informasi mesin ditampilkan secara terstruktur | Keterbacaan |
| 2 | Informasi Status | Melihat status mesin | Status menggunakan istilah yang konsisten | Konsistensi |
| 3 | Tombol Ubah Status | Memperbarui status mesin | Status hanya dapat dipilih dari pilihan yang tersedia | Pencegahan galat |
| 4 | Pesan Sistem | Menampilkan hasil perubahan status | Contoh: "Status mesin berhasil diperbarui" atau "Gagal memperbarui status mesin" | Umpan balik |

## 10. Pemeriksaan Prinsip Antarmuka

Pemeriksaan dilakukan terhadap seluruh halaman wireframe berdasarkan prinsip berikut:

| No | Prinsip | Pemeriksaan |
|---|---|---|
| 1 | Konsistensi | Menu navigasi, istilah, dan tombol yang memiliki fungsi sama menggunakan tampilan dan penamaan yang konsisten |
| 2 | Umpan balik | Setiap aksi seperti simpan, ubah, hapus, pencarian, cetak, dan unduh memberikan pesan hasil |
| 3 | Keterbacaan | Judul, label, tabel, dan tombol menggunakan istilah yang mudah dipahami dan susunan yang jelas |
| 4 | Pencegahan galat | Isian wajib diberi penanda, format data dibatasi, pilihan menggunakan daftar, dan penghapusan meminta konfirmasi |

## 11. Catatan Sebelum dan Sesudah Penerapan Prinsip

**Contoh: Form Transaksi**

- Sebelum: Form transaksi belum menjelaskan secara lengkap aturan pengisian data dan belum menampilkan pesan kesalahan yang spesifik.
- Sesudah: Form transaksi mencantumkan aturan pengisian data pelanggan, pilihan layanan, dan tanggal transaksi. Sistem juga menampilkan pesan ketika penyimpanan berhasil atau gagal.

**Prinsip yang diterapkan:** Pencegahan galat dan umpan balik.

Catatan: Pesan dan aturan pada dokumen ini menjadi acuan anotasi dan perlu disesuaikan dengan skenario use case serta tampilan wireframe yang digunakan.