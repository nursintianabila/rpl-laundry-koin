"""Uji regresi cepat Jobsheet 10/11.

Jalankan dari folder proyek:
    python tests/uji_cepat.py

Memakai basis data sementara, sehingga instance/laundry_koin.db tidak tersentuh.
"""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import models

models.DB_PATH = Path(tempfile.mkdtemp()) / "uji.db"
models.init_db()

import app as aplikasi

from services import auth_service
auth_service.buat_pengguna("pemilik@example.com", "pemilik123", "Pemilik")
auth_service.buat_pengguna("admin@example.com", "admin123", "Admin/Operator")

c = aplikasi.app.test_client()
c.post("/login", data={"username_email": "admin@example.com", "password": "admin123"})


def kirim(url, **data):
    return c.post(url, data=data, follow_redirects=True)


def ada(teks, hasil):
    assert teks in hasil.text, f"Tidak ditemukan: {teks!r}"


# data induk
with models.koneksi() as db:
    id_pel = db.execute("INSERT INTO pelanggan (nama_pelanggan) VALUES (?)", ("Pelanggan Uji",)).lastrowid
    id_lay = db.execute("INSERT INTO layanan (nama_layanan, harga) VALUES (?, ?)", ("Cuci Kering", 7000)).lastrowid

# --- modul transaksi ---
ada("Belum ada transaksi.", c.get("/transaksi"))
ada("Transaksi berhasil ditambahkan.", kirim(
    "/transaksi/tambah",
    id_pelanggan=id_pel,
    id_layanan=id_lay,
    tanggal="2026-11-21",
    berat="2.5",
))
assert len(models.semua_transaksi()) == 1
assert models.semua_transaksi()[0]["total_biaya"] == 17500

# validasi
ada("Pilih pelanggan.", kirim("/transaksi/tambah", id_pelanggan="", id_layanan=id_lay, tanggal="2026-11-21", berat="1"))
ada("Layanan tidak ditemukan.", kirim("/transaksi/tambah", id_pelanggan=id_pel, id_layanan=999, tanggal="2026-11-21", berat="1"))
ada("Berat harus lebih dari 0.", kirim("/transaksi/tambah", id_pelanggan=id_pel, id_layanan=id_lay, tanggal="2026-11-21", berat="0"))
ada("Tanggal harus berformat TTTT-BB-HH.", kirim("/transaksi/tambah", id_pelanggan=id_pel, id_layanan=id_lay, tanggal="21-11-2026", berat="1"))

# pencarian
ada("Pelanggan Uji", c.get("/transaksi?q=Pelanggan"))
ada("Tidak ada transaksi yang cocok.", c.get("/transaksi?q=zzzz"))
ada("Tidak ada transaksi yang cocok.", c.get("/transaksi?q=%25"))

# hapus
transaksi_id = models.semua_transaksi()[0]["id_transaksi"]
ada("Transaksi berhasil dihapus.", kirim(f"/transaksi/{transaksi_id}/hapus"))
assert models.ambil_transaksi(transaksi_id) is None

# kunci asing: hapus pelanggan/layanan yang dipakai transaksi
transaksi_id = models.tambah_transaksi(id_pel, id_lay, "2026-11-21", 1.0, 7000)
r = kirim(f"/pelanggan/{id_pel}/hapus")
ada("masih dipakai pada transaksi", r)
r = kirim(f"/layanan/{id_lay}/hapus")
ada("masih dipakai pada transaksi", r)


# --- autentikasi dan otorisasi (Jobsheet 11) ---
c_tamu = aplikasi.app.test_client()
r = c_tamu.get("/layanan")
assert r.status_code == 302 and "/login" in r.headers.get("Location", ""), "tamu harus dialihkan ke login"

r = c_tamu.post("/login", data={"username_email": "admin@example.com", "password": "salah"}, follow_redirects=True)
assert "Nama pengguna atau kata sandi salah." in r.text
r = c_tamu.post("/login", data={"username_email": "tidakada@example.com", "password": "x"}, follow_redirects=True)
assert "Nama pengguna atau kata sandi salah." in r.text

r = c_tamu.post("/login?next=https://jahat.example", data={"username_email": "admin@example.com", "password": "admin123"})
assert r.headers.get("Location", "").endswith("/transaksi") or r.headers.get("Location", "").endswith("/layanan"), "next luar situs harus diabaikan"

# kata sandi tersimpan sebagai hash
with models.koneksi() as db:
    baris = db.execute("SELECT password_hash FROM pengguna WHERE username_email = ?", ("admin@example.com",)).fetchone()
assert baris["password_hash"].startswith(("scrypt:", "pbkdf2:")), "kata sandi harus tersimpan sebagai hash"

# peran terbatas (pemilik) mendapat 403 pada halaman dan POST terlarang
c_pemilik = aplikasi.app.test_client()
c_pemilik.post("/login", data={"username_email": "pemilik@example.com", "password": "pemilik123"})
r = c_pemilik.get("/pelanggan")
assert r.status_code == 403, "pemilik tidak boleh membuka data pelanggan"
r = c_pemilik.post("/pelanggan/1/hapus")
assert r.status_code == 403, "pemilik tidak boleh menghapus pelanggan lewat POST"

# peran penuh (admin) berhasil
c_admin = aplikasi.app.test_client()
c_admin.post("/login", data={"username_email": "admin@example.com", "password": "admin123"})
r = c_admin.get("/pelanggan")
assert r.status_code == 200, "admin boleh membuka data pelanggan"

print("SEMUA UJI LULUS")
