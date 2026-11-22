"""Logika bisnis pembaruan status mesin."""

import models

STATUS_DISEDIAKAN = ("Tersedia", "Sedang digunakan", "Rusak", "Perawatan")
BATAS_KETERANGAN = 150


class ValidasiMesinError(ValueError):
    """Galat validasi status mesin."""

    def __init__(self, daftar_pesan):
        self.daftar_pesan = daftar_pesan
        super().__init__(" ".join(daftar_pesan))


def daftar_mesin():
    return models.semua_mesin()


def ambil_mesin(id_mesin):
    return models.ambil_mesin(id_mesin)


def ubah_status(id_mesin, status):
    """Mengubah status mesin dengan validasi sederhana."""
    nilai = (status or "").strip()
    galat = []
    if not nilai:
        galat.append("Status mesin wajib diisi.")
    elif nilai not in STATUS_DISEDIAKAN:
        galat.append("Status mesin tidak dikenal.")
    if galat:
        raise ValidasiMesinError(galat)
    return models.ubah_status_mesin(id_mesin, nilai)
