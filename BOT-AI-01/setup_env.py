import os

print("⚙️ Eliminando paquetes innecesarios...")
os.system("pip uninstall -y python-telegram-bot telegram")
os.system("pip install python-telegram-bot==20.3")
os.system("pip install python-dotenv python-docx requests openai")

print("✅ Entorno limpio y dependencias correctas instaladas.")
