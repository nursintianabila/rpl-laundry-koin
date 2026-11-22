"""Logika bisnis pengelolaan transaksi laundry."""

import re
from datetime import date

import models

BATAS_NAMA = 100


class ValidasiTransaksiError(ValueError):
    """Kesalahan validasi isian transaksi yang ditampilkan ke pengguna."""

    def __init__(self, daftar_pesan):
        self.daftar_pesan = daftar_pesan
        super().__init__(" ".join(daftar_pesan))


def daftar_transaksi(kata="", id_layanan=None):
    """Mengambil daftar transaksi yang akan ditampilkan kepada pengguna."""
    return models.cari_transaksi(kata, id_layanan)


def daftar_pelanggan():
    """Mengambil daftar pelanggan untuk pilihan pada form transaksi."""
    return models.semua_pelanggan()


def cari_pelanggan(kata=""):
    """Mencari pelanggan untuk autocomplete pada form transaksi."""
    from services import pelanggan_service
    return pelanggan_service.cari_pelanggan(kata)


def daftar_layanan():
    """Mengambil daftar layanan untuk pilihan pada form transaksi."""
    return models.semua_layanan()


def ambil_transaksi(id_transaksi):
    """Mengambil satu transaksi berdasarkan ID."""
    return models.ambil_transaksi(id_transaksi)


def periksa_isian(id_pelanggan, id_layanan, tanggal, berat):
    """Memvalidasi isian transaksi dan mengembalikan nilai bersih serta galat."""
    galat = []
    id_pel = None
    id_lay = None

    try:
        id_pel = int(id_pelanggan)
    except (TypeError, ValueError):
        galat.append("Pilih pelanggan.")
    else:
        if models.ambil_pelanggan(id_pel) is None:
            galat.append("Pelanggan tidak ditemukan.")

    try:
        id_lay = int(id_layanan)
    except (TypeError, ValueError):
        galat.append("Pilih layanan.")
    else:
        if models.ambil_layanan(id_lay) is None:
            galat.append("Layanan tidak ditemukan.")

    tgl = (tanggal or "").strip()
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", tgl):
        galat.append("Tanggal harus berformat TTTT-BB-HH.")
    else:
        try:
            date.fromisoformat(tgl)
        except ValueError:
            galat.append("Tanggal harus berformat TTTT-BB-HH.")

    berat_nilai = None
    try:
        berat_nilai = float(str(berat).replace(",", "."))
    except (TypeError, ValueError):
        galat.append("Berat harus berupa angka.")
    else:
        if berat_nilai is None or berat_nilai <= 0:
            galat.append("Berat harus lebih dari 0.")

    nilai = {
        "id_pelanggan": id_pel,
        "id_layanan": id_lay,
        "tanggal": tgl,
        "berat": berat_nilai,
    }
    return nilai, galat


def tambah_transaksi(id_pelanggan, id_layanan, tanggal, berat):
    """Menambahkan transaksi baru setelah isian dinyatakan valid."""
    nilai, galat = periksa_isian(id_pelanggan, id_layanan, tanggal, berat)
    if galat:
        raise ValidasiTransaksiError(galat)

    layanan = models.ambil_layanan(nilai["id_layanan"])
    total_biaya = int(round(nilai["berat"] * layanan["harga"]))

    return models.tambah_transaksi(
        nilai["id_pelanggan"],
        nilai["id_layanan"],
        nilai["tanggal"],
        nilai["berat"],
        total_biaya,
    )


def hapus_transaksi(id_transaksi):
    """Menghapus transaksi; mengembalikan jumlah baris terhapus."""
    return models.hapus_transaksi(id_transaksi)
