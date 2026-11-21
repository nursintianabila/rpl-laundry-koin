# SPESIFIKASI FITUR MODUL TRANSAKSI

## Sistem Informasi Laundry Koin

### 1. Pemilihan Entitas Berelasi

Entitas berelasi yang dipilih adalah **Transaksi**, yang merujuk ke `pelanggan` dan `layanan` melalui foreign key. Modul ini menerapkan JOIN, pilihan induk pada form, dan perhitungan total biaya.

### 2. Tabel Fitur Kecil (Langkah 2)

| No | Fitur kecil | Kriteria penerimaan (dari PRD) | KF |
|---|---|---|---|
| G1 | Daftar transaksi dengan JOIN | Daftar menampilkan nama pelanggan dan nama layanan (bukan hanya ID), memiliki keadaan kosong, dan query memakai alias yang jelas. | KF-04, KF-07 |
| G2 | Tambah transaksi dengan pilihan induk | Form memuat menu pilihan pelanggan dan layanan; berat bilangan > 0; tanggal format TTTT-BB-HH; ID induk yang tidak ada ditolak dengan pesan ramah; isian tetap tampil saat galat; redirect + flash saat berhasil. | KF-04, KQ-02 |
| G3 | Dampak pada tabel lain (total biaya) | Total biaya dihitung dari berat × harga layanan dan disimpan pada transaksi; validasi foreign key dijalankan sebelum penyimpanan. | KF-04 |
| G4 | Pencarian dan penyaringan (Sesi 2) | Pencarian berparameter dan penyaringan yang dapat digabung. | KF-05, KF-09 |

### 3. Aturan Validasi Transaksi

| Kolom | Aturan |
|---|---|
| `id_pelanggan` | Wajib dipilih; harus merujuk pelanggan yang ada. |
| `id_layanan` | Wajib dipilih; harus merujuk layanan yang ada. |
| `tanggal` | Wajib diisi; format TTTT-BB-HH (ISO). |
| `berat` | Wajib diisi; bilangan lebih dari 0. |
| `total_biaya` | Dihitung otomatis: `berat × harga layanan`, dibulatkan ke bilangan bulat. |

### 4. Catatan Ruang Lingkup

- Skema `transaksi` tidak mengubah stok atau data induk; dampak yang dihitung adalah `total_biaya`.
- Pencarian dan penyaringan dikerjakan pada Sesi 2 (Langkah 9–10).
- Kolom pencarian dan paginasi pada wireframe 03 tidak dikerjakan pada jobsheet ini.
