# DAFTAR PUSTAKA

## Sistem Informasi Laundry Koin

1. Brooke, J. (1996). SUS: A "quick and dirty" usability scale. Dalam P. W. Jordan, B. Thomas, B. A. Weerdmeester, & I. L. McClelland (Eds.), *Usability Evaluation in Industry*. London: Taylor & Francis.
2. Chacon, S., & Straub, B. (2014). *Pro Git* (2nd ed.). Berkeley: Apress. https://git-scm.com/book
3. OWASP Foundation. (2025). *OWASP Top 10:2025*. https://owasp.org/www-project-top-ten/
4. Pallets Projects. (2026). *Flask Documentation*. https://flask.palletsprojects.com/
5. Sommerville, I. (2016). *Software Engineering* (10th ed.). Harlow: Pearson.
6. SQLite. (n.d.). *SQLite Documentation*. https://www.sqlite.org/docs.html
7. Politeknik Sampit. *Pedoman Penulisan Tugas Akhir*. (format sitasi mengikuti pedoman fakultas).

## Pemetaan klaim ke sumber

| Klaim pada laporan | Sumber |
|---|---|
| Kategori OWASP A01–A10 pada temuan keamanan | OWASP Top 10:2025 [3] |
| Cara menghitung skor SUS (butir ganjil/genap) | Brooke (1996) [1] |
| Pengertian semantic versioning MAJOR.MINOR.PATCH | Konvensi rilis yang tercantum pada `versi.py`; rujukan umum [3] tidak dipakai untuk definisi ini |
| Arsitektur berlapis Routes–Services–Models | Sommerville (2016) [5] dan `docs/desain/arsitektur.md` |
| Perilaku sesi Flask, `session.clear()`, dan `secret_key` | Flask Documentation [4] |
| API `sqlite3.Connection.backup` untuk cadangan | SQLite Documentation [6] |
| Alur branch, commit, dan Pull Request | Chacon & Straub (2014) [2] |

Semua klaim bahwa aplikasi berjalan, uji lulus, dan cadangan berhasil bersumber dari bukti lokal pada repositori, bukan dari literatur eksternal.
