pipeline { 

    environment { 

        registry = 'braunsteinshlomi/morse-service' 

        registryCredential = 'docker-hub-credentials' 

        dockerImage = ''
        hostPort=''

    }

    agent any 

    stage('Test') {
        steps {
            script {
                branchName = sh(label: 'getBranchName', returnStdout: true, script: 'git rev-parse --abbrev-ref HEAD').trim()
                println branchName
            }   
        }
      } 

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
                 script { 
                     if (env.GIT_BRANCH == 'main') {
                         hostPort ='4000'
                        sh "docker run -d -p 11113:4000 $registry:$BUILD_NUMBER"
                    }
                     if (env.GIT_BRANCH == 'develop') {
                         hostPort ='5000'
                        sh "docker run -d -p 11113:5000 $registry:$BUILD_NUMBER"
                    }
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
