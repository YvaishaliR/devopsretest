pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'zip -r lambda_function.zip lambda_function.py'
            }
        }
        stage('Lambda - S3 Upload & Deploy') {
  
        steps {
            withAWS(credentials: 'awscreds', region: 'ap-south-1') {
                
                s3Upload(
                    file: "lambda_function.zip",
                    bucket: 'devopsretest11112025'
                )
            }

            sh '''
            aws lambda create-function \
            --function-name devopsretest \
            --runtime python3.13 \
            --role arn:aws:iam::439162045865:role/devopsretestrole \
            --handler lambda_function.lambda_handler \
            --code S3Bucket=devopsretest11112025,S3Key=lambda_function.zip '''
        }
    }
    }
}
