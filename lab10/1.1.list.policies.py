#list acme-source* buckets and list their policies
l
import json
import boto3
s3 = boto3.resource('s3')
client = boto3.client('s3')

for bucket in s3.buckets.all():
        print(bucket.name)
        
response = client.get_bucket_policy(
        Bucket='acme-logs-wdillingham'
)