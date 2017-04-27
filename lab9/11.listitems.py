import boto3
dyn = boto3.resource('dynamodb')

table = dyn.Table('Customer')
data = table.scan()

