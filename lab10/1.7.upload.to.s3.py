import boto3

s3 = boto3.resource('s3')

data = open('foo.txt', 'rb')
s3.Bucket(acme-source-wdillingham).put_object(Key='foo.txt', Body=data)