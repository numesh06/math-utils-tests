pipeline {
  agent any
  
  stages {
    stage('Test') {
      steps {
        bat 'pytest test/ --junitxml=pytest_report.xml'
      }
    }
  }
  post {
    always {
      junit 'pytest_report.xml'
    }
  }
}
