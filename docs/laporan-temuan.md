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

### T-01 SQL injection pada login
- Lokasi   : kasus_rentan.py rute /login (nomor 4)
- Kategori : A05 Injection
- Deskripsi: nama pengguna disambung langsung ke teks SQL, sehingga masukan ' OR 1=1 -- membuat kondisi selalu benar.
- Bukti    : POST /login dengan username ' OR 1=1 -- dan kata sandi sembarang menghasilkan 302 ke / (login berhasil).
- Dampak   : masuk tanpa kata sandi, bahkan mengubah/menghapus data.
- Risiko   : Tinggi
- Perbaikan: query berparameter WHERE username = ? AND password_hash = ?.
- Status   : Terbuka

### T-02 Hapus data lewat GET tanpa login
- Lokasi   : kasus_rentan.py rute /barang/<id>/hapus (nomor 7)
- Kategori : A01 Broken Access Control
- Deskripsi: penghapusan dilakukan lewat GET dan tanpa pemeriksaan sesi/peran.
- Bukti    : GET /barang/1/hapus tanpa login menghapus baris dan mengalihkan ke /barang.
- Dampak   : siapa pun (atau tautan di halaman lain) dapat menghapus data.
- Risiko   : Tinggi
- Perbaikan: POST + decorator peran + token CSRF.
- Status   : Terbuka

### T-03 Kata sandi di-hash dengan MD5 tanpa garam
- Lokasi   : kasus_rentan.py nomor (3)
- Kategori : A04 Cryptographic Failures
- Deskripsi: MD5 tanpa garam cepat dihitung; hash yang sama untuk kata sandi yang sama.
- Bukti    : md5('sandi-karangan-1') selalu menghasilkan nilai yang sama pada setiap pengguna.
- Dampak   : bila basis data bocor, banyak kata sandi dipulihkan dengan cepat.
- Risiko   : Tinggi
- Perbaikan: generate_password_hash / check_password_hash (Werkzeug).
- Status   : Terbuka

### T-04 Catatan dapat dibaca pengguna lain (IDOR)
- Lokasi   : kasus_rentan.py rute /catatan/<id> (nomor 8)
- Kategori : A01 Broken Access Control
- Deskripsi: catatan diambil berdasarkan ID tanpa cek kepemilikan.
- Bukti    : masuk sebagai kasir lalu GET /catatan/1 mengembalikan catatan milik pemilik.
- Dampak   : pengguna membaca data milik orang lain.
- Risiko   : Tinggi
- Perbaikan: tambahkan kondisi pengguna_id = sesi pada query.
- Status   : Terbuka

### T-05 Kunci rahasia dan debug mode terbuka
- Lokasi   : kasus_rentan.py nomor (2) dan (10)
- Kategori : A04 Cryptographic Failures / A02 Security Misconfiguration
- Deskripsi: secret_key ditulis di kode dan aplikasi berjalan dengan debug=True pada host 0.0.0.0.
- Bukti    : kode memuat app.secret_key = 'rahasia123' dan app.run(host='0.0.0.0', debug=True).
- Dampak   : sesi dapat dipalsukan; debugger terbuka ke jaringan.
- Risiko   : Tinggi
- Perbaikan: secret_key dari lingkungan; debug hanya bila diminta; host 127.0.0.1 pada pengembangan.
- Status   : Terbuka


## Langkah 6 — Perbaikan kasus dengan bantuan AI

Temuan diperbaiki satu per satu (bukan sekaligus), lalu ditinjau:
- T-01 SQL injection: AI mengusulkan query berparameter; perbaikan diterima (Terima).
- T-02 Hapus via GET: AI mengusulkan POST + decorator peran + CSRF; perbaikan diterima (Terima).
- T-03 MD5: AI mengusulkan Werkzeug hash; perbaikan diterima (Terima).
- T-04 IDOR: AI mengusulkan filter kepemilikan; perbaikan diterima (Terima).
- T-05 Kunci rahasia/debug: AI mengusulkan baca dari lingkungan dan nonaktifkan debug; perbaikan diterima (Terima).

Catatan kualitas AI: AI memperbaiki penyebab (bukan hanya gejala) untuk T-01/T-03/T-04. Untuk T-02, AI menambahkan CSRF yang belum diminta; bagian itu ditunda ke Langkah 11. Tidak ditemukan kelemahan baru pada perbaikan.

## Langkah 7 — Tinjauan kode proyek sendiri

Hasil tinjauan mandiri (>= 5 temuan) tercatat pada docs/temuan-keamanan.md (6 temuan: batas percobaan login, CSRF, cookie Secure, next aman, hash, peran). Temuan tersebut digabungkan dengan laporan ini.
