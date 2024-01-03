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

en labs.play-with-docker.com tengo desplegada una instancia con jenkins la cual tiene un job de tipo miltibranch pipeline que deberia desplegar en el mismo nodo 
un contenedor django el cual tiene los archivos: 

Jenkinsfile:

pipeline {
    agent any

    stages {
        
        stage('Deploy') {
            steps {
                sh 'chmod +x jenkins_deploy_prod_docker.sh'
                sh './jenkins_deploy_prod_docker.sh'
            }
        }

        stage('Publish results') {
            steps {
                echo "Deployment successful"
            }
        }
    }

    post {
        success {
            echo "Build successful"
            // You can add additional steps here, like running tests or notifications.
        }

        failure {
            echo "Build failed"
        }
    }
}

jenkins_deploy_prod_docker.sh:

ssh -T ip172-18-0-38-cmalihao7r5g00avnp5g@direct.labs.play-with-docker.com <<EOF
  git pull
  cd docker1/
  docker compose up -d
  exit
EOF

Dockerfile:

FROM python:3.11-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Set environment variables
#ENV MYSQLCLIENT_CFLAGS=<your-value-here>
#ENV MYSQLCLIENT_LDFLAGS=<your-value-here>

COPY . .

# Update the package list and install dependencies
RUN apt-get update && apt-get install -y default-libmysqlclient-dev pkg-config gcc vim && rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port server is running on
EXPOSE 8000

# Start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

compose.yaml:
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
    command: ["/bin/bash", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py createsuperuser --no-input && python manage.py runserver 0.0.0.0:8000"]
    #command: ["python", "manage.py", "runserver", "0.0.0.0:8000"]
    depends_on:
      - postgres

volumes:
  django-postgres-data: {}

pero da error al conectarse al ssh -T ip172-18-0-38-cmalihao7r5g00avnp5g@direct.labs.play-with-docker.com