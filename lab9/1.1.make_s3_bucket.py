#create a bucket and list buckets

import boto3
s3 = boto3.resource('s3')

#create bucket
s3.create_bucket(Bucket='transact-wdillingham')

#list buckets
for bucket in s3.buckets.all():
        print(bucket.name)
