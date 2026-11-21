# TINJAUAN KODE MODUL TRANSAKSI

## Sistem Informasi Laundry Koin

### 1. Ruang Lingkup
Tinjauan dilakukan pada diff modul transaksi terhadap `fitur/crud-pelanggan`, meliputi `models.py`, `services/transaksi_service.py`, `routes/transaksi_routes.py`, dan template transaksi.

### 2. Daftar Periksa
| Butir | Hasil |
|---|---|
| SQL hanya berada di `models.py` | Sesuai |
| Query menggunakan parameter (`?`) | Sesuai |
| JOIN memakai alias yang jelas | Sesuai |
| Routes tidak membuka koneksi SQLite | Sesuai |
| Validasi dilakukan di server | Sesuai |
| Total biaya dihitung di service, bukan diisi pengguna | Sesuai |
| Hapus transaksi hanya melalui POST | Sesuai |
| Hapus induk yang dipakai transaksi ditolak dengan pesan | Sesuai |
| Kunci rahasia tidak ditulis di kode | Sesuai |

### 3. Temuan dan Tindakan
| No | Temuan | Kategori | Tindakan |
|---|---|---|---|
| 1 | Total biaya dihitung di Python dengan `round()`; untuk harga dengan sen, pembulatan dapat menyimpang. | Kebenaran | **Dicatat untuk Minggu 11** — skema saat ini menyimpan `total_biaya` sebagai INTEGER; bila nanti diperlukan sen, skema dan kamus data harus diubah lebih dahulu. |
| 2 | Form transaksi belum memiliki token CSRF. | Keamanan | **Dicatat untuk Minggu 12** — sama dengan modul sebelumnya. |
| 3 | Pencarian dan penyaringan belum dikerjakan. | Kesesuaian | **Dikerjakan pada Sesi 2 (Langkah 9–10).** |

### 4. Kesimpulan
Modul transaksi memenuhi kriteria G1–G3. Validasi foreign key dijalankan sebelum penyimpanan dan total biaya dihitung otomatis.
