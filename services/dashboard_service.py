"""Logika bisnis dashboard."""

import models
from services import transaksi_service


def statistik():
    """Mengambil ringkasan data untuk halaman dashboard."""
    return models.statistik_dashboard()


def notifikasi_admin(batas=5):
    """Mengambil notifikasi transaksi selesai untuk dashboard Admin."""
    return transaksi_service.transaksi_selesai_terbaru(batas)
