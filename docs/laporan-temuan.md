# LAPORAN TEMUAN

## Sistem Informasi Laundry Koin

### 1. Peta OWASP Top 10:2025 yang diprediksi paling mungkin ada (Jobsheet 12 Langkah 2)

Tiga kategori yang diprediksi paling mungkin ada pada proyek:
1. **A01 Broken Access Control** — pembatasan peran dan hapus lewat GET.
2. **A05 Injection** — query yang dirakit dari masukan pengguna.
3. **A04 Cryptographic Failures** — penyimpanan kata sandi dan kunci rahasia.

### 2. Latihan Tinjauan: kasus_rentan.py (Langkah 3)

| No | Masalah | Kategori OWASP | Dampak | Risiko |
|---|---|---|---|---|
| (1) | Memakai modul fiktif `flask_auth_helperz` alih-alih paket resmi. | A03 Supply Chain Failures | Kode tidak dapat dijalankan/diaudit; potensi kode berbahaya. | Sedang |
| (2) | `secret_key` ditulis langsung di kode ("rahasia123"). | A04 Cryptographic Failures | Sesi dapat dipalsukan bila kode bocor. | Tinggi |
| (3) | Kata sandi di-hash dengan MD5 tanpa garam. | A04 Cryptographic Failures | Hash cepat dihitung; banyak kata sandi dipulihkan bila basis data bocor. | Tinggi |
| (4) | Query SQL dirakit dengan f-string dari masukan pengguna. | A05 Injection | Injeksi SQL: login tanpa kata sandi, perubahan/hapus data. | Tinggi |
| (5) | Pesan galat membocorkan nama pengguna ("Kata sandi salah untuk pengguna X"). | A07 Identification and Authentication Failures | Enumerasi nama pengguna. | Rendah-Sedang |
| (6) | `redirect(request.args["next"])` tanpa validasi. | A01 Broken Access Control (Open Redirect) | Pengguna dialihkan ke situs luar (phishing). | Sedang |
| (7) | Hapus data lewat GET tanpa pemeriksaan login/CSRF. | A01 Broken Access Control | Siapa pun dapat menghapus data; tautan di halaman lain dapat memicunya. | Tinggi |
| (8) | Catatan diambil berdasarkan ID tanpa cek kepemilikan (IDOR). | A01 Broken Access Control | Pengguna membaca catatan milik orang lain. | Tinggi |
| (9) | Pesan galat membocorkan rincian internal (`f"Galat: {e!r}"`). | A10 Mishandling of Exceptional Conditions | Membantu penyerang memetakan struktur basis data. | Rendah-Sedang |
| (10) | `debug=True` dan `host="0.0.0.0"`. | A02 Security Misconfiguration | Debugger terbuka ke jaringan; kebocoran kode dan eksekusi kode. | Tinggi |

### 3. Lima Temuan Terpenting (format Lampiran D.1) — diurutkan dari risiko tertinggi
*(diisi lengkap pada Langkah 5 dengan bukti)*
