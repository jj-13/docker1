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

mysql -ppass -uroot
docker exec -it nombre_del_contenedor mysql -u root -p
docker exec -it <id_contenedor> psql -U postgres

https://copyprogramming.com/howto/how-to-to-use-django-createsuperuser-noinput-command

agregar python manage.py createsuperuser --no-input con las variables de entorno correspondientes
DJANGO_SUPERUSER_USERNAME=admin DJANGO_SUPERUSER_EMAIL=admin@example.com DJANGO_SUPERUSER_PASSWORD=xxxxx
python manage.py createsuperuser --no-input --username DJANGO_SUPERUSER_USERNAME=admin --email DJANGO_SUPERUSER_EMAIL=admin@example.com --password DJANGO_SUPERUSER_PASSWORD=xxxxx

en el contenedor de jenkins toca agregar los siguientes comandos para que se pueda ejecutar los comandos docker
  groupadd docker
  usermod -aG docker root
  chmod 666 /var/run/docker.sock

y los siguiente comandos si los reconoce dentro del contenedor de jenkins:
docker build -t app_django .
docker run -dp 0.0.0.0:8000:8000 app_django

pero al usar dentro del contenedor de jenkins el comando docker-compose up -d sale el siguiente error:
bash: docker-compose: command not found, para que funcione el comando docker-compose se tendra que agregar otros permisos o que hago para que funcione el comando
docker-compose?
