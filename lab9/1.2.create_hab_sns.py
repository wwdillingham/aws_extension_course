import boto3
client = boto3.client('sns')

response = client.create_topic(
    Name='HighAccountBalanceAlertSNSTopic',
)

the_arn = response['TopicArn']

topic_response = client.set_topic_attributes(
    TopicArn=the_arn,
    AttributeName='DisplayName',
    AttributeValue='HABTopic'
)

print(topic_response)