import json
import boto3
s3 = boto3.resource('s3')
client = boto3.client('s3')


lab1bucket = 'acme-source-wdillingham'
newbucket = s3.Bucket(lab1bucket)

#List all buckets
for bucket in s3.buckets.all():
        print(bucket.name)

#list objects in that bucket
for object in newbucket.objects.all():
    print(object)