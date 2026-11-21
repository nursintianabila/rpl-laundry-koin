from datetime import date

from flask import Blueprint, abort, flash, redirect, render_template, request, url_for

from services import transaksi_service

bp = Blueprint("transaksi", __name__)


@bp.route("/transaksi")
def daftar():
    """Menampilkan halaman daftar transaksi dengan pencarian dan penyaringan."""
    kata = request.args.get("q", "").strip()
    layanan_teks = request.args.get("layanan", "").strip()
    id_layanan = int(layanan_teks) if layanan_teks.isdigit() else None

    daftar_transaksi = transaksi_service.daftar_transaksi(kata, id_layanan)
    daftar_layanan = transaksi_service.daftar_layanan()

    return render_template(
        "transaksi/daftar.html",
        daftar_transaksi=daftar_transaksi,
        kata=kata,
        id_layanan_terpilih=id_layanan,
        daftar_layanan=daftar_layanan,
        ada_pencarian=bool(kata or id_layanan),
    )


@bp.route("/transaksi/tambah", methods=["GET", "POST"])
def tambah():
    """Menampilkan dan memproses form tambah transaksi."""
    isian = {
        "id_pelanggan": "",
        "id_layanan": "",
        "tanggal": date.today().isoformat(),
        "berat": "",
    }
    galat = []

    if request.method == "POST":
        isian["id_pelanggan"] = request.form.get("id_pelanggan", "")
        isian["id_layanan"] = request.form.get("id_layanan", "")
        isian["tanggal"] = request.form.get("tanggal", "")
        isian["berat"] = request.form.get("berat", "")
        try:
            transaksi_service.tambah_transaksi(
                isian["id_pelanggan"],
                isian["id_layanan"],
                isian["tanggal"],
                isian["berat"],
            )
        except transaksi_service.ValidasiTransaksiError as kesalahan:
            galat = kesalahan.daftar_pesan
        else:
            flash("Transaksi berhasil ditambahkan.", "sukses")
            return redirect(url_for("transaksi.daftar"))

    daftar_pelanggan = transaksi_service.daftar_pelanggan()
    daftar_layanan = transaksi_service.daftar_layanan()

    return render_template(
        "transaksi/form.html",
        judul="Tambah Transaksi",
        aksi=url_for("transaksi.tambah"),
        isian=isian,
        galat=galat,
        daftar_pelanggan=daftar_pelanggan,
        daftar_layanan=daftar_layanan,
    )


@bp.route("/transaksi/<int:id_transaksi>/hapus", methods=["POST"])
def hapus(id_transaksi):
    """Menghapus transaksi setelah konfirmasi melalui POST."""
    if transaksi_service.ambil_transaksi(id_transaksi) is None:
        abort(404)

    transaksi_service.hapus_transaksi(id_transaksi)
    flash("Transaksi berhasil dihapus.", "sukses")
    return redirect(url_for("transaksi.daftar"))
