"""Periksa kelengkapan draf Bab 4.

    python alat/periksa_draf.py docs/bab4 PRD.md

Sebuah subbab dianggap SELESAI bila berkasnya ada, memuat >= 150 kata uraian
(tabel dan kode tidak dihitung), tidak ada penanda [ISI], dan memuat >= 1 bukti.
Draf siap progress check bila >= 5 dari 6 subbab selesai.
"""
import sys
from pathlib import Path

SUBBAB = {
    "4.1": "Lingkungan Implementasi",
    "4.2": "Implementasi Sistem",
    "4.3": "Tinjauan Kode dan Keamanan",
    "4.4": "Pengujian",
    "4.5": "Rilis dan Dokumentasi",
    "4.6": "Pembahasan",
}
MIN_KATA = 150


def analisis(teks):
    """Kembalikan (jumlah kata uraian, ada_penanda_ISI, ada_bukti)."""
    uraian, dalam_kode, bukti = [], False, False
    for baris in teks.splitlines():
        if baris.strip().startswith("```"):
            dalam_kode, bukti = not dalam_kode, True
            continue
        if dalam_kode:
            continue
        if baris.strip().startswith("|") or baris.strip().startswith("!["):
            bukti = True
            continue
        if not baris.lstrip().startswith("#"):
            uraian.append(baris)
    return len(" ".join(uraian).split()), "[ISI]" in teks, bukti


def main(folder, prd=None):
    selesai, semua_teks = 0, ""
    print(f"{'Subbab':8s}{'Judul':30s}{'Kata':>6s}  Status")
    for kode, judul in SUBBAB.items():
        berkas = next(iter(sorted(Path(folder).glob(f"{kode}-*.md"))), None)
        if berkas is None:
            print(f"{kode:8s}{judul:30s}{'-':>6s}  BELUM ADA BERKAS")
            continue
        teks = berkas.read_text(encoding="utf-8")
        semua_teks += teks
        kata, isi, bukti = analisis(teks)
        masalah = [
            m for ok, m in (
                (kata >= MIN_KATA, f"kurang kata (<{MIN_KATA})"),
                (not isi, "masih ada [ISI]"),
                (bukti, "belum ada bukti"),
            ) if not ok
        ]
        status = "SELESAI" if not masalah else ", ".join(masalah)
        if not masalah:
            selesai += 1
        print(f"{kode:8s}{judul:30s}{kata:>6d}  {status}")
    print(f"\nSubbab selesai: {selesai}/6 = {100 * selesai // 6}%")
    print("SIAP progress check" if selesai >= 5 else "BELUM mencapai 80%")

    if prd and Path(prd).exists():
        kode_prd = set()
        import re
        for baris in Path(prd).read_text(encoding="utf-8").splitlines():
            kode_prd.update(re.findall(r"KF-\d+", baris))
        kode_draf = set(re.findall(r"KF-\d+", semua_teks))
        asing = sorted(kode_draf - kode_prd)
        print("KF pada draf yang tidak ada di PRD:", ", ".join(asing) if asing else "tidak ada")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Pemakaian: python alat/periksa_draf.py docs/bab4 PRD.md")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
