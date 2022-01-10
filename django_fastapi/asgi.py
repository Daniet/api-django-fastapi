"""
ASGI config for django_fastapi project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.apps import apps
from django.conf import settings
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_fastapi.settings')
apps.populate(settings.INSTALLED_APPS)

from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from starlette.middleware.cors import CORSMiddleware

from characters.endpoints import routes_characters

def get_application() -> FastAPI:
    app = FastAPI(title="Characters", debug=settings.DEBUG)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(routes_characters, prefix="/characters")
    app.mount("/", WSGIMiddleware(get_wsgi_application()))

    return app

app = get_application()
