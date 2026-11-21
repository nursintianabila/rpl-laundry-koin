import os

from flask import Flask, abort, g, render_template

import models
from routes import auth_routes, layanan_routes, pelanggan_routes, transaksi_routes
from services import auth_service


def buat_aplikasi():
    """Membuat dan mengatur aplikasi Flask."""
    app = Flask(__name__)

    app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

    models.init_db()
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(layanan_routes.bp)
    app.register_blueprint(pelanggan_routes.bp)
    app.register_blueprint(transaksi_routes.bp)

    @app.before_request
    def muat_pengguna():
        auth_service.muat_pengguna_dari_sesi()

    @app.errorhandler(403)
    def akses_ditolak(kesalahan):
        return render_template("errors/403.html"), 403

    @app.template_filter("rupiah")
    def format_rupiah(nilai):
        """Menampilkan bilangan bulat sebagai rupiah, mis. 10000 -> Rp 10.000."""
        return "Rp {:,}".format(int(nilai)).replace(",", ".")

    return app


app = buat_aplikasi()


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
