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

sigue saliendo el error 
File "/usr/local/lib/python3.11/site-packages/django/db/backends/mysql/base.py", line 247, in get_new_connection connection = Database.connect(**conn_params)
django.db.utils.OperationalError: (2061, 'RSA Encryption not supported - caching_sha2_password plugin was built with GnuTLS support')

y el setting.py 
DATABASES = {    
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': getenv('MYSQL_DATABASE', 'my_database'),
        'USER': getenv('MYSQL_USER', 'root'),
        'PASSWORD': getenv('MYSQL_PASSWORD', 'secret'),
        'HOST': getenv('MYSQL_HOST', 'mysql'),# Use 'mysql' as you defined in your docker-compose.yml
        'PORT': getenv('MYSQL_PORT', '3306'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'auth_plugin': 'mysql_native_password'
        }
    }
}