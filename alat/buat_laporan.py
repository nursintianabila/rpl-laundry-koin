"""Susun laporan akhir (Bab 3 revisi + Bab 4) menjadi .docx dan .pdf.

Jalankan: python alat/buat_laporan.py
"""
import re
from pathlib import Path

from docx import Document
from docx.shared import Pt
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Preformatted, PageBreak,
)

ROOT = Path(__file__).resolve().parents[1]
OUT_DOCX = ROOT / "docs" / "laporan-akhir.docx"
OUT_PDF = ROOT / "docs" / "laporan-akhir.pdf"

FONT = "Arial"
FONT_BOLD = "ArialBold"
for name, path in [
    (FONT, r"C:\Windows\Fonts\arial.ttf"),
    (FONT_BOLD, r"C:\Windows\Fonts\arialbd.ttf"),
]:
    if Path(path).exists():
        pdfmetrics.registerFont(TTFont(name, path))

# (judul, berkas)
BAB3 = [
    ("3.1 Kebutuhan Perangkat Lunak", "PRD.md"),
    ("3.2 Arsitektur Sistem", "docs/desain/arsitektur.md"),
    ("3.3 Relasi Entitas", "docs/desain/relasi-entitas.md"),
    ("3.4 Daftar Entitas", "docs/desain/daftar-entitas.md"),
    ("3.5 Halaman dan Navigasi", "docs/desain/daftar-halaman.md"),
    ("3.6 Perencanaan Pengujian", "docs/pengujian/rencana-uji.md"),
    ("3.7 Perubahan terhadap Rancangan Awal", "docs/bab4/perubahan-rancangan.md"),
]
BAB4 = [
    ("4.1 Lingkungan Implementasi", "docs/bab4/4.1-lingkungan.md"),
    ("4.2 Implementasi Sistem", "docs/bab4/4.2-implementasi.md"),
    ("4.3 Tinjauan Kode dan Keamanan", "docs/bab4/4.3-tinjauan.md"),
    ("4.4 Pengujian", "docs/bab4/4.4-pengujian.md"),
    ("4.5 Rilis dan Dokumentasi", "docs/bab4/4.5-rilis.md"),
    ("4.6 Pembahasan", "docs/bab4/4.6-pembahasan.md"),
    ("Lampiran A. Rekap Jurnal Vibe Coding", "docs/bab4/rekap-jurnal.md"),
    ("Lampiran B. Daftar Pustaka", "docs/bab4/daftar-pustaka.md"),
]


def bersihkan(teks):
    teks = re.sub(r"\*\*(.+?)\*\*", r"\1", teks)
    teks = re.sub(r"`(.+?)`", r"\1", teks)
    teks = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", teks)
    return teks.strip()


def blok_markdown(teks):
    """Ubah markdown menjadi daftar blok: ('h1'|'h2'|'p'|'code'|'table', isi)."""
    teks = teks.lstrip("\ufeff")
    hasil = []
    baris = teks.splitlines()
    i = 0
    while i < len(baris):
        b = baris[i]
        s = b.strip()
        if s.startswith("```"):
            i += 1
            kode = []
            while i < len(baris) and not baris[i].strip().startswith("```"):
                kode.append(baris[i])
                i += 1
            i += 1
            hasil.append(("code", "\n".join(kode)))
            continue
        if s.startswith("|") and i + 1 < len(baris) and baris[i + 1].strip().startswith("|"):
            tabel = []
            while i < len(baris) and baris[i].strip().startswith("|"):
                sel = [c.strip() for c in baris[i].strip().strip("|").split("|")]
                if not all(set(c) <= set("-: ") for c in sel):
                    tabel.append([bersihkan(c) for c in sel])
                i += 1
            if tabel:
                hasil.append(("table", tabel))
            continue
        if s.startswith("## "):
            hasil.append(("h2", bersihkan(s[3:])))
        elif s.startswith("# "):
            hasil.append(("h1", bersihkan(s[2:])))
        elif s:
            hasil.append(("p", bersihkan(s)))
        i += 1
    return hasil


