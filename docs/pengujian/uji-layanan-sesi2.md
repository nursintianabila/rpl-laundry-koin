# HASIL UJI SESI 2 — CRUD LAYANAN

## Sistem Informasi Laundry Koin

### 1. Lingkungan Pengujian

- Tanggal: 21 November 2026
- Python: 3.14 (virtual environment `.venv`)
- Flask: 3.1.3
- Basis data uji: SQLite sementara yang dibuat dari `docs/desain/schema.sql`
- Perintah: `python -m unittest discover -s tests -v`

### 2. Uji Kriteria Penerimaan F2–F5

| Fitur | Skenario | Hasil diharapkan | Hasil nyata / lulus? |
|---|---|---|---|
| F2 Daftar | Membuka `/layanan` saat ada data | Tabel ID, nama, harga, aksi tampil; harga berformat rupiah | Lulus |
| F2 Daftar | Membuka `/layanan` saat data kosong | Pesan "Belum ada data layanan." tampil tanpa tabel | Lulus |
| F3 Tambah | Isian valid | Data tersimpan, pesan sukses, tampil di daftar | Lulus |
| F3 Tambah | Nama kosong, harga negatif, harga bukan angka, nama duplikat | Ditolak dengan pesan jelas; isian tidak hilang | Lulus |
| F4 Ubah | Membuka form layanan yang ada | Form terisi nama dan harga lama | Lulus |
| F4 Ubah | Mengubah dengan data valid | Perubahan tersimpan dan tampil di daftar | Lulus |
| F4 Ubah | Nama sama dengan layanan lain | Ditolak dengan pesan "Nama layanan sudah ada." | Lulus |
| F4 Ubah | Nama sendiri dipertahankan, harga diubah | Perubahan harga tersimpan | Lulus |
| F4 Ubah | Membuka `/layanan/999/ubah` | Halaman 404 | Lulus |
| F5 Hapus | Menghapus layanan yang tidak dipakai | Data terhapus, pesan sukses tampil | Lulus |
| F5 Hapus | Menghapus layanan yang dipakai transaksi | Data tidak terhapus, pesan galat jelas tampil | Lulus |
| F5 Hapus | Membuka alamat hapus melalui GET | Status 405, data tidak berubah | Lulus |
| F5 Hapus | Membuka `/layanan/999/hapus` melalui POST | Halaman 404 | Lulus |

### 3. Uji Keamanan Sederhana

| Uji | Masukan | Hasil diharapkan | Hasil nyata / lulus? |
|---|---|---|---|
| SQL injection | `Robert'); DROP TABLE layanan;--` | Tersimpan sebagai teks biasa; tabel tidak terhapus | Lulus — data tersimpan persis dan tabel `layanan` masih dapat dibaca |
| XSS | `<b>tes</b>` | Teks tampil apa adanya, bukan tebal | Lulus — HTML menampilkan `&lt;b&gt;tes&lt;/b&gt;` |

### 4. Uji Skema

`python tests/cek_skema.py` menghasilkan:

```text
OK ditolak: 6
GAGAL: 0
```

Skema tidak berubah dan seluruh aturan `CHECK` serta foreign key masih berfungsi.

### 5. Ringkasan Otomatis

```text
Ran 18 tests in 1.078s

OK
```

Seluruh 18 pengujian lulus.
