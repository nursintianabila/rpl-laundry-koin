# ATURAN PROYEK
## Sistem Informasi Laundry Koin

### 1. Stack Teknologi

Teknologi yang digunakan dalam pengembangan proyek:

- **Bahasa pemrograman:** Python 3.14 (minimal Python 3.10).
- **Framework backend:** Flask.
- **Database:** SQLite.
- **Paket tambahan:** Hanya boleh ditambahkan setelah mendapat persetujuan dosen atau pihak yang berwenang.

Penggunaan teknologi dan paket harus tetap sesuai dengan kebutuhan proyek serta kemampuan pengembang.

### 2. Struktur Folder

Struktur folder target proyek yang digunakan:

```text
rpl-laundry-koin/
|-- app.py
|-- models.py
|-- aturan-proyek.md
|-- PRD.md
|-- README.md
|-- routes/
|   |-- __init__.py
|   |-- auth_routes.py
|   |-- layanan_routes.py
|   |-- pelanggan_routes.py
|   |-- transaksi_routes.py
|   |-- laporan_routes.py
|-- services/
|   |-- auth_service.py
|   |-- layanan_service.py
|   |-- pelanggan_service.py
|   |-- transaksi_service.py
|   |-- laporan_service.py
|-- templates/
|   |-- base.html
|   |-- auth/
|   |-- layanan/
|   |-- pelanggan/
|   |-- transaksi/
|   |-- laporan/
|-- static/
|   |-- css/
|   |-- js/
|   |-- images/
|-- instance/
|   |-- laundry_koin.db
|-- tests/
|   |-- cek_skema.py
|   |-- test_models.py
|   |-- test_routes.py
|   |-- test_services.py
|-- docs/
    |-- desain/
    |-- elisitasi/
    |-- pengujian/
    |-- uml/
```

Keterangan:

- `app.py`: File utama untuk membuat dan menjalankan aplikasi Flask.
- `models.py`: Mengelola koneksi dan seluruh operasi database SQLite.
- `routes/`: Menangani URL dan permintaan pengguna.
- `services/`: Menyimpan logika bisnis dan validasi proses aplikasi.
- `templates/`: Menyimpan halaman HTML aplikasi.
- `static/`: Menyimpan file CSS, JavaScript, dan gambar.
- `instance/`: Menyimpan database SQLite aplikasi.
- `tests/`: Menyimpan file pengujian aplikasi.
- `docs/`: Menyimpan dokumentasi pengembangan proyek.

Struktur tersebut merupakan rancangan target dan akan diterapkan secara bertahap sesuai kebutuhan pengembangan.

### 3. Konvensi Pengembangan

- Komentar kode dan pesan antarmuka menggunakan Bahasa Indonesia.
- Nama variabel dan fungsi menggunakan nama yang jelas dan konsisten.
- Nama variabel dan fungsi menggunakan `snake_case`.
- Nama class menggunakan `PascalCase`.
- Setiap commit Git diusahakan hanya mencakup satu fitur atau satu perubahan yang saling berkaitan.
- Pesan commit harus menjelaskan perubahan yang dilakukan.
- Setiap perubahan diperiksa secara mandiri sebelum di-commit.
- Dokumentasi diperbarui apabila terdapat perubahan kebutuhan atau fitur.
- Penggunaan AI diperbolehkan sebagai alat bantu memahami materi, menyusun dokumentasi, dan membantu penulisan kode.
- Setiap hasil bantuan AI wajib diperiksa, dipahami, disesuaikan, dan diuji oleh pengembang. Pengembang tetap bertanggung jawab atas hasil akhir proyek.

### 4. Aturan Arsitektur dan Akses Database

- Pengembangan aplikasi menggunakan arsitektur berlapis yang terdiri dari Routes/Controller, Services/Logika Bisnis, Models, Database, dan Views.
- Routes bertugas menerima permintaan pengguna dan menghubungkan proses aplikasi.
- Services bertugas menjalankan logika bisnis dan validasi.
- Models bertugas mengelola seluruh operasi database.
- Views bertugas menampilkan informasi kepada pengguna melalui template HTML.
- **Hanya `models.py` yang diperbolehkan mengakses database SQLite secara langsung.**
- Routes dan Services tidak diperbolehkan membuka koneksi SQLite atau menjalankan perintah SQL secara langsung.
- Seluruh operasi CRUD harus dilakukan melalui fungsi pada `models.py`.

### 5. Aturan Database

- Struktur database harus mengikuti ERD, kamus data, dan skema SQL yang telah disepakati.
- File skema database berada di `docs/desain/schema.sql`.
- Database aplikasi disimpan di `instance/laundry_koin.db`.
- Setiap koneksi SQLite yang digunakan aplikasi harus mengaktifkan foreign key.
- Perubahan struktur database harus disesuaikan dengan dokumentasi desain database.
- File database hasil penggunaan aplikasi tidak menggantikan file skema SQL sebagai dokumentasi struktur database.

**Perintah untuk menerapkan skema database:**

Jalankan dari folder utama proyek setelah Python tersedia:

```powershell
python -c "import sqlite3, pathlib; pathlib.Path('instance').mkdir(exist_ok=True); db=sqlite3.connect('instance/laundry_koin.db'); db.execute('PRAGMA foreign_keys=ON'); db.executescript(pathlib.Path('docs/desain/schema.sql').read_text(encoding='utf-8')); db.close(); print('Skema database berhasil diterapkan.')"
```

Perintah tersebut membuat folder `instance` jika belum tersedia, membuat atau membuka database SQLite, kemudian menerapkan perintah SQL dari file skema.

### 6. Larangan

- Tidak menambahkan paket atau library tanpa persetujuan.
- Tidak menyimpan password, API key, token, atau informasi rahasia lainnya secara langsung di dalam kode.
- Tidak mengubah berkas di luar ruang lingkup pekerjaan yang sedang dilakukan.
- Tidak menghapus atau melemahkan pengujian yang sudah tersedia hanya untuk membuat pengujian berhasil.
- Tidak menggunakan kode hasil AI tanpa memahami dan memeriksa fungsinya.
- Tidak mengumpulkan atau memasukkan data pribadi pengguna ke dalam dokumentasi tanpa kebutuhan dan izin yang sesuai.
- Tidak mengakses database SQLite secara langsung dari Routes, Services, atau Views.

### 7. Cara Menjalankan dan Menguji

**Menjalankan aplikasi:**

1. Pastikan Python sudah terpasang.
2. Buka terminal pada folder utama proyek.
3. Aktifkan virtual environment jika digunakan.
4. Instal dependensi yang telah disetujui.
5. Jalankan aplikasi Flask dengan perintah:

```bash
python app.py
```

6. Buka alamat aplikasi yang ditampilkan pada terminal, umumnya `http://127.0.0.1:5000`.

**Menjalankan pengujian otomatis:**

Pengujian otomatis dilakukan menggunakan perintah berikut setelah berkas pengujian dan dependensi pengujian tersedia:

```bash
python -m unittest discover -s tests
```

Setiap fitur yang dikembangkan harus diperiksa agar berjalan sesuai kebutuhan dan kriteria penerimaan yang telah ditentukan.
