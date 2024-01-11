pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'chmod +x example_docker.sh'
        sh 'pwd'
        sh 'ls -l'
        //sh 'docker-compose up -d -f ./docker-compose.yml'
        sh './example_docker.sh'
      }
    }
    stage('Deploy') {
      steps {
        sh 'docker run -dp 0.0.0.0:8000:8000 --name django_app_c --network jenkins_default backend__app'
        sh 'docker exec -it django_app_c /bin/bash'
        sh 'ls'
        sh 'python manage.py makemigrations && python manage.py migrate && python manage.py createsuperuser --no-input'
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