import boto3
s3 = boto3.resource('s3')
s3.meta.client.upload_file('/tmp/transactions.txt', 'transact-wdillingham', 'transact-object')