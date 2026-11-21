"""Rekap Jurnal Vibe Coding.

    python alat/analisis_jurnal.py jurnal/*.md

Setiap berkas jurnal berisi tabel Markdown dengan kolom:
    | No | Tujuan | Prompt | Hasil AI | Keputusan | Alasan |

Keputusan diawali Terima / Ubah / Tolak.
Tag pada kolom Tujuan atau Alasan, mis. [Debug], [Keamanan].
Jenis galat AI ditulis [Galat: acuan-salah], [Galat: aturan-bisnis], dst.
"""
import re
import sys
from collections import Counter
from pathlib import Path

KEPUTUSAN = ("terima", "ubah", "tolak")


def baca_entri(berkas):
    """Kembalikan daftar entri (dict nama-kolom -> isi) dari satu berkas jurnal."""
    entri, kolom = [], None
    for baris in Path(berkas).read_text(encoding="utf-8").splitlines():
        if not baris.strip().startswith("|"):
            continue
        sel = [s.strip() for s in baris.strip().strip("|").split("|")]
        if all(set(s) <= set("-: ") for s in sel):
            continue
        if kolom is None:
            nama = [s.lower() for s in sel]
            if "keputusan" in nama:
                kolom = {n: i for i, n in enumerate(nama)}
            continue
        if len(sel) >= len(kolom):
            entri.append({n: sel[i] for n, i in kolom.items()})
    return entri


def rekap(entri):
    """Hitung keputusan, tag, dan jenis galat AI."""
    keputusan, tag, galat = Counter(), Counter(), Counter()
    for e in entri:
        k = e.get("keputusan", "").lower()
        keputusan[next((x for x in KEPUTUSAN if k.startswith(x)), "lain")] += 1
        for t in re.findall(r"\[([^\]]+)\]", e.get("tujuan", "") + " " + e.get("alasan", "")):
            if t.lower().startswith("galat:"):
                galat[t.split(":", 1)[1].strip().lower()] += 1
            else:
                tag[t.lower()] += 1
    return keputusan, tag, galat


def persen(n, total):
    return f"{100 * n / total:.1f}%" if total else "-"


def cetak(judul, entri):
    total = len(entri)
    keputusan, tag, galat = rekap(entri)
    print(f"\n=== {judul} ===")
    print(f"{'Keputusan':12s}{'Jumlah':>8s}{'Persen':>10s}")
    for k in KEPUTUSAN:
        print(f"{k.capitalize():12s}{keputusan[k]:>8d}{persen(keputusan[k], total):>10s}")
    print(f"{'Total':12s}{total:>8d}{'100%':>10s}")
    print("Tag:", ", ".join(f"{n} {v}" for n, v in sorted(tag.items())) or "-")
    print("Jenis galat AI:", ", ".join(f"{n} {v}" for n, v in sorted(galat.items())) or "-")
    print(f"Entri bertag galat: {sum(galat.values())}")


def main(berkas):
    semua = []
    for nama in berkas:
        e = baca_entri(nama)
        cetak(Path(nama).name, e)
        semua.extend(e)
    cetak("GABUNGAN", semua)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Pemakaian: python alat/analisis_jurnal.py jurnal/*.md")
        sys.exit(1)
    main(sys.argv[1:])
