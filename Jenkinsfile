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

                    dockerImage = docker.build("braunsteinshlomi/morse-service" + ":$BUILD_NUMBER")

                }

            } 

        }

       stage('Push image') { 

            steps { 

                script { 

                    docker.withRegistry(registry, registryCredential) {
                    dockerImage.push()

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
                
                    sh "docker run -d -p 11113:11113 braunsteinshlomi/morse-service:$BUILD_NUMBER"
                    sh 'curl localhost:11113'

            }

        } 

       stage('Remove Unused docker image') {
           
          steps{
                    sh "docker rmi $dockerImage"
        }
           
       }

    }

}
