"""Pembuatan berkas ekspor transaksi (CSV dan PDF)."""
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


def buat_csv(baris, statistik):
    """Mengembalikan Response CSV yang bisa dibuka di Excel."""
    keluaran = io.StringIO()
    penulis = csv.writer(keluaran)
    penulis.writerow([
        "ID", "Pelanggan", "Layanan", "Tanggal",
        "Berat (kg)", "Total Biaya (Rp)", "Status",
    ])
    penulis.writerows(_baris_tabel(baris))
    penulis.writerow([])
    penulis.writerow(["Jumlah transaksi", statistik["jumlah_transaksi"]])
    penulis.writerow(["Total pendapatan (Rp)", statistik["total_pendapatan"]])

    respons = Response(
        "\ufeff" + keluaran.getvalue(),
        mimetype="text/csv; charset=utf-8",
    )
    respons.headers["Content-Disposition"] = (
        f"attachment; filename=transaksi-{datetime.now():%Y%m%d-%H%M%S}.csv"
    )
    return respons


def buat_pdf(baris, statistik):
    """Mengembalikan Response PDF berisi tabel transaksi dan ringkasan."""
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.units import mm
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

    def aman(teks):
        return str(teks).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    gaya = getSampleStyleSheet()
    cerita = [
        Paragraph("Laporan Transaksi - Sistem Informasi Laundry Koin", gaya["Title"]),
        Paragraph(f"Dicetak: {datetime.now():%Y-%m-%d %H:%M}", gaya["Normal"]),
        Spacer(1, 8),
    ]

    data = [["ID", "Pelanggan", "Layanan", "Tanggal", "Berat", "Total (Rp)", "Status"]]
    data.extend(_baris_tabel(baris))
    tabel = Table(data, colWidths=[12 * mm, 35 * mm, 35 * mm, 25 * mm, 15 * mm, 28 * mm, 22 * mm], repeatRows=1)
    tabel.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1f4e79")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    cerita.append(tabel)
    cerita.append(Spacer(1, 10))
    cerita.append(Paragraph(
        f"Jumlah transaksi: {statistik['jumlah_transaksi']} &nbsp;&nbsp; "
        f"Total pendapatan: Rp {statistik['total_pendapatan']:,}".replace(",", "."),
        gaya["Normal"],
    ))

    penyangga = io.BytesIO()
    dokumen = SimpleDocTemplate(penyangga, pagesize=A4, title="Laporan Transaksi Laundry Koin")
    dokumen.build(cerita)

    respons = Response(penyangga.getvalue(), mimetype="application/pdf")
    respons.headers["Content-Disposition"] = (
        f"attachment; filename=transaksi-{datetime.now():%Y%m%d-%H%M%S}.pdf"
    )
    return respons
