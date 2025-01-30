pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/numesh06/math-utils-tests.git'
      }
    }
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
