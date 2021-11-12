pipeline {
    agent any

    triggers{
        githubPush()
    }

    stages{
        
        stage('Preparation') {       
            
            steps{
            catchError(buildResult: 'SUCCESS') {          
                sh 'docker stop samplerunning'          
                sh 'docker rm samplerunning'       
            }   
            }
        }   
        
        stage('Build') {       
            steps{
            build 'BuildAppJob'   
            }
        }   
        
        stage('Results') {   
            steps{    
            build 'TestAppJob'   
            }
        }
    }
}