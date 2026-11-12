\# VERIFIKASI DRAF ACTIVITY DIAGRAM AI



\## Sistem Informasi Laundry Koin



\### 1. Tujuan Verifikasi



Verifikasi dilakukan untuk memeriksa kesesuaian draf Activity Diagram yang dibuat dengan bantuan AI terhadap skenario use case pada Sistem Informasi Laundry Koin.



Pemeriksaan meliputi kesesuaian aktivitas, aktor, alur utama, alur alternatif, keputusan, pengecualian, dan alur akhir.



\### 2. Hasil Verifikasi UC-06 — Mengelola Layanan dan Harga



\*\*File:\*\* `activity-02-layanan.mmd`



\*\*Hasil pemeriksaan:\*\*



1\. Aktor Pemilik sudah sesuai dengan skenario.

2\. Aktivitas tambah layanan sudah mencakup pengisian nama layanan dan harga.

3\. Validasi data sudah digambarkan dengan keputusan valid atau tidak valid.

4\. Alur ubah dan hapus layanan sudah dibedakan.

5\. Pengecualian penyimpanan gagal sudah digambarkan.

6\. Hasil penyimpanan berhasil ditampilkan sebagai data layanan terbaru.

7\. Semua jalur proses berakhir pada simpul Selesai.



\*\*Asumsi yang digunakan:\*\*



1\. Pilihan tambah, ubah, dan hapus digambarkan sebagai percabangan fungsi.

2\. Validasi data ditampilkan secara eksplisit pada proses tambah layanan.

3\. Proses ubah dan hapus menggunakan pemeriksaan keberhasilan penyimpanan yang sama.

4\. Konfirmasi penghapusan tidak ditambahkan karena tidak tercantum dalam skenario.



\*\*Kesimpulan:\*\* Draf telah diperbaiki dan dinilai sesuai dengan alur skenario UC-06.



\### 3. Hasil Verifikasi UC-09 — Mengelola Transaksi



\*\*File:\*\* `activity-03-transaksi.mmd`



\*\*Hasil pemeriksaan:\*\*



1\. Aktor Admin/Operator sudah sesuai dengan skenario.

2\. Pencatatan transaksi baru mencakup pemilihan pelanggan dan layanan.

3\. Pengisian tanggal dan data wajib transaksi sudah digambarkan.

4\. Perhitungan total biaya sudah dicantumkan.

5\. Validasi data transaksi dilakukan sebelum penyimpanan.

6\. Perubahan transaksi sudah dilengkapi pemeriksaan hak akses.

7\. Pencarian riwayat mencakup keputusan transaksi ditemukan atau tidak ditemukan.

8\. Semua jalur proses berakhir pada simpul Selesai.



\*\*Asumsi yang digunakan:\*\*



1\. Keputusan pencatatan transaksi baru membedakan alur utama dengan pengelolaan transaksi tersimpan.

2\. Pemeriksaan pelanggan dan layanan digambarkan sebagai keputusan tersendiri.

3\. Pencarian riwayat digambarkan setelah proses perubahan transaksi mengikuti urutan alur alternatif pada skenario.

4\. Kegagalan penyimpanan perubahan transaksi tidak ditambahkan karena tidak dijelaskan secara khusus dalam skenario.



\*\*Kesimpulan:\*\* Draf telah diperbaiki dan dinilai sesuai dengan alur skenario UC-09.



\### 4. Perbaikan yang Dilakukan



1\. Memperjelas percabangan tambah, ubah, dan hapus pada UC-06.

2\. Menambahkan pemeriksaan keberhasilan penyimpanan pada UC-06.

3\. Memisahkan proses pencatatan transaksi baru dan pengelolaan transaksi tersimpan pada UC-09.

4\. Memperjelas pemeriksaan hak akses perubahan transaksi.

5\. Menyesuaikan urutan pencarian riwayat dengan skenario UC-09.



\### 5. Kesimpulan Akhir



Draf Activity Diagram yang dihasilkan dengan bantuan AI telah diperiksa dan diperbaiki berdasarkan skenario use case. Diagram digunakan sebagai dokumentasi proses sistem dan tetap mengacu pada kebutuhan yang telah ditetapkan dalam dokumen SRS dan PRD.

