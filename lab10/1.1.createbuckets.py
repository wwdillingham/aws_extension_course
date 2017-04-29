#create a bucket and list buckets
import json
import boto3
s3 = boto3.resource('s3')
client = boto3.client('s3')

#create bucket
s3.create_bucket(Bucket='acme-source-wdillingham')
s3.create_bucket(Bucket='acme-logs-wdillingham')

bucket_policy = '''{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AWSCloudTrailAclCheck20150319",
            "Effect": "Allow",
            "Principal": {"Service": "cloudtrail.amazonaws.com"},
            "Action": "s3:GetBucketAcl",
            "Resource": "arn:aws:s3:::acme-logs-wdillingham"
        },
        {
            "Sid": "AWSCloudTrailWrite20150319",
            "Effect": "Allow",
            "Principal": {"Service": "cloudtrail.amazonaws.com"},
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::acme-logs-wdillingham/AWSLogs/644009940612/*",
            "Condition": {"StringEquals": {"s3:x-amz-acl": "bucket-owner-full-control"}}
        }
    ]
}'''
#print(bucket_policy)
policy_response = client.put_bucket_policy(
    Bucket='acme-logs-wdillingham',
    Policy=bucket_policy
)

