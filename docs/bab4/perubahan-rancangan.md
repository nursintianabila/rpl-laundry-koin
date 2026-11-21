# PERUBAHAN TERHADAP RANCANGAN AWAL (BAB 3 → HASIL AKHIR)

## Sistem Informasi Laundry Koin

Tabel ini menjelaskan perbedaan antara rancangan Bab 3 dan hasil akhir implementasi, beserta alasannya. Tujuannya adalah menjelaskan keputusan, bukan menutupi penyimpangan.

| No | Rancangan awal (Bab 3) | Hasil akhir | Alasan |
|---|---|---|---|
| 1 | Beberapa halaman (Dashboard, Laporan, Status Mesin) direncanakan penuh | Menu masih berupa penanda "Belum tersedia" | Fokus Sprint 1–2 pada fitur inti Must Have; fitur tersebut masuk Sprint 3 |
| 2 | Akses Pengguna dan Teknisi disebut dalam PRD | Hanya Pemilik dan Admin/Operator yang diimplementasikan | Akses langsung pelanggan dan teknisi masih menunggu konfirmasi klien (PRD bagian Pertanyaan Terbuka) |
| 3 | Nama tabel `pengguna` dengan peran tersimpan terpisah | Tetap dipakai, ditambah `seed_peran()` untuk peran dasar | Diperlukan agar skrip pembuatan akun dapat memilih peran tanpa input manual ID |
| 4 | Validasi hanya disebut secara umum | Validasi dua lapis (HTML5 + server) dan token CSRF | Kebutuhan keamanan Jobsheet 11–12; uji keamanan ditambahkan |
| 5 | Atribut pelanggan belum dikonfirmasi | Hanya `nama_pelanggan` sesuai skema | Skema Jobsheet 6/7 tidak menyimpan kontak; tidak menambah kolom tanpa persetujuan perubahan skema |
| 6 | Pengujian direncanakan 3.6 tanpa target jumlah | 36 test case dan 60 uji otomatis | Jobsheet 13 menetapkan ≥ 20 test case dan uji regresi |
| 7 | Total biaya dicatat dari formulir | Dihitung otomatis dari berat × harga layanan | Menghindari ketidaksesuaian harga dengan data layanan yang berlaku |

Rencana pengujian 3.6 pada Bab 3 mencakup pengujian fungsional dan keamanan. Seluruh test case yang direncanakan untuk fitur yang sudah diimplementasikan telah dijalankan pada 4.4. Skenario untuk Dashboard, laporan, dan status mesin belum dijalankan karena fiturnya belum tersedia; hal ini dinyatakan terbuka pada 4.6 dan menjadi bagian dari Sprint 3.
