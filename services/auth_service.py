"""Logika autentikasi dan otorisasi dasar."""

import functools

from flask import abort, g, redirect, request, session, url_for

from werkzeug.security import check_password_hash, generate_password_hash

import models

BATAS_USERNAME = 100
BATAS_KATA_SANDI = 4  # minimal, disesuaikan kebutuhan


class ValidasiPenggunaError(ValueError):
    """Kesalahan validasi pembuatan akun."""

    def __init__(self, daftar_pesan):
        self.daftar_pesan = daftar_pesan
        super().__init__(" ".join(daftar_pesan))


def hash_kata_sandi(kata_sandi):
    """Menghasilkan hash kata sandi (scrypt/pbkdf2 dari Werkzeug)."""
    return generate_password_hash(kata_sandi)


def verifikasi_kata_sandi(hash_tersimpan, kata_sandi):
    """Memverifikasi kata sandi terhadap hash tersimpan."""
    if not hash_tersimpan:
        return False
    return check_password_hash(hash_tersimpan, kata_sandi)


def periksa_akun(username_email, kata_sandi, nama_peran):
    """Memvalidasi pembuatan akun dan mengembalikan (nilai, galat)."""
    galat = []
    username = (username_email or "").strip()
    sandi = kata_sandi or ""

    if not username:
        galat.append("Nama pengguna (email) wajib diisi.")
    elif len(username) > BATAS_USERNAME:
        galat.append(f"Nama pengguna maksimal {BATAS_USERNAME} karakter.")

    if not sandi:
        galat.append("Kata sandi wajib diisi.")
    elif len(sandi) < BATAS_KATA_SANDI:
        galat.append(f"Kata sandi minimal {BATAS_KATA_SANDI} karakter.")

    peran = models.ambil_peran_by_nama(nama_peran)
    if peran is None:
        galat.append("Peran tidak dikenal.")

    if username and models.ambil_pengguna_by_username(username) is not None:
        galat.append("Nama pengguna sudah terdaftar.")

    nilai = {"username_email": username, "kata_sandi": sandi, "id_peran": peran["id_peran"] if peran else None}
    return nilai, galat


def buat_pengguna(username_email, kata_sandi, nama_peran):
    """Membuat akun baru setelah validasi."""
    nilai, galat = periksa_akun(username_email, kata_sandi, nama_peran)
    if galat:
        raise ValidasiPenggunaError(galat)
    hash_sandi = hash_kata_sandi(nilai["kata_sandi"])
    return models.tambah_pengguna(nilai["username_email"], hash_sandi, nilai["id_peran"])


def autentikasi(username_email, kata_sandi):
    """Mengembalikan baris pengguna bila kredensial benar, selain itu None."""
    pengguna = models.ambil_pengguna_by_username((username_email or "").strip())
    if pengguna is None:
        return None
    if not verifikasi_kata_sandi(pengguna["password_hash"], kata_sandi or ""):
        return None
    return pengguna


def muat_pengguna_dari_sesi():
    """Memuat pengguna dari sesi ke g.pengguna (dipanggil before_request)."""
    g.pengguna = None
    pengguna_id = session.get("pengguna_id")
    if pengguna_id is None:
        return
    # cari pengguna berdasarkan id
    with models.koneksi() as db:
        baris = db.execute(
            """
            SELECT p.id_pengguna, p.username_email, p.id_peran, r.nama_peran
            FROM pengguna AS p
            JOIN peran AS r ON r.id_peran = p.id_peran
            WHERE p.id_pengguna = ?
            """,
            (pengguna_id,),
        ).fetchone()
    g.pengguna = baris


def login_pengguna(pengguna):
    """Membuat sesi baru untuk pengguna."""
    session.clear()
    session["pengguna_id"] = pengguna["id_pengguna"]
    session.permanent = False


def logout_pengguna():
    """Mengosongkan sesi."""
    session.clear()


def peran_diperlukan(*peran):
    """Decorator: tamu -> login (dengan next aman); peran salah -> 403."""

    def dekorator(fungsi):
        @functools.wraps(fungsi)
        def pembungkus(*args, **kwargs):
            if g.pengguna is None:
                next_url = request.path
                if not next_url.startswith("/") or next_url.startswith("//"):
                    next_url = url_for("auth.beranda")
                return redirect(url_for("auth.login", next=next_url))
            if g.pengguna["nama_peran"] not in peran:
                abort(403)
            return fungsi(*args, **kwargs)

        return pembungkus

    return dekorator


def alamat_next_aman(next_url):
    """Mengembalikan next_url bila aman (mulai /, bukan //), selain itu None."""
    if not next_url:
        return None
    if not next_url.startswith("/") or next_url.startswith("//"):
        return None
    return next_url
