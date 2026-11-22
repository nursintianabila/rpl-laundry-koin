# DRAF PRESENTASI UAS — PROSES SDLC PADA SISTEM INFORMASI LAUNDRY KOIN

Nama: Nur Sintia Nabila  
Mata kuliah: Rekayasa Perangkat Lunak  
Durasi: ±20 menit presentasi + demo, dilanjutkan tanya jawab  
Proyek: Sistem Informasi Laundry Koin v1.0.0 (tag `v1.0.0`)

---

## Pembuka (0:00–2:00)

"Assalamualaikum. Saya akan mempresentasikan proyek akhir Sistem Informasi Laundry Koin. Aplikasi ini membantu laundry koin mengelola layanan dan harga, data pelanggan, pencatatan transaksi, riwayat transaksi, laporan pendapatan, dan status mesin. Proyek ini dikerjakan secara individu atas persetujuan dosen, sehingga satu orang berperan sebagai Product Owner, Scrum Master, sekaligus Developer. Saya akan menjelaskan tahapan SDLC, model proses yang dipakai, posisi vibe coding, lalu mendemokan aplikasi."

Bukti singkat: `README.md`, `docs/manual-pengguna.md`, `CHANGELOG.md`.

---

## 1. Tahapan SDLC pada proyek (2:00–7:00)

### 1.1 Elisitasi kebutuhan
Yang saya lakukan: menyusun pedoman wawancara, simulasi catatan wawancara, user story, dan validasi diagram bersama klien/pengguna. Kebutuhan dibatasi hanya yang benar-benar dipakai laundry.

Bukti:
- `docs/elisitasi/pedoman-wawancara.md`
- `docs/elisitasi/catatanwawancara.md`
- `docs/elisitasi/user-story.md`
- `docs/elisitasi/validasi-diagram.md`
- Commit awal: `15a4728`, `c85b99e`

Contoh penjelasan: "Dari wawancara didapat bahwa yang paling dibutuhkan adalah pencatatan transaksi dan harga layanan. Akses langsung pelanggan dan teknisi masih ditunda karena belum dikonfirmasi klien; ini tercatat sebagai pertanyaan terbuka di PRD."

### 1.2 SRS / PRD
Yang saya lakukan: menyusun SRS ringkas, PRD dengan prioritas MoSCoW, dan product backlog sebagai dasar sprint.

Bukti:
- `docs/srs.md`
- `PRD.md`
- `docs/product-backlog.md`
- Commit: `98f75a8`, `ae74721`

Contoh: "Fitur Must Have adalah login, pengelolaan layanan, pelanggan, pencatatan transaksi, dan riwayat transaksi. Dashboard, laporan, dan filter periode masuk Should Have. Status mesin sempat masuk Should, lalu direalisasikan setelah perbaikan routes."

### 1.3 Perancangan
Yang saya lakukan: membuat UML use case dan activity diagram, ERD, normalisasi, kamus data, skema SQL, arsitektur berlapis, serta sembilan wireframe antarmuka.

Bukti:
- `docs/uml/use-case.mmd`, `docs/uml/daftar-aktor.md`, `docs/uml/daftar-use-case.md`
- `docs/uml/activity/*.mmd`
- `docs/desain/erd_1.mmd`, `docs/desain/relasi-entitas.md`, `docs/desain/normalisasi.md`, `docs/desain/kamus-data.md`, `docs/desain/schema.sql`
- `docs/desain/arsitektur.md`
- `docs/desain/wireframe/01-login.md` sampai `09-status-mesin.md`
- Commit: `4397091`, `99add6c`, `53e9975`, `c08767d`

Contoh: "Arsitektur dipilih berlapis: Routes → Services → Models → Database, dan Views berupa templat. Aturan ini tertulis di `aturan-proyek.md`: hanya `models.py` yang boleh menjalankan SQL."

### 1.4 Implementasi
Yang saya lakukan: membangun aplikasi Flask + SQLite bertahap, satu fitur per commit.

