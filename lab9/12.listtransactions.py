import boto3
dyn = boto3.resource('dynamodb')

table = dyn.Table('Transactions')
pe = "TransactionId"
data = table.scan(
    ProjectionExpression=pe
)
print(data)
