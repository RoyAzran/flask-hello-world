pipeline {
    agent any {
        stage('Checkout') {
            steps {
                git 'https://github.com/RoyAzran/flask-hello-world.git' 
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t hello-world:latest ."
                }
            }
        }
    }
}
