# MATRIKS AKSES — SISTEM INFORMASI LAUNDRY KOIN

## Jobsheet 11 Langkah 2

| Halaman / aksi | Tamu | Pemilik | Admin/Operator |
|---|---|---|---|
| Halaman login | ✓ | ✓ | ✓ |
| Daftar transaksi | login | ✓ | ✓ |
| Tambah transaksi | login | ✗ | ✓ |
| Ubah transaksi | login | ✗ | ✓ |
| Hapus transaksi | login | ✗ | ✓ |
| Daftar layanan | login | ✓ | ✓ |
| Tambah layanan | login | ✓ | ✗ |
| Ubah layanan | login | ✓ | ✗ |
| Hapus layanan | login | ✗ | ✓ (hanya jika tidak dipakai transaksi) |
| Daftar pelanggan | login | ✗ | ✓ |
| Tambah pelanggan | login | ✗ | ✓ |
| Ubah pelanggan | login | ✗ | ✓ |
| Hapus pelanggan | login | ✗ | ✓ (hanya jika tidak dipakai transaksi) |
| Logout (POST) | login | ✓ | ✓ |

Keterangan: ✓ = diizinkan, ✗ = ditolak (403), login = harus masuk lebih dulu.

## Fitur Kecil

| No | Fitur kecil | Kriteria penerimaan | Pelaksana |
|---|---|---|---|
| H1 | Akun awal dan hash | Kata sandi tersimpan sebagai hash; tidak ada kata sandi di kode | Nur Sintia Nabila |
| H2 | Login dan logout | Kredensial salah: pesan sama; sukses: sesi dibuat; logout lewat POST; `next` aman | Nur Sintia Nabila |
| H3 | Pembatasan peran | Tamu ke login; peran salah 403; berlaku juga untuk POST | Nur Sintia Nabila |
| H4 | Antarmuka sesuai wireframe | Menu menurut peran; gaya konsisten; pesan sukses dan galat | Nur Sintia Nabila |
| H5 | Validasi dua lapis | Atribut HTML5 + validasi server; isian dipertahankan | Nur Sintia Nabila |

Proyek dikerjakan secara individu atas persetujuan dosen.
