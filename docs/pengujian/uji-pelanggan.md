# HASIL UJI MODUL PELANGGAN

## Sistem Informasi Laundry Koin

### 1. Lingkungan Pengujian

- Tanggal: 21 November 2026
- Python: 3.14 (virtual environment `.venv`)
- Flask: 3.1.3
- Perintah: `python -m unittest tests.test_pelanggan -v`

### 2. Ringkasan

```text
Ran 11 tests in 0.910s

OK
```

### 3. Cakupan Uji

| Uji | Hasil |
|---|---|
| Halaman daftar kosong | Lulus — menampilkan "Belum ada data pelanggan." |
| Tambah pelanggan valid | Lulus — data tersimpan dan tampil |
| Nama kosong | Lulus — ditolak dengan pesan "Nama pelanggan wajib diisi." |
| Form ubah menampilkan data lama | Lulus |
| Ubah pelanggan berhasil | Lulus |
| Ubah ID tidak ditemukan | Lulus — 404 |
| Hapus pelanggan berhasil | Lulus |
| Hapus melalui GET | Lulus — 405, data tidak berubah |
| Hapus pelanggan yang dipakai transaksi | Lulus — ditolak dengan pesan galat |
| Nama berisi HTML | Lulus — tampil ter-escape |
| Nama berisi perintah SQL | Lulus — tersimpan sebagai teks |

### 4. Catatan

Modul pelanggan tidak menolak nama ganda karena skema `pelanggan` tidak memiliki constraint `UNIQUE`, sesuai rancangan agar dua pelanggan dapat memiliki nama sama.