Bukti:
- Kode: `app.py`, `models.py`, `routes/`, `services/`, `templates/`, `static/css/style.css`
- CRUD Layanan: commit `9944121`, `c9fb893`, `8332fe4`, `a5e157c`, `5cba1f9`
- CRUD Pelanggan: `ed72a63`
- Modul transaksi + JOIN + pencarian: `b7c1d70`, `0b8b98a`, `5df1776`
- Autentikasi & otorisasi: `eb6dbbb`, `1c08b83`
- Perbaikan peran & modul lanjutan: `81b52dd`, `7dfa1d4`
- Autocomplete pelanggan: `89f74f9`
- Status selesai & notifikasi: `feea303`
- Ekspor laporan CSV/PDF: `79fa925`

Contoh: "Setiap fitur melewati siklus kecil: prompt → generate → jalankan → tinjau → commit. Misalnya tombol 'Tandai Selesai' menambah kolom `status_transaksi` beserta migrasi otomatis untuk database lama."

### 1.5 Pengujian
Yang saya lakukan: menyusun 36 test case, uji otomatis dengan unittest dan pytest, uji keamanan, mutasi, debugging, dan UAT.

Bukti:
- `docs/pengujian/test-case.md`, `docs/matriks-keterlacakan.md`
- `tests/uji_cepat.py`, `tests/test_layanan.py`, `tests/test_pelanggan.py`, `tests/test_transaksi.py`, `tests/test_draf_ai.py`, `tests/test_rilis.py`, `tests/test_modul_lanjutan.py`, `tests/test_peran_menu.py`, `tests/test_autocomplete_pelanggan.py`, `tests/test_notifikasi_selesai.py`, `tests/test_ekspor_transaksi.py`
- `docs/pengujian/catatan-debugging.md`, `docs/laporan-cacat.md`
- `docs/uat/`, `docs/rencana-uat.md`
- Hasil terakhir: **74 unittest lulus, 86 pytest lulus, `uji_cepat` SEMUA UJI LULUS**, `cek_skema` 6 penolakan / 0 gagal.

Contoh: "Dua cacat nyata ditemukan: tanggal `20261108` diterima padahal format harus `YYYY-MM-DD`, dan angka Unicode `²` menyebabkan 500. Keduanya diperbaiki dan dibuktikan dengan uji regresi."

### 1.6 Rilis dan UAT
Yang saya lakukan: menyiapkan konfigurasi produksi, Waitress, cadangan, README, manual pengguna, serta rencana dan lembar UAT.

Bukti:
- Tag `v1.0.0`, `CHANGELOG.md`, `versi.py`
- `docs/deployment.md`, `docs/cadangan.md`, `docs/audit-rilis.md`
- `README.md`, `docs/manual-pengguna.md`
- `docs/uat/form-sus.md`, `docs/uat/lembar-skenario.md`, `docs/uat/hasil-uat.md`, `docs/uat/hitung_sus.py`
- Commit: `7581d3f`, `a74d935`, `4250187`, `518943e`

Contoh: "Aplikasi diuji berjalan dengan `APP_ENV=production` dan `SECRET_KEY`; tanpa kunci itu aplikasi menolak start. Cadangan dan pemulihan juga berhasil dibuktikan."

---

## 2. Model proses yang dipakai (7:00–10:00)

### Waterfall vs Agile
- **Waterfall**: tahap linear, satu tahap harus selesai sebelum tahap berikutnya, perubahan di akhir mahal. Cocok bila kebutuhan sangat stabil.
- **Agile**: iteratif dan inkremental, perubahan diterima, pengiriman kecil-kecil, umpan balik cepat. Cocok bila kebutuhan masih berkembang.

