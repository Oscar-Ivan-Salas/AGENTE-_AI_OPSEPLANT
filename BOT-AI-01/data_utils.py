import os
from telegram import Update
from telegram.ext import ContextTypes

# Esta función guarda el archivo que el supervisor envía
async def descargar_archivo(update: Update, carpeta_destino: str, nombre_archivo: str):
    archivo = await update.message.document.get_file()
    contenido = await archivo.download_as_bytearray()
    path = os.path.join(carpeta_destino, nombre_archivo)
    with open(path, "wb") as f:
        f.write(contenido)
    return path

# Esta función procesa un mensaje recibido
async def procesar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Recibido, procesando tu información... (esto es un mock de ejemplo)")
