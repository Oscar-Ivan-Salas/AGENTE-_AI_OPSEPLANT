import os
from dotenv import load_dotenv

load_dotenv()

# Variables de entorno
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Carpetas de almacenamiento
BASE_DIR = "data"
LOGO_PATH = os.path.join("assets", "logo.jpg")
PLANTILLA_WORD_PATH = os.path.join("assets", "Plantilla_Reporte_OPSEPLANT_con_fotos.docx")

