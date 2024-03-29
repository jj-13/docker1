#FROM python:3.11-slim-buster
## Set the working directory in the container to /app
#WORKDIR /app
#COPY . .
## Install any needed packages specified in requirements.txt
#RUN pip install --upgrade pip
#RUN pip install -r requirements.txt
## Expose the port server is running on
#EXPOSE 8000
#
## Start the server
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM python:3.11-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Set environment variables
#ENV MYSQLCLIENT_CFLAGS=<your-value-here>
#ENV MYSQLCLIENT_LDFLAGS=<your-value-here>

COPY . .

# Update the package list and install dependencies
#RUN apt-get update && apt-get install -y default-libmysqlclient-dev pkg-config gcc vim && rm -rf /var/lib/apt/lists/*
RUN apt-get update
RUN apt-get install -y default-libmysqlclient-dev pkg-config gcc vim
RUN rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port server is running on
EXPOSE 8000

# Start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
