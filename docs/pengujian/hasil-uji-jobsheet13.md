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

### 3. Hasil unittest
```text
Ran 48 tests in 23.552s
OK
```

### 4. Hasil uji_cepat
```text
SEMUA UJI LULUS
```

### 5. Mutasi yang diuji (Langkah 6)
| Mutasi | Uji yang gagal | Hasil |
|---|---|---|
| Hapus decorator peran pada /pelanggan | test_peran_terbatas_403 | FAILED (200 != 403) |
| Nonaktifkan pemeriksaan CSRF | test_csrf_tanpa_token_400 | FAILED (404 != 400) |
| Nonaktifkan header keamanan | test_header_keamanan | FAILED (assertion) |

Semua mutasi menyebabkan kegagalan uji, sehingga uji dianggap efektif.

### 6. Catatan
- Modul unittest lama sudah disesuaikan dengan autentikasi dan CSRF; seluruh 48 uji lulus.
- Test case tercatat pada docs/pengujian/test-case.md (36 TC).
- Matriks keterlacakan pada docs/matriks-keterlacakan.md.
