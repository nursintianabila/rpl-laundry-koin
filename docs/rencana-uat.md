# RENCANA UAT — SISTEM INFORMASI LAUNDRY KOIN

## Jobsheet 13 Langkah 13

- Tujuan      : memastikan pengguna dapat memakai aplikasi untuk pencatatan transaksi laundry
- Peserta     : Pemilik dan Admin/Operator (akun uji); pengamat: Nur Sintia Nabila
- Tanggal     : Minggu 14 (sesuai jadwal dosen)
- Tempat      : Laboratorium Komputer Prodi D3 TI Politeknik Sampit
- Durasi      : 30 menit
- Lingkungan  : aplikasi lokal; data karangan; akun uji pemilik dan admin
- Kriteria lulus: semua skenario inti lulus; tidak ada cacat Kritis/Tinggi terbuka

| ID | KF | Skenario (bahasa klien) | Langkah | Hasil diharapkan | Lulus? | Catatan |
|---|---|---|---|---|---|---|
| UAT-1 | KF-02 | Melihat daftar layanan dan harga | 1) Buka menu Layanan | Daftar layanan tampil dengan harga |  |  |
| UAT-2 | KF-02 | Menambah layanan baru | 1) Klik Tambah 2) Isi nama dan harga 3) Simpan | Layanan tersimpan dan tampil |  |  |
| UAT-3 | KF-03 | Menambah data pelanggan | 1) Buka Data Pelanggan 2) Tambah | Pelanggan tersimpan |  |  |
| UAT-4 | KF-04 | Mencatat transaksi | 1) Buka Transaksi 2) Tambah 3) Pilih pelanggan & layanan, isi berat, tanggal 4) Simpan | Transaksi tersimpan, total dihitung |  |  |
| UAT-5 | KF-05 | Mencari transaksi | 1) Ketik nama pelanggan 2) Cari | Transaksi cocok tampil |  |  |
| UAT-6 | KF-01 | Login sebagai Pemilik | 1) Masuk dengan akun pemilik | Menu sesuai peran |  |  |
| UAT-7 | KF-01 | Login sebagai Admin | 1) Masuk dengan akun admin | Menu sesuai peran |  |  |
| UAT-8 | KQ-02 | Validasi isian kosong | 1) Kirim form kosong | Pesan galat, isian tetap |  |  |

Cara merekam temuan: lembar ini diisi pengamat; temuan dipindah ke laporan-cacat.md.
