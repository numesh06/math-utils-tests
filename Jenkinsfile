pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                bat '''
                    python --version
                    pip --version
                    pytest --version
                    pytest tests/ --junitxml=pytest_report.xml
                '''
            }
        }
    }
    post {
        always {
            junit 'pytest_report.xml'
        }
    }
}
