
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
        timestamps()
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Fetching latest code from GitHub'
                deleteDir()
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                echo 'Creating Python environment'
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --no-cache-dir -r requirements.txt
                '''
            }
        }

        stage('Syntax Validation') {
            steps {
                echo 'Checking Python syntax'
                sh '''
                    .venv/bin/python -m compileall -q app.py tests
                '''
            }
        }

        stage('Unit Testing') {
            steps {
                echo 'Executing Pytest test cases'
                sh '''
                    .venv/bin/python -m pytest -v -p no:cacheprovider
                '''
            }
        }
    }

    post {
        success {
            echo 'ACEest Fitness BUILD SUCCESSFUL!'
        }

        failure {
            echo 'BUILD FAILED! Check console logs.'
        }
    }
}
