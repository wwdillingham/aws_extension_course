dyn = boto3.resource('dynamodb')

table = dyn.Table('Customer')
data = table.scan()

