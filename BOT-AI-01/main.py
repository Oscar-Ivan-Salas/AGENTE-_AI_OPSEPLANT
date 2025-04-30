import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv

from gpt_agent import responder_chat, analizar_avance
from file_manager import crear_directorio_base, guardar_texto, guardar_foto
from report_generator import generar_reporte

# Cargar variables de entorno
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Manejador principal de mensajes
async def manejar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    nombre = user.full_name
    texto = update.message.text or ""
    fotos = update.message.photo

    respuesta_gpt, accion = responder_chat(nombre, texto)
    await update.message.reply_text(respuesta_gpt)

    if accion == "registrar_avance":
        ruta_base, ruta_fotos = crear_directorio_base(nombre)
        guardar_texto(ruta_base, texto)

        if fotos:
            for i, photo in enumerate(fotos):
                archivo = await photo.get_file()
                datos = await archivo.download_as_bytearray()
                guardar_foto(ruta_fotos, datos, f"foto_{i+1}.jpg")

        resumen = analizar_avance(texto)
        reporte_path = generar_reporte(ruta_base, resumen, nombre)

        with open(reporte_path, "rb") as doc:
            await update.message.reply_document(document=doc, filename="Reporte_OPSEPLANT.docx")

    elif accion == "agregar_a_avance":
        await update.message.reply_text("📌 Avance agregado. Puedes seguir enviando fotos o detalles.")

# Iniciar el bot
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT | filters.PHOTO, manejar_mensaje))
    print("🤖 BOT OPSEPLANT activo con ApplicationBuilder...")
    app.run_polling()

if __name__ == '__main__':
    main()
    
