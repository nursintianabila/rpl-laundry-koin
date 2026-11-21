# LAPORAN CACAT

## Sistem Informasi Laundry Koin

### D-01 Tanggal tanpa tanda hubung diterima

- Ditemukan : 21 November 2026 oleh Nur Sintia Nabila lewat TC-22 / uji eksploratif
- Langkah   : 1) Buka /transaksi/tambah. 2) Isi tanggal "20261108". 3) Kirim.
- Aktual    : Diterima dan tersimpan; format di PRD adalah TTTT-BB-HH.
- Diharapkan: Ditolak dengan pesan format tanggal.
- Keparahan : Rendah (data tetap sah, tetapi format tidak konsisten)
- Prioritas : Nanti
- Penyebab  : `date.fromisoformat` Python 3.11+ menerima format ISO tanpa tanda hubung.
- Perbaikan : pemeriksaan regex `[0-9]{4}-[0-9]{2}-[0-9]{2}` sebelum `fromisoformat`; uji TC-23.
- Status    : Diperbaiki (commit perbaikan)

### D-02 Angka Unicode pada harga menyebabkan galat 500

- Ditemukan : 21 November 2026 lewat uji eksploratif
- Langkah   : POST /layanan/tambah dengan harga_jual = "²"
- Aktual    : `ValueError: invalid literal for int() with base 10: '²'` -> halaman galat 500
- Diharapkan: ditolak dengan pesan "Harga harus berupa angka..."
- Keparahan : Sedang
- Prioritas : Sprint ini
- Penyebab  : `str.isdigit()` bernilai True untuk '²' tetapi `int()` tidak dapat mengubahnya.
- Perbaikan : `isascii() and isdigit()` pada `_bilangan` (jika diterapkan); uji tambahan.
- Status    : Diperbaiki (commit perbaikan)
