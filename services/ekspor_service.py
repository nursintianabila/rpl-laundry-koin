"""Pembuatan berkas ekspor transaksi (CSV dan PDF).

PDF dibuat dengan penulis PDF minimal berbasis pustaka standar sehingga
tidak bergantung pada paket tambahan saat aplikasi dijalankan.
"""
import csv
import io
from datetime import datetime

from flask import Response


def _baris_tabel(baris):
    return [
        [
            str(t["id_transaksi"]),
            t["nama_pelanggan"],
            t["nama_layanan"],
            t["tanggal"],
            str(t["berat"]),
            str(t["total_biaya"]),
            t["status_transaksi"] or "Diproses",
        ]
        for t in baris
    ]


def buat_csv(baris, ringkasan):
    """Mengembalikan Response CSV yang bisa dibuka di Excel."""
    keluaran = io.StringIO()
    penulis = csv.writer(keluaran)
    penulis.writerow([
        "ID", "Pelanggan", "Layanan", "Tanggal",
        "Berat (kg)", "Total Biaya (Rp)", "Status",
    ])
    penulis.writerows(_baris_tabel(baris))
    penulis.writerow([])
    penulis.writerow(["Jumlah transaksi", ringkasan["jumlah"]])
    penulis.writerow(["Total pendapatan (Rp)", ringkasan["total"]])

    respons = Response(
        "\ufeff" + keluaran.getvalue(),
        mimetype="text/csv; charset=utf-8",
    )
    respons.headers["Content-Disposition"] = (
        f"attachment; filename=transaksi-{datetime.now():%Y%m%d-%H%M%S}.csv"
    )
    return respons


def _pdf_aman(teks):
    """Escape teks untuk string PDF dan samakan ke Latin-1."""
    teks = str(teks).replace("Rp ", "Rp ")
    teks = teks.encode("latin-1", "replace").decode("latin-1")
    return teks.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def _objek_pdf(isi):
    return ("%d 0 obj\n" + isi + "\nendobj\n")


def _bangun_pdf(baris_teks):
    """Menyusun PDF sederhana dari daftar baris teks."""
    objek = []
    # placeholder: 1=Catalog, 2=Pages, 3=Font, 4..=Page, setelahnya=Contents
    jumlah_per_halaman = 52
    halaman = [
        baris_teks[i:i + jumlah_per_halaman]
        for i in range(0, len(baris_teks), jumlah_per_halaman)
    ] or [[]]

    jumlah_objek = 3 + 2 * len(halaman)
    objek.append(_objek_pdf("<< /Type /Catalog /Pages 2 0 R >>"))
    kids = " ".join(f"{4 + 2 * i} 0 R" for i in range(len(halaman)))
    objek.append(_objek_pdf(
        f"<< /Type /Pages /Kids [{kids}] /Count {len(halaman)} >>"
    ))
    objek.append(_objek_pdf(
        "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>"
    ))

    for indeks, baris in enumerate(halaman):
        nomor_halaman = 4 + 2 * indeks
        nomor_konten = nomor_halaman + 1
        objek.append(_objek_pdf(
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] "
            f"/Resources << /Font << /F1 3 0 R >> >> "
            f"/Contents {nomor_konten} 0 R >>"
        ))

        bagian = ["BT", "/F1 10 Tf", "12 TL", "45 795 Td"]
        for baris_teks in baris:
            bagian.append("(" + _pdf_aman(baris_teks) + ") Tj")
            bagian.append("T*")
        bagian.append("ET")
        aliran = "\n".join(bagian)
        objek.append(_objek_pdf(
            f"<< /Length {len(aliran.encode('latin-1', 'replace'))} >>\n"
            f"stream\n{aliran}\nendstream"
        ))

    hasil = io.BytesIO()
    hasil.write(b"%PDF-1.4\n")
    offset = [0]
    for i, isi in enumerate(objek, start=1):
        offset.append(hasil.tell())
        hasil.write(isi.encode("latin-1", "replace"))

    posisi_xref = hasil.tell()
    hasil.write(f"xref\n0 {jumlah_objek + 1}\n".encode())
    hasil.write(b"0000000000 65535 f \n")
    for i in range(1, jumlah_objek + 1):
        hasil.write(f"{offset[i]:010d} 00000 n \n".encode())
    hasil.write(
        f"trailer\n<< /Size {jumlah_objek + 1} /Root 1 0 R >>\n"
        f"startxref\n{posisi_xref}\n%%EOF\n".encode()
    )
    return hasil.getvalue()


def buat_pdf(baris, ringkasan):
    """Mengembalikan Response PDF berisi tabel transaksi dan ringkasan."""
    teks = [
        "Laporan Transaksi - Sistem Informasi Laundry Koin",
        f"Dicetak: {datetime.now():%Y-%m-%d %H:%M}",
        "",
        "ID | Pelanggan | Layanan | Tanggal | Berat | Total | Status",
        "-" * 78,
    ]
    for t in baris:
        teks.append(
            f"{t['id_transaksi']:>3} | {t['nama_pelanggan']:<18} | "
            f"{t['nama_layanan']:<15} | {t['tanggal']} | "
            f"{t['berat']:>5} | {t['total_biaya']:>8} | "
            f"{t['status_transaksi'] or 'Diproses'}"
        )
    teks.extend([
        "-" * 78,
        f"Jumlah transaksi: {ringkasan['jumlah']}",
        f"Total pendapatan: Rp {ringkasan['total']:,}".replace(",", "."),
    ])

    respons = Response(_bangun_pdf(teks), mimetype="application/pdf")
    respons.headers["Content-Disposition"] = (
        f"attachment; filename=transaksi-{datetime.now():%Y%m%d-%H%M%S}.pdf"
    )
    return respons
