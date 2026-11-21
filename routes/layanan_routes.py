from flask import Blueprint, redirect, render_template, url_for

bp = Blueprint("layanan", __name__)


@bp.route("/")
def beranda():
    """Halaman beranda mengalihkan pengguna ke daftar layanan."""
    return redirect(url_for("layanan.daftar"))


@bp.route("/layanan")
def daftar():
    """Menampilkan halaman daftar layanan."""
    return render_template("layanan/daftar.html")