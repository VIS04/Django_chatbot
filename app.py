"""Alias WSGI entrypoint so Render's default `gunicorn app:app` start command works."""
from config.wsgi import application

app = application

