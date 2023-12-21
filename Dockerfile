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

# Update the package list and install dependencies
RUN apt-get update && apt-get install -y vim pkg-config gcc

COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port server is running on
EXPOSE 8000

# Start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
