# TRIASE TEMUAN — JOBSHEET 12

## Sistem Informasi Laundry Koin

| No | Temuan (ID) | Risiko | Keputusan | Alasan / rencana |
|---|---|---|---|---|
| 1 | T-01 SQL injection | Tinggi | Diperbaiki | Query berparameter (Jobsheet 10) |
| 2 | T-02 Hapus via GET | Tinggi | Diperbaiki | POST + peran + CSRF (Jobsheet 11-12) |
| 3 | T-03 MD5 | Tinggi | Diperbaiki | Werkzeug hash (Jobsheet 11) |
| 4 | T-04 IDOR | Tinggi | Diperbaiki | Filter kepemilikan (catatan) |
| 5 | T-05 Kunci rahasia/debug | Tinggi | Diperbaiki | Env + debug flag (Jobsheet 11-12) |
| 6 | Batas percobaan login | Sedang | Diperbaiki | Langkah 12 Jobsheet 12 |
| 7 | Token CSRF | Sedang | Diperbaiki | Jobsheet 11-12 |
| 8 | Cookie Secure | Rendah | Ditunda | Sprint 3 (deploy HTTPS) |
| 9 | Pembulatan total biaya | Rendah | Ditunda | Sprint 3 (ubah skema) |
| 10 | Pencarian/paginasi pelanggan | Sedang | Ditunda | Sprint 3 |

Setiap temuan ditanggapi dengan satu komentar pada Issue (jika ada).
