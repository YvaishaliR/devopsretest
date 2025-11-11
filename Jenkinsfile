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
            
		sh '''
                aws lambda update-function-code \
                    --function-name devopsretest \
                    --s3-bucket devopsretest11112025 \
                    --s3-key lambda_function.zip
           	 '''

        	}
	}
    }
    }
}
