import boto3
dyn = boto3.resource('dynamodb')

table = dyn.Table('TransactionTotal')
data = table.scan()

for i in data['Items']:
        print(i['CustomerId'], i['accountBalance'])
