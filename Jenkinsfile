pipeline {
    agent any

    stages {
        /*stage('Checkout') {
            steps {
                checkout scm

                sh 'git log HEAD^..HEAD --pretty="%h %an - %s" > GIT_CHANGES'
                def lastChanges = readFile('GIT_CHANGES')
            }
        }*/

        stage('Deploy') {
            steps {
                sh 'pwd'
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

/*
pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                // Este paso instala las dependencias
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
               // Este paso ejecuta las pruebas
                sh 'python manage.py test'
            }
        }

        stage('Build') {
            steps {
                // Este paso construye el proyecto
                sh 'python setup.py build'
            }
        }
    }
}
*/