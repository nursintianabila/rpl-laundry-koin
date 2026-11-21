"""Hitung skor SUS (System Usability Scale).

Jalankan: python docs/uat/hitung_sus.py

Isi JAWABAN dengan satu daftar 10 angka (1-5) per responden,
sesuai urutan butir 1-10 pada docs/uat/form-sus.md.
"""

JAWABAN = {
    # "Nama responden": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
}


def skor_sus(jawaban):
    """Mengembalikan skor SUS 0-100 dari sepuluh jawaban (1-5)."""
    assert len(jawaban) == 10 and all(1 <= x <= 5 for x in jawaban), \
        "harus 10 jawaban bernilai 1-5"
    jumlah = sum(
        (x - 1) if i % 2 == 0 else (5 - x)
        for i, x in enumerate(jawaban)
    )
    return jumlah * 2.5


if __name__ == "__main__":
    assert skor_sus([4, 2, 4, 1, 4, 2, 5, 2, 4, 1]) == 82.5
    assert skor_sus([3] * 10) == 50.0

    if not JAWABAN:
        print("Belum ada jawaban. Isi JAWABAN dengan data responden UAT.")
    else:
        skor = {nama: skor_sus(j) for nama, j in JAWABAN.items()}
        for nama, nilai in skor.items():
            print(f"{nama:20s} {nilai:5.1f}")
        print(f"{'Rata-rata':20s} {sum(skor.values()) / len(skor):5.1f}")
