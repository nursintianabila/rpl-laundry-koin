# JURNAL VIBE CODING

Nama: Nur Sintia Nabila  
NIM: (isi sesuai data akademik)  
Kelompok: Individu (proyek atas persetujuan dosen)

## Refleksi Penggunaan AI — Activity Diagram

Kesalahan AI yang paling sering ditemukan adalah ketidaksesuaian alur percabangan dan keputusan, sehingga diagram perlu diperiksa kembali berdasarkan skenario use case.

## Jurnal Jobsheet 9 — CRUD Layanan

| No | Tujuan | Prompt (ringkas) | Hasil AI | Keputusan | Alasan |
|---|---|---|---|---|---|
| 1 | Kerangka proyek Flask + SQLite | Konteks `aturan-proyek.md` dan `schema.sql`; buat `app.py`, `models.py`, `services/`, `routes/`, dan `templates/base.html`; kunci rahasia dari variabel lingkungan; SQL hanya di `models.py`. | Kerangka berjalan dan basis data terbentuk dari skema. Kunci rahasia sempat berpotensi ditulis langsung di kode, dan halaman `/layanan` masih berupa placeholder. | Ubah | Kunci rahasia dipindahkan ke `SECRET_KEY`/nilai acak; route dipisah menjadi blueprint; template dasar dan format rupiah disesuaikan dengan wireframe; SQL tetap hanya berada di `models.py`. |
