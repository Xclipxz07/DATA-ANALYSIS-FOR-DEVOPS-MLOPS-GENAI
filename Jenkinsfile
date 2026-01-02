pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/your-username/sales-dashboard.git'
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker build -t sales-dashboard .'
            }
        }

        stage('Run Docker') {
            steps {
                sh 'docker run -d -p 5000:5000 sales-dashboard'
            }
        }
    }
}
