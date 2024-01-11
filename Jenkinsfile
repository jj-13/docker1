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
        sh 'ls'
        sh 'docker exec -i django_app_c /bin/bash -c "python manage.py makemigrations && python manage.py migrate"'
        //sh 'docker cp create_superuser.py django_app_c:/create_superuser.py' //para cuando se agregan archivos al repo y ya esta creado el contenedor
        sh 'docker exec -i django_app_c python manage.py shell < create_superuser.py'
        sh 'docker exec -i django_app_c python manage.py test'
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