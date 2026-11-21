import os

from flask import Flask

import models
from routes import layanan_routes


def buat_aplikasi():
    """Membuat dan mengatur aplikasi Flask."""
    app = Flask(__name__)

    # Kunci rahasia diambil dari variabel lingkungan. Bila tidak diatur,
    # gunakan nilai acak agar tidak ada kunci rahasia yang tertulis di kode.
    app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

    models.init_db()
    app.register_blueprint(layanan_routes.bp)

    @app.template_filter("rupiah")
    def format_rupiah(nilai):
        """Menampilkan bilangan bulat sebagai rupiah, mis. 10000 -> Rp 10.000."""
        return "Rp {:,}".format(int(nilai)).replace(",", ".")

    return app


app = buat_aplikasi()


if __name__ == "__main__":
    # Mode debug hanya aktif bila FLASK_DEBUG=1, tidak aktif secara bawaan.
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")