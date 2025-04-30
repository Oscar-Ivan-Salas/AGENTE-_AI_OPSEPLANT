import os
from datetime import datetime
from config import BASE_DIR

def crear_directorio_base(nombre_supervisor: str):
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    ruta_base = os.path.join(BASE_DIR, nombre_supervisor, fecha_actual)
    ruta_fotos = os.path.join(ruta_base, "fotos")

    os.makedirs(ruta_fotos, exist_ok=True)
    return ruta_base, ruta_fotos

def guardar_texto(ruta_base: str, texto: str):
    archivo_texto = os.path.join(ruta_base, "avance.txt")
    with open(archivo_texto, "a", encoding="utf-8") as f:
        f.write(texto + "\n\n")

def guardar_foto(ruta_fotos: str, datos: bytes, nombre_archivo: str):
    ruta_foto = os.path.join(ruta_fotos, nombre_archivo)
    with open(ruta_foto, "wb") as f:
        f.write(datos)
