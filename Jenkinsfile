pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/RoyAzran/flask-hello-world.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t roy-repo:latest ."
                }
            }
        }
        
        stage('Push Image to ECR') {
            steps {
                script {
                    // Authenticate to ECR
                    sh """
                        aws ecr get-login-password --region us-east-1 \
                        | docker login --username AWS --password-stdin 992382545251.dkr.ecr.us-east-1.amazonaws.com
                        
                        docker tag roy-repo:latest 992382545251.dkr.ecr.us-east-1.amazonaws.com/roy-repo:latest
                        docker push 992382545251.dkr.ecr.us-east-1.amazonaws.com/roy-repo:latest
                    """
                }
            }
        }
    }
}
