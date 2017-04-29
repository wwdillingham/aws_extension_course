import boto3
client = boto3.client('cloudtrail')

response = client.create_trail(
    Name='acme-log-trail',
    S3BucketName='acme-logs-wdillingham',
    SnsTopicName='LogsforBucketTopic',
    IsMultiRegionTrail=False,
    IncludeGlobalServiceEvents=False,
)

print(response)