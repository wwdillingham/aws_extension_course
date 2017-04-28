import boto3
dyn = boto3.resource('dynamodb')

table = dyn.Table('TransactionTotal')
pe = "CustomerId, accountBalance"
data = table.scan(
    ProjectionExpression=pe
)
print(data)
