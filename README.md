# usuariosP
Desarrollo de algoritmos de ordenamiento
1.-Instale xampp y pycharm para ocupar mysql
2.-Instale la versión de python 3.11 y django 4 con las siguientes instrucciones:
3.-python -m pip install --upgrade pip actualice las librerias de python
4.-pip3 install virtualenvwrapper-win instale la instrucción para crear entornos virtuales
mkvirtualenv [nombre del entorno] cree un entorno virtual
5.-pip3 install django instalé django
mkdir usuarios Cree la carpeta y con cd me dirigí a donde se encontraba
6.- django-admin startproject [nombre del proyecto] cree la carpeta del proyecto
7.-y subí el servidor con la siguiente instrucción
python manage.py runserver
8.-Instale los paquetes cymysql y django-cymysql:
pip install cymysql
pip install django-cymysql
pip install openpyxl
9.-pip list con esta instrucción verifico los paquetes instalados
10.-Realice la configuración de la base de datos, la zona horaria y las url para css y javascript
DATABASES = {
     'default': {
        'ENGINE': 'mysql_cymysql',
        'NAME': 'crudusu',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'UTC'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

11.-python manage.py startapp myusuariosapp creo la aplicación en la carpeta del proyecto
y cambio con settings.py
INSTALLED_APPS = […
    'myusuariosapp.apps.MyusuariosappConfig',
]
12.-Con esta instrucción se crean los modelos después de agregar la base
python manage.py inspectdb





