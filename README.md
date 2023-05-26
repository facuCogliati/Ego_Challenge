# Ego Challenge

## Requisitos previos

Asegúrate de tener los siguientes requisitos previos instalados en tu sistema:

- Python (versión 3.10.8)
- Django (versión 4.2.1)

## Configuración del entorno

Sigue los siguientes pasos para configurar el entorno de desarrollo local:

1. Clona este repositorio en tu máquina local:
git clone https://github.com/facuCogliati/Ego_Challenge

2. Ve al directorio del proyecto:
cd Ego

3. Crea un entorno virtual e actívalo:
python -m venv venv
source venv/bin/activate

4. Instala las dependencias del proyecto:
pip install -r requirements.txt

5. Configura la base de datos:
python manage.py migrate

6. Ejecuta el servidor de desarrollo:
python manage.py runserver

7. Accede a la aplicación en tu navegador web en la siguiente URL: [http://localhost:8000/vehicules]
