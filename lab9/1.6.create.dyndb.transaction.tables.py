import boto3

dynamodb = boto3.resource('dynamodb',endpoint_url='https://dynamodb.us-east-1.amazonaws.com')

table2 = dynamodb.create_table(
TableName='Transactions',
KeySchema=[
    {
        'AttributeName': 'CustomerId',
        'KeyType': 'HASH'
    },
    {
        'AttributeName': 'TransactionId',
        'KeyType': 'RANGE'
    }
],
AttributeDefinitions=[
    {
        'AttributeName': 'TransactionId',
        'AttributeType': 'S'
    },
    {
        'AttributeName': 'CustomerId',
        'AttributeType': 'S'
    }
],
ProvisionedThroughput={
    'ReadCapacityUnits': 5,
    'WriteCapacityUnits': 5
},
StreamSpecification={
    'StreamEnabled': True,
    'StreamViewType': 'NEW_IMAGE'
    }
)