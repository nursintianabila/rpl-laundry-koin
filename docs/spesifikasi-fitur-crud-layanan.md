# SPESIFIKASI FITUR KECIL — CRUD LAYANAN

## Sistem Informasi Laundry Koin

### 1. Pemilihan Entitas Pertama

Entitas pertama yang dipilih adalah **Layanan**. Alasannya:

- Tabel `layanan` tidak bergantung pada tabel lain (tidak memiliki foreign key), sehingga sesuai dengan arahan Jobsheet 9 untuk memilih entitas induk dengan relasi paling sedikit.
- Data layanan menjadi acuan pencatatan transaksi melalui `transaksi.id_layanan`.
- Fitur ini termasuk kebutuhan **Must Have KF-02 (Pengelolaan layanan dan harga)** pada PRD dan Product Backlog Sprint 1.
- Halaman acuan tampilan: `docs/desain/wireframe/06-layanan-harga.md`.

### 2. Tabel Fitur Kecil

| No | Fitur kecil | Kriteria penerimaan (dari PRD) | KF |
|---|---|---|---|
| F1 | Kerangka proyek | Aplikasi Flask berjalan tanpa galat; basis data `instance/laundry_koin.db` terbentuk dari `docs/desain/schema.sql`; koneksi SQLite mengaktifkan `PRAGMA foreign_keys = ON`; halaman beranda mengalihkan ke `/layanan`; navigasi dasar sesuai wireframe tampil. | — |
| F2 | Daftar layanan | Given data layanan telah tersedia, When pengguna membuka `/layanan`, Then sistem menampilkan tabel berisi ID, nama layanan, harga, dan kolom aksi sesuai wireframe; harga tampil dalam format rupiah; bila belum ada data, tampil pesan "Belum ada data"; tidak ada perintah SQL pada routes. | KF-02, KF-10 |
| F3 | Tambah layanan | Given pengguna membuka form tambah layanan, When nama layanan dan harga yang valid disimpan, Then data tersimpan, pesan sukses tampil, dan pengguna dialihkan ke daftar (Post–Redirect–Get). Nama kosong, harga negatif, harga bukan angka, dan nama yang sudah ada harus ditolak dengan pesan galat; isian yang sudah diketik tidak hilang. | KF-02, KQ-02 |
| F4 | Ubah layanan | Given layanan sudah tersimpan, When pengguna mengubah nama atau harga dengan data valid, Then perubahan tersimpan dan terlihat pada daftar; form terisi data lama; hanya kolom nama dan harga yang dapat diubah; nama kosong, harga tidak valid, atau nama duplikat ditolak; ID yang tidak ditemukan menghasilkan halaman 404. | KF-02, KQ-02 |
| F5 | Hapus layanan | Given layanan tidak dipakai transaksi, When pengguna mengonfirmasi hapus melalui POST, Then data terhapus dan pesan sukses tampil; layanan yang dipakai tabel `transaksi` tidak terhapus dan muncul pesan yang jelas; membuka alamat hapus melalui GET tidak mengubah data. | KF-02 |

### 3. Aturan Validasi Layanan

| Kolom | Aturan |
|---|---|
| `nama_layanan` | Wajib diisi; spasi di awal/akhir dibuang; maksimal 100 karakter; tidak boleh sama dengan nama layanan lain (tanpa membedakan huruf besar/kecil). |
| `harga` | Wajib diisi; berupa bilangan bulat; tidak boleh negatif. |

### 4. Catatan Ruang Lingkup

- Kolom `id_layanan` dibuat otomatis oleh SQLite dan tidak dapat diubah dari form.
- Nama layanan belum memiliki constraint `UNIQUE` pada `schema.sql`, sehingga pencegahan nama ganda dilakukan pada lapisan service sebagai aturan bisnis. Bila nanti disepakati menjadi constraint basis data, `schema.sql` dan kamus data harus diperbarui lebih dahulu.
- Kolom aksi pada tahap Sesi 1 baru menampilkan tautan yang tersedia; tombol Ubah dan Hapus dilengkapi pada Sesi 2 (F4 dan F5).
