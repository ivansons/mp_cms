pipeline {
    agent {
        docker {
            image 'redis:latest'
            args '-u root'
        }
    }
    stages {
        stage('Build Environment') {
            steps {
                script {
                    sh """apt-get update && \
                        apt-get install -y python-dev python-pip sudo lsb-core git virtualenv awscli && \
                        sudo pip install --upgrade pip
                        """
                    sh 'redis-server --daemonize yes'
                }
            }
        }
        stage ('Test') {
            steps {
                script {
                    sh 'make test'

                }
            }
        }
        stage('Deploy'){
            steps{
                script {
                    sh 'make build'
                    def VERSION = sh(script: "git describe --tags --long | tr -d '\n'", returnStdout: true)
                    s3Upload(
                        bucket:"matterport-software",
                        path:'mp_cms/',
                        includePathPattern:'mp_cms-*.tar.gz',
                        workingDir:'builds/',
                        acl:'BucketOwnerFullControl')
                    sh "echo ${VERSION}"
                    sh "aws s3 cp public_html/static/ s3://static.matterport.com/mp_cms/${VERSION}/ \
                        --recursive \
                        --grants \
                            full=id=c5658c1957d8ed52b846446fd67e0fdd86a43c543926cdd61b7d39600a677913 \
                            read=uri=http://acs.amazonaws.com/groups/global/AllUsers"
                }
            }
        }
    }
    post {
        failure {
            emailext(
                subject: "Build ${env.JOB_NAME} - ${currentBuild.displayName} ${currentBuild.result}",
                body: """Build ${currentBuild.result}
                    ${env.RUN_DISPLAY_URL}
                    """,
                recipientProviders: [[$class: 'CulpritsRecipientProvider']]
            )
        }
        always {
                echo 'Cleaning artifacts, and leftover from previous build.'
                sh 'useradd -ms /bin/bash ubuntu'
                sh 'chown -R ubuntu:ubuntu `pwd`'
        }
    }
}
