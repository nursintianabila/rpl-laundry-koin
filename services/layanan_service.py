"""Logika bisnis pengelolaan layanan laundry."""

import sqlite3

import models

BATAS_NAMA = 100


class ValidasiLayananError(ValueError):
    """Kesalahan validasi isian layanan yang ditampilkan ke pengguna."""

    def __init__(self, daftar_pesan):
        self.daftar_pesan = daftar_pesan
        super().__init__(" ".join(daftar_pesan))


class LayananDipakaiError(ValueError):
    """Layanan tidak dapat dihapus karena masih dipakai transaksi."""


def daftar_layanan():
    """Mengambil daftar layanan yang akan ditampilkan kepada pengguna."""
    return models.semua_layanan()


def ambil_layanan(id_layanan):
    """Mengambil satu layanan berdasarkan ID."""
    return models.ambil_layanan(id_layanan)


def periksa_isian(nama_layanan, harga, id_layanan=None):
    """Memvalidasi isian layanan dan mengembalikan nilai bersih serta galat."""
    nama = (nama_layanan or "").strip()
    harga_teks = (harga or "").strip()
    galat = []
    nilai_harga = None

    if not nama:
        galat.append("Nama layanan wajib diisi.")
    elif len(nama) > BATAS_NAMA:
        galat.append(f"Nama layanan maksimal {BATAS_NAMA} karakter.")

    if not harga_teks:
        galat.append("Harga wajib diisi.")
    elif not (harga_teks.isascii() and harga_teks.isdigit()):
        galat.append("Harga harus berupa bilangan bulat, misalnya 10000.")
    else:
        try:
            nilai_harga = int(harga_teks)
        except ValueError:
            galat.append("Harga harus berupa bilangan bulat, misalnya 10000.")
        else:
            if nilai_harga < 0:
                galat.append("Harga tidak boleh negatif.")

    if nama:
        layanan_lain = models.cari_layanan_by_nama(nama)
        if layanan_lain is not None and layanan_lain["id_layanan"] != id_layanan:
            galat.append("Nama layanan sudah ada. Gunakan nama lain.")

    nilai = {"nama_layanan": nama, "harga": nilai_harga}
    return nilai, galat


def tambah_layanan(nama_layanan, harga):
    """Menambahkan layanan baru setelah isian dinyatakan valid."""
    nilai, galat = periksa_isian(nama_layanan, harga)
    if galat:
        raise ValidasiLayananError(galat)
    return models.tambah_layanan(nilai["nama_layanan"], nilai["harga"])


def ubah_layanan(id_layanan, nama_layanan, harga):
    """Mengubah layanan setelah isian dinyatakan valid."""
    nilai, galat = periksa_isian(nama_layanan, harga, id_layanan=id_layanan)
    if galat:
        raise ValidasiLayananError(galat)
    return models.ubah_layanan(
        id_layanan,
        nilai["nama_layanan"],
        nilai["harga"],
    )


def hapus_layanan(id_layanan):
    """Menghapus layanan dan menerjemahkan galat kunci asing."""
    try:
        return models.hapus_layanan(id_layanan)
    except sqlite3.IntegrityError as kesalahan:
        raise LayananDipakaiError(
            "Layanan tidak dapat dihapus karena masih dipakai pada transaksi."
        ) from kesalahan
