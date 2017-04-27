import boto3
dyn = boto3.resource('dynamodb')

table = dyn.Table('Transactions')
data = table.scan()
print(data)
