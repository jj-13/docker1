pipeline {
  agent any
  stages {
    stage('Build and Deploy') {
      steps {
        sh 'docker compose up -d'
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