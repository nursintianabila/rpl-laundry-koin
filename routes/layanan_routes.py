from flask import Blueprint, redirect, render_template, url_for

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
