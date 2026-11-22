# Sistem Informasi Laundry Koin

Aplikasi web untuk mengelola operasional laundry koin: data layanan dan harga, data pelanggan, pencatatan transaksi, pencarian transaksi, serta pengelolaan pengguna dan hak akses.

Versi saat ini: **1.0.0** (lihat [CHANGELOG.md](CHANGELOG.md)).

Dibuat sebagai proyek mata kuliah Rekayasa Perangkat Lunak, Prodi D3 Teknologi Informasi, Politeknik Sampit.

## Fitur

- Login dengan dua peran: **Pemilik** dan **Admin/Operator**, dengan kata sandi ter-hash.
- Pengelolaan layanan dan harga (tambah, ubah, hapus, cari layanan).
- Pengelolaan data pelanggan (tambah, ubah, hapus).
- Pencatatan transaksi dengan total biaya dihitung otomatis dari berat dan harga layanan.
- Pencarian dan penyaringan transaksi berparameter.
- Dashboard dan laporan pendapatan untuk Pemilik; riwayat transaksi hanya-baca.
- Pembaruan status mesin dan notifikasi transaksi selesai untuk Admin/Operator.
- Pemisahan lapisan Routes → Services → Models → Database.
- Token CSRF, batas percobaan login, dan header keamanan dasar.

## Kebutuhan

- Python 3.10 atau lebih baru.
- Git (untuk mengambil kode).

## Instalasi

```powershell
git clone https://github.com/nursintianabila/rpl-laundry-koin.git
cd rpl-laundry-koin
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install -r requirements.txt
```

Dependensi pengujian:

```powershell
python -m pip install -r requirements-dev.txt
```

## Konfigurasi (variabel lingkungan)

| Variabel | Fungsi | Bawaan |
|---|---|---|
| `APP_ENV` | `production` untuk mode produksi | pengembangan |
| `SECRET_KEY` | Kunci sesi, **wajib** pada produksi | acak (development) |
| `TOKO_DB` | Lokasi berkas basis data | `instance/laundry_koin.db` |
| `COOKIE_SECURE` | `1` = cookie hanya HTTPS; `0` untuk HTTP jaringan tertutup | `1` pada produksi |

Buat kunci acak:

```powershell
python -c "import secrets; print(secrets.token_hex(32))"
```

**Jangan menyimpan kunci di dalam kode atau Git.**

## Membuat akun pertama

```powershell
python buat_pengguna.py
```

Masukkan nama pengguna (email), peran (`Pemilik` atau `Admin/Operator`), dan kata sandi. Kata sandi diketik di terminal dan tidak tersimpan di berkas mana pun.

## Menjalankan

Pengembangan:

```powershell
python app.py
```

Buka `http://127.0.0.1:5000`.

Produksi (Waitress):

```powershell
python -m pip install waitress
$env:APP_ENV='production'
$env:SECRET_KEY='<kunci-acak>'
$env:TOKO_DB='C:\laundry\laundry_koin.db'
waitress-serve --listen=127.0.0.1:8000 app:app
```

Buka `http://127.0.0.1:8000`. Untuk akses dari komputer lain pada jaringan toko tertutup, gunakan `--listen=0.0.0.0:8000` dan izinkan port 8000 pada firewall.

Aplikasi menolak berjalan pada mode produksi tanpa `SECRET_KEY`.

## Pengujian

```powershell
python -m pytest -q tests
python -m unittest discover -s tests
python tests/uji_cepat.py
```

## Cadangan dan pemulihan

Lihat [docs/cadangan.md](docs/cadangan.md).

## Struktur

```text
app.py                 aplikasi Flask dan konfigurasi
models.py              koneksi dan operasi basis data
routes/                rute HTTP per modul
services/              logika bisnis dan validasi
templates/             templat Jinja2
static/css/            gaya tampilan
tests/                 pengujian otomatis
docs/                  dokumentasi proyek
versi.py               nomor versi aplikasi
cadangkan.py           skrip pencadangan basis data
buat_pengguna.py       skrip pembuatan akun
requirements.txt       dependensi produksi
requirements-dev.txt   dependensi pengujian
```
