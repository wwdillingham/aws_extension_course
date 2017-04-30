import boto3
client = boto3.client('iam')
rolepolicy='''{
	"Version": "2012-10-17",
	"Statement": [{
		"Sid": "",
		"Effect": "Allow",
		"Principal": {
			"Service": "lambda.amazonaws.com"
		},
		"Action": "sts:AssumeRole"
	}]
}'''
response = client.create_role(
    RoleName='lambda-s3-execution-role',
    AssumeRolePolicyDocument=rolepolicy
)
print(response)