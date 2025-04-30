import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Determinar intención del mensaje
def responder_chat(nombre: str, mensaje: str) -> tuple[str, str]:
    prompt = f"""
Eres un agente AI de OPSEPLANT que asiste al supervisor "{nombre}" en el registro de avances de obra.

Tu tarea es:
1. Saludar si el mensaje es un saludo.
2. Detectar si el mensaje contiene un avance diario de trabajo.
3. Si el mensaje indica que desea continuar con un avance anterior, marcar como "agregar_a_avance".
4. Si no es relevante, ignóralo.

Ejemplos de respuestas:

- "Hola, ¿cómo estás?" → ("👋 ¡Hola {nombre}! ¿Qué avance deseas reportar hoy?", "esperando_avance")
- "Hoy se instaló el tablero eléctrico en el área 2." → ("✅ Avance registrado. ¿Deseas agregar fotos o más detalles?", "registrar_avance")
- "Quiero añadir más fotos del mismo trabajo." → ("📎 Claro, agrega las imágenes que desees.", "agregar_a_avance")
- "Estoy de vacaciones" → ("Gracias por avisar. ¡Que disfrutes!", "ignorar")

Ahora responde de forma apropiada al siguiente mensaje:
Supervisor: {nombre}
Mensaje: {mensaje}
Respuesta:
"""

    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.5,
        )

        texto = respuesta.choices[0].message.content.strip()
        partes = texto.split("||")
        if len(partes) == 2:
            return partes[0].strip(), partes[1].strip()
        else:
            # Fallback: si no se usa "||", usar lógica básica
            if "agregar" in texto.lower():
                return texto, "agregar_a_avance"
            elif "registrado" in texto.lower():
                return texto, "registrar_avance"
            else:
                return texto, "ignorar"

    except Exception as e:
        return f"❌ Error al analizar el mensaje: {e}", "ignorar"

# Analizar contenido para resumen
def analizar_avance(texto: str) -> str:
    prompt = f"""
Extrae un resumen profesional del siguiente texto de avance técnico para incluirlo en un informe de obra.

Texto:
\"\"\"
{texto}
\"\"\"

Resumen:
"""

    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.3,
        )
        return respuesta.choices[0].message.content.strip()
    except Exception as e:
        return f"Error al generar resumen: {e}"

