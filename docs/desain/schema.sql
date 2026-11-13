
PRAGMA foreign_keys = ON;

-- 1. Tabel Peran
CREATE TABLE IF NOT EXISTS peran (
    id_peran INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_peran VARCHAR(50) NOT NULL UNIQUE
        CHECK (
            length(trim(nama_peran)) > 0
            AND length(nama_peran) <= 50
        )
);

-- 2. Tabel Pengguna
CREATE TABLE IF NOT EXISTS pengguna (
    id_pengguna INTEGER PRIMARY KEY AUTOINCREMENT,
    username_email VARCHAR(100) NOT NULL UNIQUE
        CHECK (
            length(trim(username_email)) > 0
            AND length(username_email) <= 100
        ),
    password_hash VARCHAR(255) NOT NULL
        CHECK (
            length(trim(password_hash)) > 0
            AND length(password_hash) <= 255
        ),
    id_peran INTEGER NOT NULL,
    FOREIGN KEY (id_peran)
        REFERENCES peran(id_peran)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- 3. Tabel Pelanggan
CREATE TABLE IF NOT EXISTS pelanggan (
    id_pelanggan INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_pelanggan VARCHAR(100) NOT NULL
        CHECK (
            length(trim(nama_pelanggan)) > 0
            AND length(nama_pelanggan) <= 100
        )
);

-- 4. Tabel Layanan
CREATE TABLE IF NOT EXISTS layanan (
    id_layanan INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_layanan VARCHAR(100) NOT NULL
        CHECK (
            length(trim(nama_layanan)) > 0
            AND length(nama_layanan) <= 100
        ),
    harga INTEGER NOT NULL
        CHECK (harga >= 0)
);

-- 5. Tabel Transaksi
CREATE TABLE IF NOT EXISTS transaksi (
    id_transaksi INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pelanggan INTEGER NOT NULL,
    id_layanan INTEGER NOT NULL,
    tanggal TEXT NOT NULL
        CHECK (
            length(tanggal) = 10
            AND tanggal GLOB
                '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
            AND date(tanggal) IS NOT NULL
            AND date(tanggal) = tanggal
        ),
    berat REAL NOT NULL
        CHECK (berat > 0),
    total_biaya INTEGER NOT NULL
        CHECK (total_biaya >= 0),
    FOREIGN KEY (id_pelanggan)
        REFERENCES pelanggan(id_pelanggan)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    FOREIGN KEY (id_layanan)
        REFERENCES layanan(id_layanan)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- 6. Tabel Mesin
CREATE TABLE IF NOT EXISTS mesin (
    id_mesin INTEGER PRIMARY KEY AUTOINCREMENT,
    informasi_mesin VARCHAR(150) NOT NULL
        CHECK (
            length(trim(informasi_mesin)) > 0
            AND length(informasi_mesin) <= 150
        ),
    status_mesin VARCHAR(30) NOT NULL
        CHECK (
            length(trim(status_mesin)) > 0
            AND length(status_mesin) <= 30
        )
);
