pipeline {
  agent any
  stages {
    stage('Build and Deploy') {
      steps {
        sh 'chmod +x example_docker.sh'
        sh './example_docker.sh'
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