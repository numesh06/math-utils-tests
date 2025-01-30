pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        sh 'pytest test/ --junitxml=pytest_report.xml'
      }
    }
  }
  post {
    always {
      junit 'pytest_report.xml'
    }
  }
}
