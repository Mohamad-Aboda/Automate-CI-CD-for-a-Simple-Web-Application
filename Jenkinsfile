pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'pytest'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sh 'python app.py'
                }
            }
        }
    }
}
