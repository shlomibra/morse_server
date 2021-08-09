pipeline { 

    environment { 

        registry = 'https://registry.hub.docker.com' 

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

                    docker.withRegistry(registry, registryCredential) {
                    dockerImage.push("${env.BUILD_NUMBER}")
                    dockerImage.push("latest")

                    }

                } 

            }

        } 

        stage('Pull image') { 

            steps { 
                
              script {
                
                    dockerImage.pull() 
                    
                    }

            }

        } 

    }

}
