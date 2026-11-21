import os

from flask import Flask, abort, g, render_template, request

import models
from routes import auth_routes, layanan_routes, pelanggan_routes, transaksi_routes
from services import auth_service


def buat_aplikasi():
    """Membuat dan mengatur aplikasi Flask."""
    app = Flask(__name__)

    env = os.environ.get("FLASK_ENV", "development")
    secret = os.environ.get("SECRET_KEY")
    if env == "production" and not secret:
        raise RuntimeError("SECRET_KEY wajib diisi pada mode produksi.")
    app.secret_key = secret or os.urandom(24)

    app.config["SESSION_COOKIE_HTTPONLY"] = True
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
    app.config["SESSION_COOKIE_SECURE"] = (env == "production")

    models.init_db()
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(layanan_routes.bp)
    app.register_blueprint(pelanggan_routes.bp)
    app.register_blueprint(transaksi_routes.bp)

    @app.before_request
    def muat_pengguna():
        auth_service.muat_pengguna_dari_sesi()

    @app.before_request
    def cek_csrf():
        if request.method == "POST":
            token = request.form.get("csrf_token") or request.headers.get("X-CSRFToken")
            if not auth_service.verifikasi_csrf(token):
                abort(400)

    @app.context_processor
    def suntik_csrf():
        return {"csrf_token": auth_service.csrf_token}

    @app.errorhandler(403)
    def akses_ditolak(kesalahan):
        return render_template("errors/403.html"), 403

    @app.template_filter("rupiah")
    def format_rupiah(nilai):
        """Menampilkan bilangan bulat sebagai rupiah, mis. 10000 -> Rp 10.000."""
        return "Rp {:,}".format(int(nilai)).replace(",", ".")

    @app.after_request
    def header_keamanan(response):
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        return response

    return app


app = buat_aplikasi()


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
