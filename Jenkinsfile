pipeline { 

    environment { 

        registry = 'braunsteinshlomi/morse-service' 

        registryCredential = 'docker-hub-credentials' 

        dockerImage = ''
        hostPort=''

    }

    agent any 

    stages { 

        stage('Cloning our Git') { 

            steps { 
                sh 'echo $BRANCH_NAME'
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
                 script { 
                     if (env.BRANCH_NAME == 'main') {
                         hostPort ='4000'
                        sh "docker run -d -p 11113:4000 $registry:$BUILD_NUMBER"
                    }
                     if (env.BRANCH_NAME == 'develop') {
                         hostPort ='5000'
                        sh "docker run -d -p 11113:5000 $registry:$BUILD_NUMBER"
                    }
                        sh 'curl localhost:$hostPort'
                        sh 'curl localhost:$hostPort'
                        sh 'docker kill $(docker ps -q)'
                    }
            }

        } 

       stage('Remove Unused docker image') {
           
          steps{
                    sh "docker rmi $registry:$BUILD_NUMBER"
        }
           
       }

    }

}
