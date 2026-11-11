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

Struktur folder proyek yang digunakan:

```text
rpl-laundry-koin/
├── app.py
├── templates/
│   └── file HTML aplikasi
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── tests/
│   └── file pengujian otomatis
├── docs/
│   └── dokumentasi proyek
├── aturan-proyek.md
├── PRD.md
└── README.md
```

Keterangan:
- `app.py`: File utama untuk menjalankan aplikasi Flask.
- `templates/`: Menyimpan halaman HTML.
- `static/`: Menyimpan file CSS, JavaScript, dan gambar.
- `tests/`: Menyimpan file pengujian aplikasi.
- `docs/`: Menyimpan dokumentasi pengembangan proyek.

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

### 4. Larangan

- Tidak menambahkan paket atau library tanpa persetujuan.
- Tidak menyimpan password, API key, token, atau informasi rahasia lainnya secara langsung di dalam kode.
- Tidak mengubah berkas di luar ruang lingkup pekerjaan yang sedang dilakukan.
- Tidak menghapus atau melemahkan pengujian yang sudah tersedia hanya untuk membuat pengujian berhasil.
- Tidak menggunakan kode hasil AI tanpa memahami dan memeriksa fungsinya.
- Tidak mengumpulkan atau memasukkan data pribadi pengguna ke dalam dokumentasi tanpa kebutuhan dan izin yang sesuai.

### 5. Cara Menjalankan dan Menguji

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
