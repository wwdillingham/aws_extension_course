import boto3

s3 = boto3.resource('s3')

data = open('foo.txt', 'rb')
bucket='acme-source-wdillingham'
s3.Bucket(bucket).put_object(Key='foo.txt', Body=data)