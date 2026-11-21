# PROSEDUR CADANGAN DAN PEMULIHAN

## Sistem Informasi Laundry Koin

### Pencadangan
- Frekuensi: harian setelah jam operasional tutup.
- Perintah: `python cadangkan.py`
- Hasil: `cadangan/laundry_koin-YYYYMMDD-HHMMSS.db` (folder tidak ikut Git).
- Penanggung jawab: Admin/Operator toko.

### Pemulihan
1. Hentikan aplikasi.
2. Salin berkas cadangan yang diinginkan ke lokasi `TOKO_DB` (menimpa berkas basis data aktif).
3. Jalankan kembali aplikasi.
4. Verifikasi data yang hilang sudah kembali.

### Bukti uji (Langkah 6)
```text
sebelum: [(1, 'Semen', 65000), (2, 'Paku', 20000)]
cadangan: laundry_koin-20261121-132825.db True
setelah hapus: [(1, 'Semen', 65000)]
setelah pulihkan: [(1, 'Semen', 65000), (2, 'Paku', 20000)]
```

Pemulihan berhasil; data yang dihapus kembali setelah cadangan disalin.
