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

version: '3'
services:
  postgres:
    image: postgres:latest
    volumes:
      - django-postgres-data:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: my_database

  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      POSTGRES_HOST: postgres
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: my_database
      DJANGO_SUPERUSER_USERNAME: admin
      DJANGO_SUPERUSER_EMAIL: admin@gmail.com
      DJANGO_SUPERUSER_PASSWORD: admin369

    command: ["/bin/bash", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
    #command: ["python", "manage.py", "runserver", "0.0.0.0:8000"]
    depends_on:
      - postgres

volumes:
  django-postgres-data: {}
