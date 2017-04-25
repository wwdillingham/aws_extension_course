import boto3

dynamodb = boto3.resource('dynamodb',endpoint_url='https://dynamodb.us-east-1.amazonaws.com')

table2 = dynamodb.create_table(
TableName='Transactions',
KeySchema=[
    {
        'AttributeName': 'TransactionId',
        'KeyType': 'HASH'
    },
    {
        'AttributeName': 'TransactionId',
        'KeyType': 'RANGE'
    }
],
AttributeDefinitions=[
    {
        'AttributeName': 'CustomerId',
        'AttributeType': 'S'
    },
],
ProvisionedThroughput={
    'ReadCapacityUnits': 5,
    'WriteCapacityUnits': 5
},
StreamSpecification={
    'StreamEnabled': True|False,
    'StreamViewType': 'NEW_IMAGE'
    }
)