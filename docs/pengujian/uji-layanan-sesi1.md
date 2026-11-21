# HASIL UJI SESI 1 — CRUD LAYANAN

## Sistem Informasi Laundry Koin

### 1. Lingkungan Pengujian

- Tanggal: 21 November 2026
- Python: 3.14 (virtual environment `.venv`)
- Flask: 3.1.3
- Basis data: SQLite `instance/laundry_koin.db`
- Perintah: `python -m unittest discover -s tests -v`

### 2. Tabel Uji Tambah Layanan (Langkah 6)

| No | Masukan uji | Hasil diharapkan | Hasil nyata / lulus? |
|---|---|---|---|
| 1 | Nama "Cuci Kering", harga 7000 | Tersimpan; muncul pesan sukses; tampil di daftar | Lulus — data tersimpan, pesan "Layanan berhasil ditambahkan.", tampil sebagai Rp 7.000 |
| 2 | Nama kosong (spasi saja) | Ditolak; pesan galat jelas; data tidak tersimpan | Lulus — pesan "Nama layanan wajib diisi.", jumlah data tetap 0 |
| 3 | Harga −5 | Ditolak; pesan galat | Lulus — pesan "Harga tidak boleh negatif.", jumlah data tetap 0 |
| 4 | Harga "abc" | Ditolak; pesan galat; isian tidak hilang | Lulus — pesan "Harga harus berupa bilangan bulat...", nilai "abc" dan nama tetap tampil |
| 5 | Nama "cuci kering" setelah "Cuci Kering" tersimpan | Ditolak; pesan "sudah ada" | Lulus — pesan "Nama layanan sudah ada. Gunakan nama lain.", jumlah data tetap 1 |

### 3. Uji Tambahan

| Uji | Hasil |
|---|---|
| Halaman daftar saat tabel kosong | Lulus — menampilkan "Belum ada data layanan." tanpa tabel |
| Form tambah dapat dibuka (GET) | Lulus — status 200 dan judul "TAMBAH LAYANAN" tampil |
| Pengujian skema `tests/cek_skema.py` | Lulus — 6 penolakan sesuai harapan, 0 gagal |

### 4. Ringkasan Otomatis

```text
Ran 7 tests in 0.511s

OK
```

Seluruh pengujian Sesi 1 lulus. Pengujian ubah, hapus, keamanan masukan, dan tinjauan menyeluruh dilakukan pada Sesi 2.
