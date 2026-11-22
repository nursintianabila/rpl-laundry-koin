"""Logika bisnis pengelolaan pelanggan laundry."""

import sqlite3

import models

BATAS_NAMA = 100


class ValidasiPelangganError(ValueError):
    """Kesalahan validasi isian pelanggan yang ditampilkan ke pengguna."""

    def __init__(self, daftar_pesan):
        self.daftar_pesan = daftar_pesan
        super().__init__(" ".join(daftar_pesan))


class PelangganDipakaiError(ValueError):
    """Pelanggan tidak dapat dihapus karena masih dipakai transaksi."""


def daftar_pelanggan():
    """Mengambil daftar pelanggan yang akan ditampilkan kepada pengguna."""
    return models.semua_pelanggan()


def cari_pelanggan(kata=""):
    """Mencari pelanggan untuk pilihan pada form transaksi."""
    return models.cari_pelanggan(kata)


def ambil_pelanggan(id_pelanggan):
    """Mengambil satu pelanggan berdasarkan ID."""
    return models.ambil_pelanggan(id_pelanggan)


def periksa_isian(nama_pelanggan):
    """Memvalidasi isian pelanggan dan mengembalikan nama bersih serta galat."""
    nama = (nama_pelanggan or "").strip()
    galat = []

    if not nama:
        galat.append("Nama pelanggan wajib diisi.")
    elif len(nama) > BATAS_NAMA:
        galat.append(f"Nama pelanggan maksimal {BATAS_NAMA} karakter.")

    return nama, galat


def tambah_pelanggan(nama_pelanggan):
    """Menambahkan pelanggan baru setelah isian dinyatakan valid."""
    nama, galat = periksa_isian(nama_pelanggan)
    if galat:
        raise ValidasiPelangganError(galat)
    return models.tambah_pelanggan(nama)


def ubah_pelanggan(id_pelanggan, nama_pelanggan):
    """Mengubah pelanggan setelah isian dinyatakan valid."""
    nama, galat = periksa_isian(nama_pelanggan)
    if galat:
        raise ValidasiPelangganError(galat)
    return models.ubah_pelanggan(id_pelanggan, nama)


def hapus_pelanggan(id_pelanggan):
    """Menghapus pelanggan dan menerjemahkan galat kunci asing."""
    try:
        return models.hapus_pelanggan(id_pelanggan)
    except sqlite3.IntegrityError as kesalahan:
        raise PelangganDipakaiError(
            "Pelanggan tidak dapat dihapus karena masih dipakai pada transaksi."
        ) from kesalahan
