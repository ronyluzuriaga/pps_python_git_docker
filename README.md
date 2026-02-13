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
### 3. Docker
Se ha creado un compose.yaml que levante el docker necesario para el correcto funcionamiento de las funciones. Para levantarlos se usará el comando:

```bash
docker compose up --build
```
Con ello tendremos nuestra base de datos lista para guardar nuestras frases auspiciosas.

### 4. Configuración de Frases
Para disponer siempre de frases en la base de datos, se ha configurado que, al iniciar el app.py se cargarán las frases de frases.txt

Puedes añadir tantas frases como quieras desde el nuevo endpoint.

### 5. Ejecutar la aplicación
Una vez instaladas las dependencias y creado el fichero de texto, ejecuta el servidor:

```bash
python app.py
```
Verás un mensaje indicando que el servidor está corriendo (generalmente en http://127.0.0.1:5000 o localhost).

### Cómo usar la API
Una vez la aplicación esté ejecutándose, abre tu navegador web y prueba las siguientes rutas:

Página de inicio: http://localhost:5000/ (Debería mostrar "Hola, mundo")

Obtener frases de la fortuna: Usa la ruta /frotar/<número> para obtener una lista de frases aleatorias.

Ejemplo para obtener 3 frases: http://localhost:5000/frotar/3

Devolverá una respuesta en formato JSON:

```json
{
  "frases": [
    "El éxito es como un fantasma, muchos hablan de él, pero pocos lo han visto de verdad",
    "La aventura de hoy es la historia de terror del mañana",
    "La felicidad es como un rayo de sol, disfrútala antes de que el cambio climático la arruine",
    "Enfrenta tus miedos, o pídeles alquiler por vivir en tu cabeza",
    "Recuerda, cada pequeño cambio cuenta. Especialmente los errores en tu declaración de la renta",
    "Aprovecha las oportunidades, son como los autobuses, los que no llegan tarde simplemente no pasan",
    "Ser agradecido está bien, pero no paga las facturas",
    "La creatividad es como jugar a la ruleta rusa, nunca sabes cuándo te tocará una 'buena' idea",
    "Ríe y el mundo reirá contigo. Llora, y te darán una cuenta de Twitter",
    "Sigue tu corazón, pero recuerda llevar tu cerebro contigo"
  ]
}
```
Añadir frases a la base de datos: http://localhost:5000/add abrirá una web con un formulario que permite cargar archivos. Admitirá solo archivos .json en forma de listas o diccionarios. Se ha realizado una comprobación de errores que confirme que el archivo subido es correcto.


