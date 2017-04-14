#create a bucket and list buckets

import boto3
s3 = boto3.resource('s3')
client = boto3.client('s3')

client.list_buckets()

#s3.create_bucket(Bucket='transact-wdillingham')
