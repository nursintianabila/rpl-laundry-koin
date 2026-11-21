from flask import Blueprint, flash, redirect, render_template, request, url_for

from services import layanan_service

bp = Blueprint("layanan", __name__)


@bp.route("/")
def beranda():
    """Halaman beranda mengalihkan pengguna ke daftar layanan."""
    return redirect(url_for("layanan.daftar"))


@bp.route("/layanan")
def daftar():
    """Menampilkan halaman daftar layanan."""
    daftar_layanan = layanan_service.daftar_layanan()
    return render_template("layanan/daftar.html", daftar_layanan=daftar_layanan)


@bp.route("/layanan/tambah", methods=["GET", "POST"])
def tambah():
    """Menampilkan dan memproses form tambah layanan."""
    isian = {"nama_layanan": "", "harga": ""}
    galat = []

    if request.method == "POST":
        isian["nama_layanan"] = request.form.get("nama_layanan", "")
        isian["harga"] = request.form.get("harga", "")
        try:
            layanan_service.tambah_layanan(isian["nama_layanan"], isian["harga"])
        except layanan_service.ValidasiLayananError as kesalahan:
            galat = kesalahan.daftar_pesan
        else:
            flash("Layanan berhasil ditambahkan.")
            return redirect(url_for("layanan.daftar"))

    return render_template(
        "layanan/form.html",
        judul="Tambah Layanan",
        aksi=url_for("layanan.tambah"),
        isian=isian,
        galat=galat,
    )
