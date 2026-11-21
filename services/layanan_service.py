"""Logika bisnis pengelolaan layanan laundry."""

import models

BATAS_NAMA = 100


class ValidasiLayananError(ValueError):
    """Kesalahan validasi isian layanan yang ditampilkan ke pengguna."""

    def __init__(self, daftar_pesan):
        self.daftar_pesan = daftar_pesan
        super().__init__(" ".join(daftar_pesan))


def daftar_layanan():
    """Mengambil daftar layanan yang akan ditampilkan kepada pengguna."""
    return models.semua_layanan()


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
