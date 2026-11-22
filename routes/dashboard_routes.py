from flask import Blueprint, abort, g, render_template, request

from services import auth_service, dashboard_service, ekspor_service, transaksi_service

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


@bp.route("/dashboard/ekspor")
@auth_service.peran_diperlukan("Pemilik")
def ekspor():
    """Mengunduh daftar transaksi sebagai CSV atau PDF."""
    format_ekspor = request.args.get("format", "csv").lower()
    if format_ekspor not in ("csv", "pdf"):
        abort(400)

    baris = transaksi_service.daftar_transaksi()
    statistik = dashboard_service.statistik()

    if format_ekspor == "csv":
        return ekspor_service.buat_csv(baris, statistik)
    return ekspor_service.buat_pdf(baris, statistik)
