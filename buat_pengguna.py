"""Skrip pembuatan akun pengguna (Jobsheet 11 Langkah 3).

Menjalankan: python buat_pengguna.py
Kata sandi dibaca dari terminal, tidak disimpan di kode.
"""
import getpass
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import models
from services import auth_service

models.init_db()

print("Peran tersedia: Pemilik, Admin/Operator")
username = input("Nama pengguna (email): ").strip()
peran = input("Peran: ").strip()
kata_sandi = getpass.getpass("Kata sandi: ")
konfirmasi = getpass.getpass("Ulangi kata sandi: ")

if kata_sandi != konfirmasi:
    print("Kata sandi tidak sama.")
    sys.exit(1)

try:
    auth_service.buat_pengguna(username, kata_sandi, peran)
except auth_service.ValidasiPenggunaError as kesalahan:
    print("Gagal membuat akun:")
    for pesan in kesalahan.daftar_pesan:
        print(" -", pesan)
    sys.exit(1)

print("Akun berhasil dibuat.")
