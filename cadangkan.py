"""Cadangkan basis data: python cadangkan.py [folder_tujuan]

Memakai API backup SQLite sehingga aman dijalankan saat aplikasi berjalan.
Hasil: cadangan/laundry_koin-YYYYMMDD-HHMMSS.db (folder cadangan/ tidak ikut Git).
"""
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

import models


def cadangkan(folder=None):
    """Membuat berkas cadangan dan mengembalikan Path-nya."""
    tujuan_folder = Path(folder) if folder else Path(__file__).with_name("cadangan")
    tujuan_folder.mkdir(parents=True, exist_ok=True)
    berkas = tujuan_folder / f"laundry_koin-{datetime.now():%Y%m%d-%H%M%S}.db"

    sumber = sqlite3.connect(models.DB_PATH)
    tujuan = sqlite3.connect(berkas)
    try:
        with tujuan:
            sumber.backup(tujuan)
    finally:
        sumber.close()
        tujuan.close()
    return berkas


if __name__ == "__main__":
    print("Cadangan dibuat:", cadangkan(sys.argv[1] if len(sys.argv) > 1 else None))
