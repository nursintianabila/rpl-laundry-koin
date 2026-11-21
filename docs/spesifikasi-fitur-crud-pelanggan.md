# SPESIFIKASI FITUR KECIL — CRUD PELANGGAN

## Sistem Informasi Laundry Koin

### 1. Pemilihan Entitas Kedua

Entitas kedua yang dipilih adalah **Pelanggan**. Alasannya:

- Tabel `pelanggan` hanya memiliki satu kolom data (`nama_pelanggan`) dan tidak bergantung pada tabel lain.
- Pelanggan berelasi dengan `transaksi` melalui `transaksi.id_pelanggan`, sehingga penghapusan dapat menguji kunci asing.
- Fitur ini termasuk kebutuhan **Must Have KF-03 (Pengelolaan data pelanggan)** pada PRD dan Product Backlog Sprint 1.
- Halaman acuan tampilan: `docs/desain/wireframe/07-data-pelanggan.md`.

### 2. Tabel Fitur Kecil

| No | Fitur kecil | Kriteria penerimaan (dari PRD) | KF |
|---|---|---|---|
| F1 | Kerangka modul pelanggan | Modul pelanggan terdaftar pada aplikasi; daftar pelanggan dapat dibuka. | — |
| F2 | Daftar pelanggan | Given data pelanggan telah tersedia, When pengguna membuka `/pelanggan`, Then sistem menampilkan tabel berisi ID, nama pelanggan, dan aksi; bila kosong, tampil pesan "Belum ada data pelanggan."; tidak ada SQL di routes. | KF-03 |
| F3 | Tambah pelanggan | Given pengguna mengisi nama pelanggan yang valid, When disimpan, Then data tersimpan, pesan sukses tampil, dan pengguna dialihkan ke daftar (Post–Redirect–Get). Nama kosong dan nama lebih dari 100 karakter harus ditolak; isian tidak hilang. | KF-03, KQ-02 |
| F4 | Ubah pelanggan | Given pelanggan sudah tersimpan, When pengguna mengubah nama dengan data valid, Then perubahan tersimpan; form terisi data lama; nama kosong ditolak; ID yang tidak ditemukan menghasilkan 404. | KF-03, KQ-02 |
| F5 | Hapus pelanggan | Given pelanggan tidak dipakai transaksi, When pengguna mengonfirmasi hapus melalui POST, Then data terhapus. Pelanggan yang dipakai transaksi tidak terhapus dan muncul pesan jelas; GET tidak menghapus data. | KF-03 |

### 3. Aturan Validasi Pelanggan

| Kolom | Aturan |
|---|---|
| `nama_pelanggan` | Wajib diisi; spasi di awal/akhir dibuang; maksimal 100 karakter. |

### 4. Catatan Ruang Lingkup

- Skema `pelanggan` hanya menyimpan nama pelanggan, sehingga modul ini tidak menambah kolom identitas tambahan.
- Nama pelanggan tidak memiliki constraint `UNIQUE` pada `schema.sql`; dua pelanggan boleh memiliki nama sama karena hal itu wajar pada data nyata.
- Kolom pencarian dan paginasi pada wireframe 07 tidak dikerjakan pada jobsheet ini.
