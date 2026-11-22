from flask import Blueprint, render_template

from services import auth_service, dashboard_service

bp = Blueprint("dashboard", __name__)


@bp.route("/dashboard")
@auth_service.peran_diperlukan("Pemilik")
def indeks():
    """Menampilkan ringkasan usaha untuk Pemilik."""
    statistik = dashboard_service.statistik()
    return render_template("dashboard/indeks.html", statistik=statistik)
