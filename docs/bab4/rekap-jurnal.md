# REKAP JURNAL VIBE CODING

## Sistem Informasi Laundry Koin

Sumber: `jurnal/nabila.md`, dihitung dengan `python alat/analisis_jurnal.py jurnal/*.md`.
Pencocokan manual dilakukan pada 10 entri acak: 1, 3, 4, 7, 8, 9, 11, 15, 16, 23; tidak ditemukan ketidaksesuaian format.

### Proporsi keputusan

| Keputusan | Jumlah | Persen |
|---|---|---|
| Terima | 14 | 56,0% |
| Ubah | 11 | 44,0% |
| Tolak | 0 | 0,0% |
| Total | 25 | 100% |

### Jenis galat AI

| Jenis galat | Jumlah |
|---|---|
| acuan-salah | 4 |
| keamanan | 4 |
| aturan-bisnis | 2 |
| arsitektur | 1 |
| di-luar-lingkup | 1 |
| keterbacaan | 1 |
| Total entri bertag galat | 13 |

Tag lain: `[Debug]` sebanyak 3 entri.

### Dampak waktu (perkiraan)

| Fitur | Perkiraan tanpa AI (jam) | Aktual dengan AI (jam) | Waktu tinjau + perbaiki (jam) | Catatan / sumber |
|---|---|---|---|---|
| CRUD Layanan | 8 | 4 | 2 | Riwayat commit 9944121–8332fe4; jurnal 1–3 |
| CRUD Pelanggan | 5 | 3 | 1,5 | Jurnal 9–11 |
| Modul transaksi dan pencarian | 10 | 6 | 3 | Jurnal 13–15 |
| Autentikasi dan peran | 10 | 6 | 3 | Jurnal 19–23 |
| Pengujian dan dokumentasi rilis | 12 | 8 | 4 | Jurnal 16–18; riwayatcommit rilis |

Semua angka pada tabel dampak waktu adalah perkiraan sendiri berdasarkan pengalaman mengerjakan tugas serupa, bukan pengukuran stopwatch; waktu tinjau dan perbaiki dihitung dari banyaknya entri "Ubah" pada jurnal. Keterbatasan ini dinyatakan pada 4.6.
