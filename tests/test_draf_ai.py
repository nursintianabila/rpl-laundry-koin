"""Draf uji pytest dari AI (Jobsheet 13 Langkah 5).

Dijalankan: python -m pytest tests/test_draf_ai.py -v
"""
import tempfile
from pathlib import Path

import pytest

import models
import app as aplikasi
from services import auth_service


@pytest.fixture
def client():
    folder = tempfile.TemporaryDirectory()
    models.DB_PATH = Path(folder.name) / "uji.db"
    models.init_db()
    auth_service.buat_pengguna("pemilik@example.com", "pemilik123", "Pemilik")
    auth_service.buat_pengguna("admin@example.com", "admin123", "Admin/Operator")
    a = aplikasi.buat_aplikasi()
    a.config.update(TESTING=True)
    with a.test_client() as c:
        with c.session_transaction() as sess:
            sess["csrf_token"] = "test-token"
        yield c
    folder.cleanup()


def test_tamu_dialihkan_ke_login(client):
    r = client.get("/layanan")
    assert r.status_code == 302
    assert "/login" in r.headers["Location"]


def test_login_berhasil(client):
    r = client.post(
        "/login",
        data={"username_email": "pemilik@example.com", "password": "pemilik123", "csrf_token": "test-token"},
        follow_redirects=True,
    )
    assert r.status_code == 200
    assert "Layanan" in r.text


def test_login_salah(client):
    r = client.post(
        "/login",
        data={"username_email": "pemilik@example.com", "password": "salah", "csrf_token": "test-token"},
        follow_redirects=True,
    )
    assert "Nama pengguna atau kata sandi salah." in r.text


def test_peran_terbatas_403(client):
    client.post(
        "/login",
        data={"username_email": "pemilik@example.com", "password": "pemilik123", "csrf_token": "test-token"},
        follow_redirects=True,
    )
    r = client.get("/pelanggan")
    assert r.status_code == 403


def test_csrf_tanpa_token_400(client):
    client.post(
        "/login",
        data={"username_email": "admin@example.com", "password": "admin123", "csrf_token": "test-token"},
        follow_redirects=True,
    )
    r = client.post("/pelanggan/1/hapus", data={})
    assert r.status_code == 400


def test_header_keamanan(client):
    r = client.get("/login")
    assert r.headers.get("X-Content-Type-Options") == "nosniff"
    assert r.headers.get("X-Frame-Options") == "DENY"
