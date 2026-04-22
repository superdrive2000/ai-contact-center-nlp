# Imagen base
FROM python:3.10-slim

# Evitar prompts interactivos
ENV DEBIAN_FRONTEND=noninteractive

# Instalar ffmpeg (CLAVE para Whisper)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

# Crear carpeta de trabajo
WORKDIR /app

# Copiar archivos
COPY . .

# Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Descargar modelo Whisper (opcional pero recomendado)
RUN python -c "import whisper; whisper.load_model('base')"

# Exponer puertos
EXPOSE 5000
EXPOSE 8000

# Ejecutar app
CMD ["python", "app.py"]