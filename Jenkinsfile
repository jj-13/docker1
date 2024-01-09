pipeline {
  agent any
  stages {
    stage("build") {
      steps {
        sh """
          docker build -t django_app .
        """
      }
    }
    stage("run") {
      steps {
        sh """
          docker run -dp 0.0.0.0:8000:8000 django_app
        """
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