from flask import Blueprint, abort, flash, redirect, render_template, request, url_for

from services import auth_service, pelanggan_service

bp = Blueprint("pelanggan", __name__)


@bp.route("/pelanggan")
@auth_service.peran_diperlukan("Admin/Operator")
def daftar():
    """Menampilkan halaman daftar pelanggan."""
    daftar_pelanggan = pelanggan_service.daftar_pelanggan()
    return render_template("pelanggan/daftar.html", daftar_pelanggan=daftar_pelanggan)


@bp.route("/pelanggan/tambah", methods=["GET", "POST"])
@auth_service.peran_diperlukan("Admin/Operator")
def tambah():
    """Menampilkan dan memproses form tambah pelanggan."""
    isian = {"nama_pelanggan": ""}
    galat = []

    if request.method == "POST":
        isian["nama_pelanggan"] = request.form.get("nama_pelanggan", "")
        try:
            pelanggan_service.tambah_pelanggan(isian["nama_pelanggan"])
        except pelanggan_service.ValidasiPelangganError as kesalahan:
            galat = kesalahan.daftar_pesan
        else:
            flash("Pelanggan berhasil ditambahkan.", "sukses")
            return redirect(url_for("pelanggan.daftar"))

    return render_template(
        "pelanggan/form.html",
        judul="Tambah Pelanggan",
        aksi=url_for("pelanggan.tambah"),
        isian=isian,
        galat=galat,
    )


@bp.route("/pelanggan/<int:id_pelanggan>/ubah", methods=["GET", "POST"])
@auth_service.peran_diperlukan("Admin/Operator")
def ubah(id_pelanggan):
    """Menampilkan dan memproses form ubah pelanggan."""
    pelanggan = pelanggan_service.ambil_pelanggan(id_pelanggan)
    if pelanggan is None:
        abort(404)

    isian = {"nama_pelanggan": pelanggan["nama_pelanggan"]}
    galat = []

    if request.method == "POST":
        isian["nama_pelanggan"] = request.form.get("nama_pelanggan", "")
        try:
            pelanggan_service.ubah_pelanggan(id_pelanggan, isian["nama_pelanggan"])
        except pelanggan_service.ValidasiPelangganError as kesalahan:
            galat = kesalahan.daftar_pesan
        else:
            flash("Pelanggan berhasil diubah.", "sukses")
            return redirect(url_for("pelanggan.daftar"))

    return render_template(
        "pelanggan/form.html",
        judul="Ubah Pelanggan",
        aksi=url_for("pelanggan.ubah", id_pelanggan=id_pelanggan),
        isian=isian,
        galat=galat,
    )


@bp.route("/pelanggan/<int:id_pelanggan>/hapus", methods=["POST"])
@auth_service.peran_diperlukan("Admin/Operator")
def hapus(id_pelanggan):
    """Menghapus pelanggan setelah konfirmasi melalui POST."""
    if pelanggan_service.ambil_pelanggan(id_pelanggan) is None:
        abort(404)

    try:
        pelanggan_service.hapus_pelanggan(id_pelanggan)
    except pelanggan_service.PelangganDipakaiError as kesalahan:
        flash(str(kesalahan), "galat")
    else:
        flash("Pelanggan berhasil dihapus.", "sukses")

    return redirect(url_for("pelanggan.daftar"))
