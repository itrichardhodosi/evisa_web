# manage.py
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Carga las variables de entorno desde el .env en la carpeta del proyecto
load_dotenv(Path(__file__).resolve().parent / ".env")

def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "evisa_web.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django..."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