def tambah_ke_docx(doc, blok):
    for jenis, isi in blok:
        if jenis == "h1":
            doc.add_heading(isi, level=1)
        elif jenis == "h2":
            doc.add_heading(isi, level=2)
        elif jenis == "code":
            p = doc.add_paragraph()
            run = p.add_run(isi)
            run.font.name = "Consolas"
            run.font.size = Pt(9)
        elif jenis == "table":
            t = doc.add_table(rows=1, cols=len(isi[0]))
            t.style = "Table Grid"
            for j, h in enumerate(isi[0]):
                t.rows[0].cells[j].text = h
            for baris in isi[1:]:
                sel = t.add_row().cells
                for j, v in enumerate(baris):
                    sel[j].text = v
            doc.add_paragraph()
        else:
            doc.add_paragraph(isi)


def escape_xml(teks):
    return teks.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def tambah_ke_pdf(cerita, blok, styles):
    for jenis, isi in blok:
        if jenis == "h1":
            cerita.append(Paragraph(escape_xml(isi), styles["Heading1"]))
        elif jenis == "h2":
            cerita.append(Paragraph(escape_xml(isi), styles["Heading2"]))
        elif jenis == "code":
            cerita.append(Preformatted(isi, styles["Kode"]))
        elif jenis == "table":
            data = [[Paragraph(escape_xml(c), styles["Small"]) for c in baris] for baris in isi]
            lebar = [170 * mm / len(isi[0])] * len(isi[0])
            t = Table(data, colWidths=lebar, repeatRows=1)
            t.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1f4e79")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("FONTSIZE", (0, 0), (-1, -1), 8),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ]))
            cerita.append(t)
            cerita.append(Spacer(1, 6))
        else:
            cerita.append(Paragraph(escape_xml(isi), styles["Body"]))


def main():
    doc = Document()
    for gaya, ukuran in [("Normal", 11)]:
        doc.styles[gaya].font.name = FONT
        doc.styles[gaya].font.size = Pt(ukuran)

    doc.add_heading("Laporan Proyek Rekayasa Perangkat Lunak", 0)
    doc.add_heading("Sistem Informasi Laundry Koin — Versi 1.0.0", 1)
    doc.add_paragraph("Nur Sintia Nabila — Prodi D3 Teknologi Informasi, Politeknik Sampit")
    doc.add_paragraph("Laporan ini menyatukan Bab 3 yang telah direvisi dan Bab 4 sesuai hasil implementasi dan pengujian.")

    for judul, berkas in BAB3 + BAB4:
        path = ROOT / berkas
        doc.add_heading(judul, level=1)
        if path.exists():
            tambah_ke_docx(doc, blok_markdown(path.read_text(encoding="utf-8")))
        else:
            doc.add_paragraph(f"[ISI] Berkas sumber tidak ditemukan: {berkas}")
    doc.save(OUT_DOCX)
    print("DOCX:", OUT_DOCX)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Body", fontName=FONT, fontSize=10, leading=14, spaceAfter=6))
    styles.add(ParagraphStyle(name="Small", fontName=FONT, fontSize=8, leading=10))
    styles.add(ParagraphStyle(name="Kode", fontName="Courier", fontSize=8, leading=10, backColor=colors.HexColor("#f2f2f2")))

    cerita = []
    cerita.append(Paragraph("Laporan Proyek Rekayasa Perangkat Lunak", styles["Title"]))
    cerita.append(Paragraph("Sistem Informasi Laundry Koin — Versi 1.0.0", styles["Heading1"]))
    cerita.append(Paragraph("Nur Sintia Nabila — Prodi D3 Teknologi Informasi, Politeknik Sampit", styles["Body"]))
    for judul, berkas in BAB3 + BAB4:
        cerita.append(PageBreak())
        cerita.append(Paragraph(escape_xml(judul), styles["Heading1"]))
        path = ROOT / berkas
        if path.exists():
            tambah_ke_pdf(cerita, blok_markdown(path.read_text(encoding="utf-8")), styles)
        else:
            cerita.append(Paragraph(f"[ISI] Berkas sumber tidak ditemukan: {berkas}", styles["Body"]))

    pdf = SimpleDocTemplate(
        str(OUT_PDF), pagesize=A4,
        leftMargin=18 * mm, rightMargin=18 * mm,
        topMargin=18 * mm, bottomMargin=18 * mm,
        title="Laporan Proyek RPL — Sistem Informasi Laundry Koin",
    )
    pdf.build(cerita)
    print("PDF:", OUT_PDF)


if __name__ == "__main__":
    main()
