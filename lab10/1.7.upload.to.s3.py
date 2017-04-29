import boto3

s3 = boto3.resource('s3')

data = open('foo2.txt', 'rb')
bucket='acme-source-wdillingham'
s3.Bucket(bucket).put_object(Key='foo2.txt', Body=data)