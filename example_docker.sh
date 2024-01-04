#!/bin/sh

docker compose up
#docker compose up -d
#mkdir tempdir
#echo "FROM python:3.11-slim-buster" >> tempdir/Dockerfile
#echo "WORKDIR /app" >> tempdir/Dockerfile
#echo "COPY . ." >> tempdir/Dockerfile
#echo "RUN apt-get update && apt-get install -y default-libmysqlclient-dev pkg-config gcc vim && rm -rf /var/lib/apt/lists/*" >> tempdir/Dockerfile
#echo "RUN pip install --upgrade pip" >> tempdir/Dockerfile
#echo "RUN pip install -r requirements.txt" >> tempdir/Dockerfile
#echo "EXPOSE 8000" >> tempdir/Dockerfile
#echo "CMD python manage.py runserver 0.0.0.0:8000" >> tempdir/Dockerfile
#
#cd tempdir
#docker build -t django_app .
#docker run -dp 0.0.0.0:8000:8000 django_app
docker ps