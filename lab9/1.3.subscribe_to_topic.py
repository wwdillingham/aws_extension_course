import boto3
client = boto3.client('sns')

subsribe_resoonse = client.subscribe(
    TopicArn='arn:aws:sns:us-east-1:644009940612:HighAccountBalanceAlertSNSTopic',
    Protocol='email',
    Endpoint='wes_dillingham@harvard.edu'
)