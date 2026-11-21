# DEPLOYMENT — SISTEM INFORMASI LAUNDRY KOIN

## Jobsheet 14 Langkah 5

### Lingkungan yang disepakati
Komputer toko / laptop demo dengan Python 3.10+ pada jaringan tertutup.

### Perintah (Windows PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install -r requirements.txt
$env:APP_ENV='production'
$env:SECRET_KEY='<kunci-acak-dari: python -c "import secrets; print(secrets.token_hex(32))">'
$env:TOKO_DB='C:\laundry\laundry_koin.db'
python buat_pengguna.py
waitress-serve --listen=127.0.0.1:8000 app:app
```

### Akses dari komputer kedua (jaringan toko tertutup)
```powershell
waitress-serve --listen=0.0.0.0:8000 app:app
```
Buka `http://[alamat-IP]:8000` dari komputer kedua dan izinkan port 8000 pada firewall.

### Keputusan COOKIE_SECURE
- Pada HTTPS: biarkan `COOKIE_SECURE=1` (bawaan produksi).
- Pada HTTP jaringan tertutup: `COOKIE_SECURE=0` hanya jika login gagal tersimpan. Risiko: sesi dapat disadap bila jaringan tidak terpercaya. Jangan gunakan `0` bila aplikasi dapat diakses dari internet.

### Akun klien
Akun Pemilik dan Admin/Operator dibuat dengan `python buat_pengguna.py`; kata sandi awal diserahkan langsung kepada klien dan diganti oleh klien. Tidak ada kata sandi di kode atau dokumen.

Status: perintah di atas sudah diuji pada komputer sendiri (Langkah 4). Uji dari komputer kedua dilakukan oleh mahasiswa/penguji pada lingkungan praktikum.
