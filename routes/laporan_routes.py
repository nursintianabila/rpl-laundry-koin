from flask import Blueprint, abort, render_template, request

from services import auth_service, ekspor_service, laporan_service

bp = Blueprint("laporan", __name__)


@bp.route("/laporan")
@auth_service.peran_diperlukan("Pemilik")
def pendapatan():
    """Menampilkan laporan pendapatan dengan rentang tanggal opsional."""
    mulai = request.args.get("mulai", "")
    akhir = request.args.get("akhir", "")
    galat = None
    data = {
        "mulai": None,
        "akhir": None,
        "ringkasan": None,
        "per_layanan": [],
    }

    try:
        data = laporan_service.ringkasan(mulai, akhir)
    except laporan_service.ValidasiPeriodeError as kesalahan:
        galat = kesalahan.pesan

    return render_template(
        "laporan/pendapatan.html",
        data=data,
        mulai=mulai,
        akhir=akhir,
        galat=galat,
    )


@bp.route("/laporan/ekspor")
@auth_service.peran_diperlukan("Pemilik")
def ekspor():
    """Mengunduh laporan transaksi sesuai periode sebagai CSV atau PDF."""
    format_ekspor = request.args.get("format", "csv").lower()
    if format_ekspor not in ("csv", "pdf"):
        abort(400)

    mulai = request.args.get("mulai", "")
    akhir = request.args.get("akhir", "")
    try:
        data = laporan_service.ringkasan(mulai, akhir)
    except laporan_service.ValidasiPeriodeError:
        abort(400)

    baris = laporan_service.daftar_transaksi(data["mulai"], data["akhir"])
    if format_ekspor == "csv":
        return ekspor_service.buat_csv(baris, data["ringkasan"])
    return ekspor_service.buat_pdf(baris, data["ringkasan"])
