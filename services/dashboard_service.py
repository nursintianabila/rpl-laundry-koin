"""Logika bisnis dashboard Pemilik."""

import models


def statistik():
    """Mengambil ringkasan data untuk halaman dashboard."""
    return models.statistik_dashboard()
