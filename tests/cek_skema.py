
import sqlite3
import sys
from pathlib import Path

# Menentukan lokasi proyek dan file skema
ROOT = Path(__file__).resolve().parents[1]
FILE_SKEMA = ROOT / "docs" / "desain" / "schema.sql"

# Membuat database sementara untuk pengujian
db = sqlite3.connect(":memory:")
db.execute("PRAGMA foreign_keys = ON")

# Membaca dan menjalankan skema
sql = FILE_SKEMA.read_text(encoding="utf-8")
db.executescript(sql)

# Memastikan foreign key aktif
assert db.execute("PRAGMA foreign_keys").fetchone()[0] == 1

# Menyiapkan data awal yang valid
db.execute(
    "INSERT INTO peran (nama_peran) VALUES (?)",
    ("Admin/Operator",)
)

db.execute(
    "INSERT INTO pelanggan (nama_pelanggan) VALUES (?)",
    ("Pelanggan Uji",)
)

db.execute(
    "INSERT INTO layanan (nama_layanan, harga) VALUES (?, ?)",
    ("Cuci Kering", 10000)
)

db.execute(
    """
    INSERT INTO pengguna
    (username_email, password_hash, id_peran)
    VALUES (?, ?, ?)
    """,
    ("admin@uji.com", "hash_password_uji", 1)
)

db.commit()

# Fungsi untuk menguji penolakan data tidak valid
jumlah_ok = 0
jumlah_gagal = 0


def uji_penolakan(nama_uji, perintah, data):
    global jumlah_ok, jumlah_gagal

    try:
        db.execute(perintah, data)
        db.rollback()
        print(f"GAGAL: {nama_uji} - data tidak valid diterima")
        jumlah_gagal += 1

    except sqlite3.IntegrityError:
        db.rollback()
        print(f"OK ditolak: {nama_uji}")
        jumlah_ok += 1


# Daftar pengujian pelanggaran
UJI = [
    (
        "Username/email duplikat",
        """
        INSERT INTO pengguna
        (username_email, password_hash, id_peran)
        VALUES (?, ?, ?)
        """,
        ("admin@uji.com", "hash_lain", 1)
    ),
    (
        "Foreign key peran tidak ditemukan",
        """
        INSERT INTO pengguna
        (username_email, password_hash, id_peran)
        VALUES (?, ?, ?)
        """,
        ("operator@uji.com", "hash_uji", 999)
    ),
    (
        "Harga layanan negatif",
        """
        INSERT INTO layanan (nama_layanan, harga)
        VALUES (?, ?)
        """,
        ("Layanan Tidak Valid", -5000)
    ),
    (
        "Foreign key pelanggan tidak ditemukan",
        """
        INSERT INTO transaksi
        (id_pelanggan, id_layanan, tanggal, berat, total_biaya)
        VALUES (?, ?, ?, ?, ?)
        """,
        (999, 1, "2026-11-13", 2.0, 20000)
    ),
    (
        "Berat transaksi nol",
        """
        INSERT INTO transaksi
        (id_pelanggan, id_layanan, tanggal, berat, total_biaya)
        VALUES (?, ?, ?, ?, ?)
        """,
        (1, 1, "2026-11-13", 0, 20000)
    ),
    (
        "Total biaya negatif",
        """
        INSERT INTO transaksi
        (id_pelanggan, id_layanan, tanggal, berat, total_biaya)
        VALUES (?, ?, ?, ?, ?)
        """,
        (1, 1, "2026-11-13", 2.0, -20000)
    )
]

# Menjalankan seluruh pengujian
for nama, perintah, data in UJI:
    uji_penolakan(nama, perintah, data)

# Menampilkan ringkasan hasil
print("\nRINGKASAN PENGUJIAN")
print(f"OK ditolak: {jumlah_ok}")
print(f"GAGAL: {jumlah_gagal}")

db.close()

# Memberikan status gagal jika ada pengujian yang tidak lolos
if jumlah_gagal > 0:
    sys.exit(1)
