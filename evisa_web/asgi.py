"""
ASGI config for evisa_web project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""
import os
from pathlib import Path
import dotenv

# Leer .env
dotenv.read_dotenv(Path(__file__).resolve().parent.parent / ".env")
# Definir settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.getenv("DJANGO_SETTINGS_MODULE"))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
