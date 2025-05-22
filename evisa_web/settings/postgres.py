# evisa_web/settings/postgres.py
from .base import *
import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("PG_DB"),
        "USER": os.getenv("PG_USER"),
        "PASSWORD": os.getenv("PG_PASSWORD"),
        "HOST": os.getenv("PG_HOST"),
        "PORT": os.getenv("PG_PORT"),
    }
}
