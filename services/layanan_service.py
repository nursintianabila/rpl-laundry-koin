"""Logika bisnis pengelolaan layanan laundry."""

from models import semua_layanan


def daftar_layanan():
    """Mengambil daftar layanan yang akan ditampilkan kepada pengguna."""
    return semua_layanan()
