import boto3
client = boto3.client('sns')

response = client.create_topic(
    Name='LogsforBucketTopic',
)

the_arn = response['TopicArn']
print(the_arn)

topic_response = client.set_topic_attributes(
    TopicArn=the_arn,
    AttributeName='DisplayName',
    AttributeValue='AcmeLogs'
)

print(topic_response)