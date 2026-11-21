# RENCANA SPRINT RTM-2

## Sistem Informasi Laundry Koin

### 1. Identitas

- Proyek: Sistem Informasi Laundry Koin (`rpl-laundry-koin`)
- Pelaksana: Nur Sintia Nabila (individu, atas persetujuan dosen)
- Dasar perencanaan: `docs/product-backlog.md`, `PRD.md`, dan Jobsheet 9 Langkah 15

### 2. Kondisi Saat Ini

Modul CRUD yang sudah tersedia pada branch fitur:

- Layanan: daftar, tambah, ubah, hapus, validasi, uji keamanan dasar.
- Pelanggan: daftar, tambah, ubah, hapus, validasi, uji keamanan dasar.

Kebutuhan yang belum dikerjakan: transaksi, riwayat, dashboard, laporan, status mesin, autentikasi, dan hak akses.

### 3. Sprint 1 (Minggu 10) — Fondasi Transaksi

| ID | Fitur | Tugas | Target |
|---|---|---|---|
| KF-04 | Pencatatan transaksi | Form transaksi memilih pelanggan dan layanan; hitung total biaya; simpan transaksi | Akhir Sprint 1 |
| KF-05 | Riwayat transaksi | Pencarian transaksi berdasarkan informasi yang tersedia | Akhir Sprint 1 |
| KF-07 | Daftar transaksi | Halaman daftar transaksi | Akhir Sprint 1 |
| KF-10 | Informasi layanan dan harga | Tampilan layanan untuk kebutuhan transaksi | Akhir Sprint 1 |
| KF-13 | Rincian transaksi | Halaman rincian transaksi | Akhir Sprint 1 |

Checkpoint Minggu 10: transaksi dapat dicatat, dicari, dan ditampilkan.

### 4. Sprint 2 (Minggu 11) — Laporan dan Penyaringan

| ID | Fitur | Tugas | Target |
|---|---|---|---|
| KF-06 | Dashboard | Ringkasan informasi usaha berdasarkan data tersimpan | Akhir Sprint 2 |
| KF-08 | Ringkasan pendapatan | Perhitungan pendapatan dari transaksi | Akhir Sprint 2 |
| KF-09 | Filter periode laporan | Laporan berdasarkan rentang tanggal | Akhir Sprint 2 |
| KF-11 | Perubahan transaksi | Ubah data transaksi sesuai hak akses | Akhir Sprint 2 |

Checkpoint Minggu 11: laporan pendapatan dan perubahan transaksi berfungsi.

### 5. Sprint 3 (Minggu 12) — Keamanan dan Peninjauan

| ID | Fitur | Tugas | Target |
|---|---|---|---|
| KF-12 | Pembaruan status mesin | CRUD status mesin | Akhir Sprint 3 |
| KQ-01 | Password hash | Penyimpanan kata sandi dalam bentuk hash | Akhir Sprint 3 |
| KQ-02 | Validasi formulir | Validasi data wajib pada login, layanan, dan pelanggan | Akhir Sprint 3 |
| — | Tinjauan kode | Code review, pemeriksaan keamanan, perbaikan temuan | Akhir Sprint 3 |

Checkpoint Minggu 12: code review dan keamanan; temuan CRUD layanan (constraint `UNIQUE`, token CSRF) ditindaklanjuti atau dicatat.

### 6. Sprint 4 (Minggu 13–14) — Autentikasi dan Integrasi

| ID | Fitur | Tugas | Target |
|---|---|---|---|
| KF-01 | Login dan hak akses | Autentikasi pengguna dan pembatasan akses berdasarkan peran | Akhir Sprint 4 |
| — | Integrasi | Menghubungkan layanan dan pelanggan ke transaksi; pengujian menyeluruh | Akhir Sprint 4 |

Checkpoint Minggu 14: sistem terintegrasi dan siap RTM-2.

### 7. Target Minggu 10

Relasi, pencarian, dan penyaringan diprioritaskan: transaksi yang menghubungkan pelanggan dan layanan, pencarian transaksi, serta penyaringan daftar transaksi.

### 8. Catatan

- Proyek dikerjakan secara individu atas persetujuan dosen, meskipun jobsheet menyebut kerja kelompok.
- Perubahan kebutuhan harus ditinjau terlebih dahulu dan disesuaikan dengan PRD.
- Jurnal Vibe Coding diperbarui setiap siklus pengembangan.
