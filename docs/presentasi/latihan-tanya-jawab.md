# LATIHAN TANYA JAWAB TANPA AI

## Bank pertanyaan penjelasan

1. Mengapa `models.py` menjadi satu-satunya tempat akses basis data? Apa yang terjadi bila `app.py` langsung memanggil SQL?
2. Tunjukkan di mana pemeriksaan peran dilakukan. Apa yang terjadi bila dekorator pada rute hapus layanan dihapus dan uji mana yang gagal?
3. Mengapa transaksi disimpan dalam satu koneksi dan satu commit?
4. Apa fungsi `csrf_token()` dan di mana ia diperiksa? Apa yang terjadi pada POST tanpa token?
5. Mengapa pesan login salah sama untuk pengguna yang tidak ada dan kata sandi yang salah?
6. Jelaskan satu uji pada `tests/test_draf_ai.py`: apa kasus batasnya dan mengapa dipilih?

## Bank tugas modifikasi (≤ 10 menit, tanpa AI)

1. Ubah batas percobaan login dari 5 menjadi 3. Uji memakai konstanta yang sama sehingga tetap lulus; pesan dan README ikut diperbarui.
2. Tambahkan aturan nama layanan minimal 3 karakter. Validasi di service, pesan galat, dan uji batas panjang 2 dan 3.
3. Ubah pesan flash hapus transaksi, lalu perbarui uji yang mencocokkan teksnya.

## Daftar belajar pribadi

- [ ] Jelaskan alur `before_request` untuk memuat pengguna dan pengecekan CSRF tanpa melihat kode.
- [ ] Latih menjawab enam pertanyaan di atas dalam ≤ 1 menit tanpa membuka dokumentasi.
- [ ] Selesaikan satu tugas modifikasi tanpa AI dan jalankan seluruh uji.