### Mengapa proyek ini lebih dekat ke iteratif/agile
- Tidak semua kebutuhan tahu di awal (akses pelanggan dan teknisi masih dikonfirmasi), jadi tidak bisa memakai waterfall yang kaku.
- Pekerjaan dibagi ke **Sprint 1–4** pada `docs/rencana-sprint.md`.
- Ada **product backlog** (`docs/product-backlog.md`), **checkpoint tiap jobsheet**, dan **PR per fitur**.
-Tiap fitur di-commit kecil dan dapat diuji sendiri, misalnya CRUD layanan dipecah menjadi lima commit.

### Konsep Scrum pada proyek individu
| Konsep Scrum | Penerapan pada proyek ini |
|---|---|
| Product Owner | Menentukan prioritas KF di `PRD.md` dan `product-backlog.md` |
| Scrum Master | Mengatur checkpoint, sprint, dan disiplin commit/PR |
| Developer | Menulis kode, pengujian, dan dokumentasi |
| Product Backlog | `docs/product-backlog.md`, diperbarui di `docs/rencana-sprint.md` |
| Sprint Backlog | Pembagian Sprint 1–3 pada backlog + target Minggu 10/12/14 |
| Increment | Setiap fitur yang lolos uji dan di-commit, misalnya modul transaksi lengkap |
| Daily/Sprint Review | Checkpoint tiap jobsheet dan gladi demo sebelum UAT |

"Walaupun individu, peran tetap saya sebutkan agar artefak Scrum tetap jelas dan dapat dipertanggungjawabkan."

---

## 3. Posisi vibe coding dalam SDLC (10:00–15:00)

### Di tahap mana AI dipakai
AI dipakai sebagai asisten, bukan pengambil keputusan, terutama pada:
- perancangan awal (draf use case, skema, wireframe),
- penulisan kode CRUD dan validasi,
- penyusunan test case dan draf uji pytest,
- perapian bahasa laporan, README, manual, dan salindia.

AI **tidak** dipakai untuk memutuskan kebutuhan, memilih arsitektur akhir, atau menerima kode tanpa tinjauan.

### Siklus enam langkah
1. **Spesifikasi** — menulis konteks dan batasan singkat, misalnya "SQL hanya di models.py, kunci dari environment".
2. **Prompt** — satu prompt untuk satu perubahan kecil.
3. **Generate** — AI menghasilkan kode/dokumen.
4. **Jalankan dan uji** — perintah dijalankan, hasil uji dilihat.
5. **Tinjau** — baca baris demi baris, bandingkan dengan skema/PRD.
6. **Commit dan catat** — commit bermakna + entri jurnal dengan keputusan Terima/Ubah/Tolak.

### Contoh entri jurnal (Nyata)
Dari `docs/jurnal-vibe-coding.md`, entri 8:

| No | Tujuan | Hasil AI | Keputusan | Alasan |
|---|---|---|---|---|
| 8 | [Galat: acuan-salah] `[Debug]` Perbaiki SyntaxError pada tes XSS | Nama fungsi pengujian memakai tanda hubung, padahal nama fungsi Python hanya boleh berisi huruf, angka, dan garis bawah | **Terima** | Tanda hubung diganti menjadi garis bawah (`ter_escape`); seluruh 18 pengujian lulus setelah perbaikan |

"Di sini AI menemukan penyebabnya setelah saya memberi traceback lengkap, kode terkait, dan langkah reproduksi. Saya menerima karena penjelasannya cocok dengan aturan penamaan Python dan langsung saya verifikasi dengan menjalankan ulang uji."

### Risiko dan cara mengendalikannya
| Risiko | Contoh pada proyek | Cara mengendalikan |
|---|---|---|
| Kode tidak dipahami | AI menghasilkan validasi di route, bukan di service | Tinjau baris demi baris; commit kecil; mampu menjelaskan alur tanpa melihat AI |
| Kerentanan | `secret_key` di kode, SQL dirakit, CSRF belum ada | Daftar periksa OWASP, query berparameter, token CSRF, batas login, hash kata sandi |
| Utang teknis | Fitur dashboard/laporan/status mesin sempat jadi placeholder | Dicatat di `docs/triase-temuan.md` dan `docs/rencana-sprint.md`, lalu direalisasikan bertahap |
| Uji lemah | Uji lulus walau kode salah | Mutasi tiga perubahan kode; semua menyebabkan uji gagal, jadi uji dianggap efektif |

