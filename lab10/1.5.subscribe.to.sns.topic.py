import boto3
client = boto3.client('sns')

response = client.subscribe(
    TopicArn='arn:aws:sns:us-east-1:644009940612:LogsforBucketTopic',
    Protocol='email',
    Endpoint='wes_dillingham@harvard.edu'
)
print(response)