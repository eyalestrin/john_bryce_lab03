pipeline {
    agent any
    parameters {
        string defaultValue: '300', name: 'INTERVAL'
    }

    stages {
        stage('Init Cleanup') {
            steps {
                echo "Cleaning old deployments of the application"
                cleanWs()
                sh "docker kill myapp || true"
                sh "docker rm myapp || true"
            }
        }
        stage('SCM Step') {
            steps {
                echo "Pulling code from GitHub"
                git url: 'https://github.com/eyalestrin/john_bryce_lab03.git', branch: 'main'
            }
        }
        stage('Build Step') {
            steps {
                echo "Creating an application from Dockerfile, with version that match the current build running number"
                sh "docker build -t myapp:${currentBuild.number} -f Dockerfile ."
            }
        }
        stage('Deploy Step') {
            steps {
                echo "Running the docker container, with version that match the current build running number"
                sh "docker run -v ${HOME}/.aws/credentials:/root/.aws/credentials:ro -itd --name myapp --env INTERVAL=${params.INTERVAL} myapp:${currentBuild.number}"
            }
        }
    }
}
