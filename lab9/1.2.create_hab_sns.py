import boto3
client = boto3.client('sns')

response = client.create_topic(
    Name='HighAccountBalanceAlertSNSTopic',
    DisplayName='HABTopic'
)