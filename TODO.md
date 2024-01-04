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

#!/bin/sh

eval $(ssh-agent -s)
ssh-add /etc/ssh/ssh_host_ed25519_key

#ssh -T root@buildkitsandbox <<EOF
ssh -o StrictHostKeyChecking=no -T ip172-18-0-38-cmalihao7r5g00avnp5g@direct.labs.play-with-docker.com <<EOF
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

pero al conectarse al ssh -T ip172-18-0-38-cmalihao7r5g00avnp5g@direct.labs.play-with-docker.com da error:
+ ./jenkins_deploy_prod_docker.sh
Host key verification failed.


modifique el archivo jenkins_deploy_prod_docker.sh con:
ssh -o StrictHostKeyChecking=no -T ip172-18-0-38-cmalihao7r5g00avnp5g@direct.labs.play-with-docker.com <<EOF
  git pull
  cd docker1/
  docker compose up -d
  exit
EOF

y salio el siguiente error:
+ ./jenkins_deploy_prod_docker.sh
Warning: Permanently added 'direct.labs.play-with-docker.com' (RSA) to the list of known hosts.
ip172-18-0-38-cmalihao7r5g00avnp5g@direct.labs.play-with-docker.com: Permission denied (publickey).


-----BEGIN OPENSSH PRIVATE KEY-----
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
5wJzOpE437evSbAAAACnJvb3RAbm9kZTE=
-----END OPENSSH PRIVATE KEY-----



-----BEGIN OPENSSH PRIVATE KEY-----
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
Xt00lGhC03KRcAAAAKcm9vdEBub2RlMQE=
-----END OPENSSH PRIVATE KEY-----

docker run -d --rm --name=agent1 -p 22:22 \
-e "JENKINS_AGENT_SSH_PUBKEY=ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDXi2sSmGaJgF3RqY5FfpHFAAPqAb6pQLrlkuq57hA+pmiSOBMf24DlkMVZEBvzMQw2IwnMMRxJEVQRg7ynLaBkYKcVBqCFRoQAnOHUuJAaG1pU3a2K+xDo+5/kFj6Ggtvb1QVP/atJ1h7NGM6xQFdPpZ5vrX7UGDp9yEjCTPG2dogSY4YIkDtZku7jxBpDMHrdSj9wGp+4+GZu3xH7Bq/qdn4c4ihhh8bhwSkrsRvlzpfRQ3i8+iePl17cNau7USh4B1Pe3PgzF75pHrTPI121r+G6Z2Q+bLlod/F0P6gn1QSlwoF299JVUh1PqhhzD2Re2AygwttZvVnIRg7jmTUN2TFuDKxFAqCcKetN6IlJynWBWINZVgoqOYp6QImxWV/pEDU0xhyUyndS9QcPPdEMtVJfEwFdDVt85H8007VXwjmYym1ZUNY5WsFtJDkANrV8ZHyQcPUC2lLSZ5pszYTitaUAj2UPSZShe1qKLNZzyTdLxtgF0/O5d29hqHUAF50= root@node1" \
jenkins/ssh-agent:alpine-jdk17

ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDXi2sSmGaJgF3RqY5FfpHFAAPqAb6pQLrlkuq57hA+pmiSOBMf24DlkMVZEBvzMQw2IwnMMRxJEVQRg7ynLaBkYKcVBqCFRoQAnOHUuJAaG1pU3a2K+xDo+5/kFj6Ggtvb1QVP/atJ1h7NGM6xQFdPpZ5vrX7UGDp9yEjCTPG2dogSY4YIkDtZku7jxBpDMHrdSj9wGp+4+GZu3xH7Bq/qdn4c4ihhh8bhwSkrsRvlzpfRQ3i8+iePl17cNau7USh4B1Pe3PgzF75pHrTPI121r+G6Z2Q+bLlod/F0P6gn1QSlwoF299JVUh1PqhhzD2Re2AygwttZvVnIRg7jmTUN2TFuDKxFAqCcKetN6IlJynWBWINZVgoqOYp6QImxWV/pEDU0xhyUyndS9QcPPdEMtVJfEwFdDVt85H8007VXwjmYym1ZUNY5WsFtJDkANrV8ZHyQcPUC2lLSZ5pszYTitaUAj2UPSZShe1qKLNZzyTdLxtgF0/O5d29hqHUAF50= root@node1


ssh-add -l -E sha256

al ejecutar el archivo example_docker.sh desde un job en jenkins sale este error:
[build_app_job] $ /bin/sh -xe /tmp/jenkins8868534962604727975.sh
+ bash ./example_docker.sh
ERROR: permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/_ping": dial unix /var/run/docker.sock: connect: permission denied
docker: permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/create": dial unix /var/run/docker.sock: connect: permission denied.
See 'docker run --help'.
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/json": dial unix /var/run/docker.sock: connect: permission denied
Build step 'Execute shell' marked build as failure
Finished: FAILURE

contenido del archivo example_docker.sh:
#!/bin/sh

mkdir tempdir

echo "FROM python:3.11-slim-buster" >> tempdir/Dockerfile
echo "WORKDIR /app" >> tempdir/Dockerfile
echo "COPY . ." >> tempdir/Dockerfile
echo "RUN apt-get update && apt-get install -y default-libmysqlclient-dev pkg-config gcc vim && rm -rf /var/lib/apt/lists/*" >> tempdir/Dockerfile
echo "RUN pip install --upgrade pip" >> tempdir/Dockerfile
echo "RUN pip install -r requirements.txt" >> tempdir/Dockerfile
echo "EXPOSE 8000" >> tempdir/Dockerfile
echo "CMD python manage.py runserver 0.0.0.0:8000" >> tempdir/Dockerfile

cd tempdir
docker build -t django_app .
docker run -dp 0.0.0.0:8000:8000 django_app
docker ps

al siguiente compose.yaml agregale el networks 

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
