pipeline { 

    environment { 

        registry = 'braunsteinshlomi/morse-service' 

        registryCredential = 'docker-hub-credentials' 

        dockerImage = '' 

    }

    agent any 

    stages { 

        stage('Cloning our Git') { 

            steps { 
                sh 'echo $GIT_BRANCH'
                git([url: 'https://github.com/shlomibra/morse_server.git', branch: 'main'])
            }

        } 

        stage('Building our image') { 

            steps { 

                script { 

                    dockerImage = docker.build(registry + ":$BUILD_NUMBER")

                }

            } 

        }

       stage('Push image') { 

            steps { 

                script { 

                    docker.withRegistry('https://registry.hub.docker.com', registryCredential) {
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
                
                    sh "docker run -d -p 11113:11113 $registry:$BUILD_NUMBER"
                    sh 'curl localhost:11113'
                    sh 'docker kill $(docker ps -q)'

            }

        } 

       stage('Remove Unused docker image') {
           
          steps{
                    sh "docker rmi $registry:$BUILD_NUMBER"
        }
           
       }

    }

}
