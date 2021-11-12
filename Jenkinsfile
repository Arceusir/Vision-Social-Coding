pipeline {
    agent any

    triggers{
        githubPush()
    }

    stages{
        
        stage('Preparation') {       
            
            steps{
            catchError(buildResult: 'SUCCESS') {          
                sh 'docker stop apprunning'          
                sh 'docker rm apprunning'       
            }   
            }
        }   
        
        stage('Build') {       
            steps{
            build 'build'   
            }
        }   
        
        stage('Results') {   
            steps{    
            build 'test'   
            }
        }
    }
}