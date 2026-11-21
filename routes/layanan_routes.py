from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from services import auth_service, layanan_service

bp = Blueprint("layanan", __name__)


@bp.route("/")
def beranda():
    """Halaman beranda mengalihkan pengguna ke daftar layanan."""
    return redirect(url_for("layanan.daftar"))


@bp.route("/layanan")
@auth_service.peran_diperlukan("Pemilik", "Admin/Operator")
def daftar():
    """Menampilkan halaman daftar layanan."""
    daftar_layanan = layanan_service.daftar_layanan()
    return render_template("layanan/daftar.html", daftar_layanan=daftar_layanan)


@bp.route("/layanan/tambah", methods=["GET", "POST"])
@auth_service.peran_diperlukan("Pemilik")
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
            flash("Layanan berhasil ditambahkan.", "sukses")
            return redirect(url_for("layanan.daftar"))

    return render_template(
        "layanan/form.html",
        judul="Tambah Layanan",
        aksi=url_for("layanan.tambah"),
        isian=isian,
        galat=galat,
    )


@bp.route("/layanan/<int:id_layanan>/ubah", methods=["GET", "POST"])
@auth_service.peran_diperlukan("Pemilik")
def ubah(id_layanan):
    """Menampilkan dan memproses form ubah layanan."""
    layanan = layanan_service.ambil_layanan(id_layanan)
    if layanan is None:
        abort(404)

    isian = {
        "nama_layanan": layanan["nama_layanan"],
        "harga": layanan["harga"],
    }
    galat = []

    if request.method == "POST":
        isian["nama_layanan"] = request.form.get("nama_layanan", "")
        isian["harga"] = request.form.get("harga", "")
        try:
            layanan_service.ubah_layanan(
                id_layanan,
                isian["nama_layanan"],
                isian["harga"],
            )
        except layanan_service.ValidasiLayananError as kesalahan:
            galat = kesalahan.daftar_pesan
        else:
            flash("Layanan berhasil diubah.", "sukses")
            return redirect(url_for("layanan.daftar"))

    return render_template(
        "layanan/form.html",
        judul="Ubah Layanan",
        aksi=url_for("layanan.ubah", id_layanan=id_layanan),
        isian=isian,
        galat=galat,
    )


@bp.route("/layanan/<int:id_layanan>/hapus", methods=["POST"])
@auth_service.peran_diperlukan("Pemilik")
def hapus(id_layanan):
    """Menghapus layanan setelah konfirmasi melalui POST."""
    if layanan_service.ambil_layanan(id_layanan) is None:
        abort(404)

    try:
        layanan_service.hapus_layanan(id_layanan)
    except layanan_service.LayananDipakaiError as kesalahan:
        flash(str(kesalahan), "galat")
    else:
        flash("Layanan berhasil dihapus.", "sukses")

    return redirect(url_for("layanan.daftar"))
