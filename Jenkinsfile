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
        
        stage('Run and test server') { 

            steps { 
                
                    sh 'docker run -d -p 11113:11113 braunsteinshlomi/morse-service'
                    sh 'telnet localhost 11113'
                    sh 'telnet localhost 11113'
            }

        } 
                     
    }

}
