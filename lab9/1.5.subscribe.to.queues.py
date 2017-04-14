import boto3
client = boto3.client('sns')

notification_subscription_response = client.subscribe(
    TopicArn='arn:aws:sqs:us-east-1:644009940612:UserNotificationQueue',
    Protocol='email',
    Endpoint='wes_dillingham@harvard.edu'
)
collection_subscription_response = client.subscribe(
    TopicArn='arn:aws:sqs:us-east-1:644009940612:CreditCollectionQueue',
    Protocol='email',
    Endpoint='wes_dillingham@harvard.edu'
)
print(subscription_response)
print(collection_subscription_response)