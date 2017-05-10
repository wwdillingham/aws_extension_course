import json
import boto3
s3 = boto3.resource('s3')
s3_client = boto3.client('s3')

target_bucket='out-code-wdillingham'
target_object='output.wmv'


put_bucket_acl_response = s3_client.put_bucket_acl(
    ACL='public-read'
    Bucket=target_bucket
)

print(put_bucket_acl_response)