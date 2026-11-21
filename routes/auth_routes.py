from flask import Blueprint, abort, flash, redirect, render_template, request, url_for

from services import auth_service

bp = Blueprint("auth", __name__)


@bp.route("/login", methods=["GET", "POST"])
def login():
    """Menampilkan dan memproses form login."""
    if request.method == "POST":
        username = request.form.get("username_email", "")
        kata_sandi = request.form.get("password", "")
        pengguna = auth_service.autentikasi(username, kata_sandi)
        if pengguna is None:
            flash("Nama pengguna atau kata sandi salah.", "galat")
        else:
            auth_service.login_pengguna(pengguna)
            next_url = auth_service.alamat_next_aman(request.args.get("next"))
            if next_url:
                return redirect(next_url)
            if pengguna["nama_peran"] == "Pemilik":
                return redirect(url_for("layanan.daftar"))
            return redirect(url_for("transaksi.daftar"))

    return render_template("auth/login.html", next=request.args.get("next", ""))


@bp.route("/logout", methods=["POST"])
def logout():
    """Mengosongkan sesi dan kembali ke login."""
    auth_service.logout_pengguna()
    flash("Anda telah keluar.", "sukses")
    return redirect(url_for("auth.login"))


@bp.route("/")
def beranda():
    """Halaman beranda mengarahkan pengguna sesuai peran."""
    from flask import g

    if g.pengguna is None:
        return redirect(url_for("auth.login"))
    if g.pengguna["nama_peran"] == "Pemilik":
        return redirect(url_for("layanan.daftar"))
    return redirect(url_for("transaksi.daftar"))
