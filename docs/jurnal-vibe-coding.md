# JURNAL VIBE CODING

Nama: Nur Sintia Nabila  
NIM: (isi sesuai data akademik)  
Kelompok: Individu (proyek atas persetujuan dosen)

## Refleksi Penggunaan AI — Activity Diagram

Kesalahan AI yang paling sering ditemukan adalah ketidaksesuaian alur percabangan dan keputusan, sehingga diagram perlu diperiksa kembali berdasarkan skenario use case.

## Jurnal Jobsheet 9 — CRUD Layanan

| No | Tujuan | Prompt (ringkas) | Hasil AI | Keputusan | Alasan |
|---|---|---|---|---|---|
| 1 | Kerangka proyek Flask + SQLite | Konteks `aturan-proyek.md` dan `schema.sql`; buat `app.py`, `models.py`, `services/`, `routes/`, dan `templates/base.html`; kunci rahasia dari variabel lingkungan; SQL hanya di `models.py`. | Kerangka berjalan dan basis data terbentuk dari skema. Halaman `/layanan` masih placeholder dan daftar dependensi belum dicatat. | Ubah | `requirements.txt` dan spesifikasi fitur ditambahkan; route daftar disiapkan bertahap; kunci rahasia tetap diambil dari `SECRET_KEY`/nilai acak; SQL tetap hanya berada di `models.py`. |
| 2 | Halaman daftar layanan (F2) | Konteks wireframe 06 dan kamus data; buat route `/layanan`, ambil data melalui service/models, tampilkan kolom ID, nama, harga, aksi, format rupiah, dan keadaan "Belum ada data". | Tabel daftar tampil dari data SQLite dan format rupiah sesuai wireframe; tombol tambah serta kolom aksi belum berfungsi. | Ubah | Tombol tambah dinonaktifkan sampai F3 dibuat, kolom aksi diberi keterangan tahap berikutnya, dan empat data uji karangan ditambahkan langsung ke SQLite agar daftar tidak kosong. |
| 3 | Form tambah layanan dengan validasi (F3) | Buat form tambah layanan; validasi nama wajib, maksimal 100 karakter, harga bilangan bulat tidak negatif, dan nama tidak duplikat; pertahankan isian saat galat; gunakan Post–Redirect–Get. | Form dan validasi berjalan di lapisan service, tetapi alamat `action` form masih ditulis langsung ke endpoint tambah sehingga sulit dipakai ulang untuk form ubah. | Ubah | Alamat form diparameterkan, pesan galat dibuat spesifik per kolom, isian dipertahankan, nama duplikat diperiksa tanpa membedakan huruf besar/kecil, dan tujuh pengujian otomatis dijalankan sampai lulus. |
