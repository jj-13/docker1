pipeline {
  agent any
  stages {
    stage("build") {
      steps {
        sh """
          docker compose up -d
        """
      }
    }
    stage("run") {
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