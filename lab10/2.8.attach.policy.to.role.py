#2.8 Attach the policy: AWSLambdaExecute to the role you created in step 7:
# lambda-s3-execution-role
import boto3
client = boto3.client('iam')

response = client.attach_role_policy(
    RoleName='lambda-s3-execution-role',
    PolicyArn='arn:aws:iam::aws:policy/AWSLambdaExecute'
)
print(response)