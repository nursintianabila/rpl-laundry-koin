# HASIL UJI — JOBSHEET 13

## Sistem Informasi Laundry Koin

### 1. Lingkungan
- Python 3.14, pytest 9.1.1, Flask 3.1.3
- Basis data sementara (tempfile), tidak menyentuh instance/laundry_koin.db

### 2. Hasil pytest
```text
tests/test_draf_ai.py ......  [100%]
6 passed in 3.00s
```

### 3. Hasil uji_cepat
```text
SEMUA UJI LULUS
```

### 4. Mutasi yang diuji (Langkah 6)
| Mutasi | Uji yang gagal | Hasil |
|---|---|---|
| Hapus decorator peran pada /pelanggan | test_peran_terbatas_403 | FAILED (200 != 403) |
| Nonaktifkan pemeriksaan CSRF | test_csrf_tanpa_token_400 | FAILED (404 != 400) |
| Nonaktifkan header keamanan | test_header_keamanan | FAILED (assertion) |

Semua mutasi menyebabkan kegagalan uji, sehingga uji dianggap efektif.

### 5. Catatan
- Modul unittest lama (test_layanan, test_pelanggan, test_transaksi) belum disesuaikan dengan autentikasi; akan diperbarui pada Langkah 12/15. uji_cepat.py sudah disesuaikan.
- Test case tercatat pada docs/pengujian/test-case.md (36 TC).
- Matriks keterlacakan pada docs/matriks-keterlacakan.md.
