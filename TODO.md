con el projecto base django:
    dockerizar la aplicacion

al projecto django agregar:
   1) crear una nueva app
   2) crear los modelos 
   3) crear la api
   4) crear la ruta para swagger
   5) todo lo anterior desde el contenedor

crear una network mysql y conectar la aplicacion
crear una network postgresql y conectar la aplicacion

al dockerizar una aplicacion en los requiremets.txt:

Django==4.2.7
mysqlclient==2.2.1

sale este error:
error: subprocess-exited-with-error
Command 'pkg-config --exists mysqlclient' returned non-zero
File "/usr/local/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 335, in main json_out['return_val'] = hook(**hook_input['kwargs'])
Exception: Can not find valid pkg-config name.
Specify MYSQLCLIENT_CFLAGS and MYSQLCLIENT_LDFLAGS env vars manual

solucion:
sudo apt-get update
apt install pkg-config gcc
sudo apt install python3-dev default-libmysqlclient-dev

agrega las variables de entorno MYSQLCLIENT_CFLAGS y MYSQLCLIENT_LDFLAGS manualmente2 al siguiente dockerfile:

Dockerfile:

FROM python:3.11-slim-buster
# Set the working directory in the container to /app
WORKDIR /app
COPY . .
# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# Expose the port server is running on
EXPOSE 8000

# Start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testdb',
        'USER': 'root',
        'PASSWORD': 'test',
        'HOST': '172.17.0.3', # <---- mysql container IPv4Address
        'PORT': '3306',
        'OPTIONS': {'auth_plugin': 'mysql_native_password'},
        }
}

mysql -ppass -uroot

