# pps_python_git_docker

## La Bayeta de la Fortuna

Aplicación al estilo de la galleta de la fortuna con mensajes personalizados.

## Instalación y Entorno

Para garantizar que la aplicación funciona correctamente sin conflictos de versiones, utilizamos un entorno virtual. Sigue estos pasos para configurarlo:

### 1. Preparar el entorno
Primero, crea y activa un entorno virtual de Python. En el mismo directorio donde se encuentra el archivo app.py, ejecuta:

**En Windows:**
```bash
python -m venv nombre_entorno
.\nombre_entorno\Scripts\activate
```

**En Linux:**
```bash
python3 -m venv nombre_entorno
source nombre_entorno/bin/activate
```

### 2. Instalar dependencias
Una vez activado el entorno virtual, instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

### 3. Ejecutar la aplicación
Una vez instaladas las dependencias, puedes ejecutar la aplicación:

```bash
python app.py
```