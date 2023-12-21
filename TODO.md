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

cambia en el siguiente compose mysql por un contenedor postgresql

version: '3'
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      MYSQL_HOST: mysql
      MYSQL_USER: root
      MYSQL_PASSWORD: secret
      MYSQL_DB: my_database
    command: ["python", "manage.py", "runserver", "0.0.0.0:8000"]

  mysql:
    image: mysql:8.0
    volumes:
      - django-mysql-data:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: secret
      MYSQL_DATABASE: my_database

volumes:
  django-mysql-data: {}