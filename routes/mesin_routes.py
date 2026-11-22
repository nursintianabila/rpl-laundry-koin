from flask import Blueprint, abort, flash, redirect, render_template, request, url_for

from services import auth_service, mesin_service

bp = Blueprint("mesin", __name__)


@bp.route("/mesin")
@auth_service.peran_diperlukan("Admin/Operator")
def daftar():
    """Menampilkan daftar mesin dan formulir status."""
    return render_template("mesin/daftar.html", daftar_mesin=mesin_service.daftar_mesin())


@bp.route("/mesin/<int:id_mesin>/status", methods=["POST"])
@auth_service.peran_diperlukan("Admin/Operator")
def ubah_status(id_mesin):
    """Menyimpan status mesin baru."""
    if mesin_service.ambil_mesin(id_mesin) is None:
        abort(404)
    try:
        mesin_service.ubah_status(id_mesin, request.form.get("status_mesin", ""))
    except mesin_service.ValidasiMesinError as kesalahan:
        for pesan in kesalahan.daftar_pesan:
            flash(pesan, "galat")
    else:
        flash("Status mesin berhasil diperbarui.", "sukses")
    return redirect(url_for("mesin.daftar"))
