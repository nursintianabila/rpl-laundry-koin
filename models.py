import sqlite3
from contextlib import contextmanager
from pathlib import Path

# Lokasi berkas proyek, database, dan skema.
ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "instance" / "laundry_koin.db"
SCHEMA = ROOT / "docs" / "desain" / "schema.sql"


@contextmanager
def koneksi():
    """Buka koneksi SQLite, aktifkan kunci asing, lalu commit dan tutup."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys = ON")
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def init_db():
    """Membuat database dari schema.sql bila database belum ada."""
    if not DB_PATH.exists():
        with koneksi() as db:
            db.executescript(SCHEMA.read_text(encoding="utf-8"))


def semua_layanan():
    """Mengambil seluruh data layanan untuk halaman daftar."""
    with koneksi() as db:
        return db.execute(
            """
            SELECT id_layanan, nama_layanan, harga
            FROM layanan
            ORDER BY id_layanan
            """
        ).fetchall()


def ambil_layanan(id_layanan):
    """Mengambil satu layanan berdasarkan ID, atau None bila tidak ada."""
    with koneksi() as db:
        return db.execute(
            """
            SELECT id_layanan, nama_layanan, harga
            FROM layanan
            WHERE id_layanan = ?
            """,
            (id_layanan,),
        ).fetchone()


def cari_layanan_by_nama(nama_layanan):
    """Mencari layanan berdasarkan nama tanpa membedakan huruf besar/kecil."""
    with koneksi() as db:
        return db.execute(
            """
            SELECT id_layanan, nama_layanan
            FROM layanan
            WHERE lower(nama_layanan) = lower(?)
            """,
            (nama_layanan,),
        ).fetchone()


def tambah_layanan(nama_layanan, harga):
    """Menyimpan layanan baru dan mengembalikan ID yang dibuat."""
    with koneksi() as db:
        hasil = db.execute(
            "INSERT INTO layanan (nama_layanan, harga) VALUES (?, ?)",
            (nama_layanan, harga),
        )
        return hasil.lastrowid


def ubah_layanan(id_layanan, nama_layanan, harga):
    """Mengubah nama dan harga layanan; mengembalikan jumlah baris terubah."""
    with koneksi() as db:
        hasil = db.execute(
            """
            UPDATE layanan
            SET nama_layanan = ?, harga = ?
            WHERE id_layanan = ?
            """,
            (nama_layanan, harga, id_layanan),
        )
        return hasil.rowcount


def hapus_layanan(id_layanan):
    """Menghapus layanan; kegagalan kunci asing diteruskan ke pemanggil."""
    with koneksi() as db:
        hasil = db.execute(
            "DELETE FROM layanan WHERE id_layanan = ?",
            (id_layanan,),
        )
        return hasil.rowcount