Rekap jurnal terakhir: **30 entri**, 18 Terima (60,0%), 12 Ubah (40,0%), 0 Tolak, 13 entri bertag galat, 3 entri `[Debug]`. Saya tidak mengklaim angka ini sebagai tingkat keberhasilan AI; proporsi Terima yang tinggi bisa berarti tinjauan kurang teliti, sehingga setiap keputusan diberi alasan.

---

## 4. Demo aplikasi (15:00–19:00)

### Persiapan
```powershell
cd C:\Users\user\Documents\JOB-SHEET-BILA\rpl-laundry-koin
.\.venv\Scripts\activate
python app.py
```
Buka `http://127.0.0.1:5000`.

Data dummy sudah ada di database lokal: 4 layanan, 4 pelanggan, transaksi contoh, dan 4 mesin. Akun uji:
- Pemilik: `pemilik@example.com` / `pemilik123`
- Admin/Operator: `admin@example.com` / `admin123`

### Alur demo yang ditampilkan
1. **Tamu** membuka `/layanan` → dialihkan ke `/login?next=/layanan`.
2. **Pemilik** login → Dashboard (ringkasan) → Riwayat Transaksi → Layanan → Laporan → pilih periode → **Unduh CSV/PDF**.
3. **Admin/Operator** login → Dashboard ada notifikasi "selesai" → Transaksi → ketik `nur` pada kolom pelanggan → pilih saran → isi berat & tanggal → Simpan → **Tandai Selesai**.
4. Admin buka **Status Mesin**, ubah status → notifikasi muncul di Dashboard.
5. Tunjukkan 403 dengan mencoba membuka `/pelanggan` sebagai Pemilik.
6. Tunjukkan POST tanpa token CSRF ditolak 400 (bila perlu).

Cadangan: rekaman layar singkat, data dummy, dua akun uji, dan jangan tampilkan berkas konfigurasi/kunci rahasia.

---

## Penutup (19:00–20:00)

"Proyek ini membuktikan bahwa SDLC dapat dijalankan secara iteratif dengan artefak Scrum walaupun dikerjakan individu. Vibe coding mempercepat penulisan, tetapi nilainya ditentukan oleh tinjauan manusia: 12 dari 30 siklus diubah, dan semua perbaikan keamanan tidak lepas dari pemeriksaan manual dan uji pelanggaran. Aplikasi v1.0.0 siap didemokan, dengan sisa fitur yang jujur saya sebutkan sebagai calon v1.1."

---

## Lampiran: daftar bukti cepat

| Kategori | Bukti |
|---|---|
| Kebutuhan | `PRD.md`, `docs/srs.md`, `docs/elisitasi/`, `docs/product-backlog.md` |
| Rancangan | `docs/desain/`, `docs/uml/`, `docs/desain/schema.sql` |
| Implementasi | `app.py`, `models.py`, `routes/`, `services/`, `templates/` |
| Pengujian | `docs/pengujian/`, `tests/`, `docs/laporan-cacat.md` |
| Rilis | `CHANGELOG.md`, tag `v1.0.0`, `docs/audit-rilis.md`, `docs/deployment.md`, `docs/cadangan.md` |
| Dokumentasi | `README.md`, `docs/manual-pengguna.md`, `docs/laporan-akhir.docx/.pdf` |
| Jurnal & agil | `docs/jurnal-vibe-coding.md`, `docs/rencana-sprint.md`, `docs/uat/` |

Catatan perbaikan bahasa: beberapa kata dalam draf ini sengaja saya tulis dengan spasi agar mudah dibaca; silakan rapikan saat menyalin ke salindia atau laporan akhir.
