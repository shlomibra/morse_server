pipeline { 

    environment { 
        registry = 'braunsteinshlomi/morse-service' 
        registryCredential = 'docker-hub-credentials'         
        dockerImage = ''
        branch_Name = "${GIT_BRANCH.replaceFirst(/^.*\//, '')}"
    }

    agent any 

    stages { 
        
        stage('Cloning our Git') { 

            steps { 
                sh 'echo branch name is: $branch_Name'
                git([url: 'https://github.com/shlomibra/morse_server.git', branch: branch_Name])
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
                     if (branch_Name == 'main') {
                        sh "docker run -d -p 11113:4000 $registry:$BUILD_NUMBER"
                        sh 'curl localhost:4000'
                    }
                     if (branch_Name == 'develop') {
                        sh "docker run -d -p 11113:5000 $registry:$BUILD_NUMBER"
                        sh 'curl localhost:5000'
                    }
                        
                        sh 'docker kill $(docker ps -a -q  --filter ancestor=$registry:$BUILD_NUMBER)'
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
