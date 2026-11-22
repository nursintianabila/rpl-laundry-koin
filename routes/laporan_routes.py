from flask import Blueprint, render_template, request

from services import auth_service, laporan_service

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
