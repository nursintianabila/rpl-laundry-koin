from flask import Blueprint, g, render_template

from services import auth_service, dashboard_service

bp = Blueprint("dashboard", __name__)


@bp.route("/dashboard")
@auth_service.peran_diperlukan("Pemilik", "Admin/Operator")
def indeks():
    """Menampilkan ringkasan usaha dan notifikasi sesuai peran."""
    statistik = dashboard_service.statistik()
    notifikasi = (
        dashboard_service.notifikasi_admin()
        if g.pengguna["nama_peran"] == "Admin/Operator"
        else []
    )
    return render_template(
        "dashboard/indeks.html",
        statistik=statistik,
        notifikasi=notifikasi,
    )
