# Imagen base de Python
FROM python:3.10-slim

# Directorio de trabajo
WORKDIR /app

# Copiar archivos al contenedor
COPY . .

# Comando para ejecutar el programa enviando una versión automática
# Esto evita que el build se quede pegado esperando el input
CMD ["sh", "-c", "echo 'v1.0.0-PROD' | python app.py"]