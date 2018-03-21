pipeline {
  agent any
  stages {
    stage('checkout') {
      steps {
        git(url: 'https://github.com/i-maverick/AioApiServer', branch: 'master')
      }
    }
  }
}