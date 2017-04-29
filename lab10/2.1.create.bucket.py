#create a bucket and list buckets
import json
import boto3
s3 = boto3.resource('s3')
client = boto3.client('s3')

#create bucket
s3.create_bucket(Bucket='acme-source-wdillingham-resized')

#upload to lab 1 bucket
lab1bucket = 'acme-source-wdillingham'
data = open('HappyFace.jpg', 'rb')
s3.Bucket(lab1bucket).put_object(Key='HappyFace.jpg', Body=data)

#List all buckets
for bucket in s3.buckets.all():
        print(bucket.name)

#list objects in that bucket
for object in lab1bucket.objects.all():
    print(object)

