pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/RoyAzran/flask-hello-world.git'
            }
        }
        
        stage('connect to ECR and push image to ecr ') {
            steps {
                script {
                     sh """aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 992382545251.dkr.ecr.us-east-1.amazonaws.com 
                         docker build -t roy-repo . 
                         docker tag roy-repo:latest 992382545251.dkr.ecr.us-east-1.amazonaws.com/roy-repo:latest
                         docker push 992382545251.dkr.ecr.us-east-1.amazonaws.com/roy-repo:latest  """
                }
            }
        }
        
        stage('deploy application to container') {
            steps {
                script {
                    sh """
                      
                        docker run --rm -d -p 5000:5000 roy-repo 
                    """
                }
            }
        }
    }
}
