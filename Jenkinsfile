pipeline { 

    environment { 

        registry = "https://hub.docker.com/repository/docker/braunsteinshlomi/morse-service" 

        registryCredential = 'docker-hub-credentials' 

        dockerImage = '' 

    }

    agent any 

    stages { 

        stage('Cloning our Git') { 

            steps { 

                git([url: 'https://github.com/shlomibra/morse_server.git', branch: 'main'])
            }

        } 

        stage('Building our image') { 

            steps { 

                script { 

                    dockerImage = docker.build("braunsteinshlomi/morse-service")

                }

            } 

        }

       stage('Push image') { 

            steps { 

                script { 

                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                    dockerImage.push("${env.BUILD_NUMBER}")
                    dockerImage.push("latest")

                    }

                } 

            }

        } 

        stage('Cleaning up') { 

            steps { 

//                sh "docker rmi $registry:$BUILD_NUMBER" 

            }

        } 

    }

}
