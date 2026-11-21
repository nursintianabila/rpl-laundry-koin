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
    seed_peran()


def seed_peran():
    """Memastikan peran dasar tersedia."""
    peran_dasar = ("Pemilik", "Admin/Operator")
    with koneksi() as db:
        for nama in peran_dasar:
            db.execute(
                "INSERT OR IGNORE INTO peran (nama_peran) VALUES (?)",
                (nama,),
            )


def ambil_peran_by_nama(nama_peran):
    with koneksi() as db:
        return db.execute(
            "SELECT id_peran, nama_peran FROM peran WHERE nama_peran = ?",
            (nama_peran,),
        ).fetchone()


def ambil_pengguna_by_username(username_email):
    with koneksi() as db:
        return db.execute(
            """
            SELECT p.id_pengguna, p.username_email, p.password_hash, p.id_peran, r.nama_peran
            FROM pengguna AS p
            JOIN peran AS r ON r.id_peran = p.id_peran
            WHERE p.username_email = ?
            """,
            (username_email,),
        ).fetchone()


def tambah_pengguna(username_email, password_hash, id_peran):
    with koneksi() as db:
        hasil = db.execute(
            "INSERT INTO pengguna (username_email, password_hash, id_peran) VALUES (?, ?, ?)",
            (username_email, password_hash, id_peran),
        )
        return hasil.lastrowid


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


def semua_pelanggan():
    """Mengambil seluruh data pelanggan untuk halaman daftar."""
    with koneksi() as db:
        return db.execute(
            """
            SELECT id_pelanggan, nama_pelanggan
            FROM pelanggan
            ORDER BY id_pelanggan
            """
        ).fetchall()


def _escape_like(teks):
    """Netralkan % dan _ agar dicari sebagai huruf biasa."""
    return teks.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")


def semua_transaksi():
    """Mengambil daftar transaksi dengan JOIN ke pelanggan dan layanan."""
    return cari_transaksi()


def cari_transaksi(kata="", id_layanan=None):
    """Mencari dan menyaring transaksi; kata dicari pada nama pelanggan/layanan."""
    sql = """
        SELECT t.id_transaksi,
               t.id_pelanggan,
               t.id_layanan,
               t.tanggal,
               t.berat,
               t.total_biaya,
               p.nama_pelanggan,
               l.nama_layanan,
               l.harga AS harga_layanan
        FROM transaksi AS t
        JOIN pelanggan AS p ON p.id_pelanggan = t.id_pelanggan
        JOIN layanan AS l ON l.id_layanan = t.id_layanan
        WHERE (p.nama_pelanggan LIKE ? ESCAPE '\\'
               OR l.nama_layanan LIKE ? ESCAPE '\\')
    """
    pola = "%" + _escape_like(kata) + "%"
    param = [pola, pola]

    if id_layanan is not None:
        sql += " AND t.id_layanan = ?"
        param.append(id_layanan)

    sql += " ORDER BY t.id_transaksi DESC"

    with koneksi() as db:
        return db.execute(sql, param).fetchall()


def ambil_transaksi(id_transaksi):
    """Mengambil satu transaksi berdasarkan ID, atau None bila tidak ada."""
    with koneksi() as db:
        return db.execute(
            """
            SELECT t.id_transaksi,
                   t.id_pelanggan,
                   t.id_layanan,
                   t.tanggal,
                   t.berat,
                   t.total_biaya,
                   p.nama_pelanggan,
                   l.nama_layanan,
                   l.harga AS harga_layanan
            FROM transaksi AS t
            JOIN pelanggan AS p ON p.id_pelanggan = t.id_pelanggan
            JOIN layanan AS l ON l.id_layanan = t.id_layanan
            WHERE t.id_transaksi = ?
            """,
            (id_transaksi,),
        ).fetchone()


def tambah_transaksi(id_pelanggan, id_layanan, tanggal, berat, total_biaya):
    """Menyimpan transaksi baru dan mengembalikan ID yang dibuat."""
    with koneksi() as db:
        hasil = db.execute(
            """
            INSERT INTO transaksi
            (id_pelanggan, id_layanan, tanggal, berat, total_biaya)
            VALUES (?, ?, ?, ?, ?)
            """,
            (id_pelanggan, id_layanan, tanggal, berat, total_biaya),
        )
        return hasil.lastrowid


def hapus_transaksi(id_transaksi):
    """Menghapus transaksi; mengembalikan jumlah baris terhapus."""
    with koneksi() as db:
        hasil = db.execute(
            "DELETE FROM transaksi WHERE id_transaksi = ?",
            (id_transaksi,),
        )
        return hasil.rowcount


def ambil_pelanggan(id_pelanggan):
    """Mengambil satu pelanggan berdasarkan ID, atau None bila tidak ada."""
    with koneksi() as db:
        return db.execute(
            """
            SELECT id_pelanggan, nama_pelanggan
            FROM pelanggan
            WHERE id_pelanggan = ?
            """,
            (id_pelanggan,),
        ).fetchone()


def tambah_pelanggan(nama_pelanggan):
    """Menyimpan pelanggan baru dan mengembalikan ID yang dibuat."""
    with koneksi() as db:
        hasil = db.execute(
            "INSERT INTO pelanggan (nama_pelanggan) VALUES (?)",
            (nama_pelanggan,),
        )
        return hasil.lastrowid


def ubah_pelanggan(id_pelanggan, nama_pelanggan):
    """Mengubah nama pelanggan; mengembalikan jumlah baris terubah."""
    with koneksi() as db:
        hasil = db.execute(
            "UPDATE pelanggan SET nama_pelanggan = ? WHERE id_pelanggan = ?",
            (nama_pelanggan, id_pelanggan),
        )
        return hasil.rowcount


def hapus_pelanggan(id_pelanggan):
    """Menghapus pelanggan; kegagalan kunci asing diteruskan ke pemanggil."""
    with koneksi() as db:
        hasil = db.execute(
            "DELETE FROM pelanggan WHERE id_pelanggan = ?",
            (id_pelanggan,),
        )
        return hasil.rowcount


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