# Pasos para la instación del server y la base de datos

**Instala Python**: Asegúrate de tener Python 3.7 o superior instalado. Puedes descargarlo desde [python.org](https://www.python.org/downloads/), también lo puedes hacer desde la tienda de microsoft.

# Configura un Entorno Virtual:

Abre la terminal (o línea de comandos en Windows) y navega a la carpeta donde se encuentra tu proyecto. Por ejemplo:

    cd C:\Users\Ricardo\Desktop\prueba tecnica\SkycomBack

Crea un entorno virtual con:

    python -m venv env

**Activa el entorno virtual**
Es mas comodo hacerlo con las extensiones de visual studio llamada python, dando windows + g eliminando lo que nos salga y colocando ">" para bucar python seleccionar interprete, escogemos la opcion que contenga env

# Instala dependencias

    pip install django djangorestframework django-cors-headers

# Realiza migraciones

    python manage.py makemigrations
    python manage.py migrate

# Opcional crear un superusuario

    python manage.py createsuperuser

# Correr el servidor

    python manage.py runserver

La dirección del servidor sera nuestra variable de entorno en nuestro front-end
Ejemplo http://127.0.0.1:8000/api/
