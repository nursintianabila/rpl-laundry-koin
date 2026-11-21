# AUDIT KESIAPAN RILIS — JOB SHEET 14

## Sistem Informasi Laundry Koin

### Hasil tiga pemeriksaan Git (Langkah 2)
```text
git ls-files "*.db" ".env"                 -> (kosong)
git grep -nI "secret_key"                   -> hanya variabel lingkungan dan contoh di dokumentasi
git log --all --oneline -- "*.db" ".env"    -> (kosong)
```

### Daftar Periksa (Lampiran B)
| No | Butir | Ya / Tidak |
|---|---|---|
| 1 | pytest dan uji_cepat.py lulus | Ya (60 pytest, SEMUA UJI LULUS) |
| 2 | Tidak ada .db atau .env dilacak Git; riwayat bersih | Ya |
| 3 | Tidak ada kunci rahasia/kata sandi asli pada kode | Ya |
| 4 | SECRET_KEY, APP_ENV, TOKO_DB dari lingkungan; produksi tanpa SECRET_KEY menolak start | Ya |
| 5 | requirements.txt berversi persis; waitress dicatat | Sebagian (Lihat Langkah 4) |
| 6 | debug mati pada produksi; tidak ada host 0.0.0.0 tertulis | Ya |
| 7 | Akun awal dibuat dengan skrip; tidak ada kata sandi bawaan | Ya |
| 8 | Aplikasi dapat diakses dari komputer kedua | Menunggu Langkah 5 |
| 9 | Keputusan COOKIE_SECURE dicatat | Menunggu Langkah 5 |
| 10 | Cadangan dibuat dan pemulihan teruji | Menunggu Langkah 6 |
| 11 | Nomor versi terlihat di aplikasi; CHANGELOG.md memuat versi | Ya |
| 12 | Tag beranotasi v1.0.0 dan Release tersedia | Menunggu Langkah 7 |
| 13 | README lulus uji orang asing | Menunggu Langkah 8 |
| 14 | Manual pengguna mencakup semua skenario UAT | Menunggu Langkah 9 |
