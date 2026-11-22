"""Logika bisnis laporan pendapatan."""

from datetime import date

import models


class ValidasiPeriodeError(ValueError):
    """Galat validasi rentang tanggal laporan."""

    def __init__(self, pesan):
        self.pesan = pesan
        super().__init__(pesan)


def _tanggal(teks, nama):
    nilai = (teks or "").strip()
    if not nilai:
        return None
    try:
        date.fromisoformat(nilai)
    except ValueError:
        raise ValidasiPeriodeError(f"{nama} harus berformat TTTT-BB-HH.")
    return nilai


def ringkasan(mulai, akhir):
    """Mengambil ringkasan pendapatan dan perincian per layanan."""
    mulai_valid = _tanggal(mulai, "Tanggal mulai")
    akhir_valid = _tanggal(akhir, "Tanggal akhir")
    if mulai_valid and akhir_valid and mulai_valid > akhir_valid:
        raise ValidasiPeriodeError("Tanggal mulai tidak boleh setelah tanggal akhir.")
    return {
        "mulai": mulai_valid,
        "akhir": akhir_valid,
        "ringkasan": models.ringkasan_pendapatan(mulai_valid, akhir_valid),
        "per_layanan": models.pendapatan_per_layanan(mulai_valid, akhir_valid),
    }
