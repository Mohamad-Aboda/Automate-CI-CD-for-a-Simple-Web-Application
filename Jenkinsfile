pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Create a virtual environment and install requirements
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Activate virtual environment and run tests
                    sh '. venv/bin/activate && pytest -v'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Activate virtual environment and start Flask application
                    sh '. venv/bin/activate && python3 app.py'
                }
            }
        }
    }
}
