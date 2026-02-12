# -------- FASE 1: Construcción / dependencias --------
FROM python:3.11-slim AS builder

WORKDIR /app

# Copiamos requirements
COPY requirements.txt .

# Instalamos dependencias en un directorio aislado
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# -------- FASE 2: Ejecución --------
FROM python:3.11-slim

WORKDIR /app

# Copiamos solo lo necesario desde la fase anterior
COPY --from=builder /install /usr/local
COPY . .

# Exponemos el puerto del servidor Flask
EXPOSE 5000

# Comando de ejecución
CMD ["python", "app.py"]
