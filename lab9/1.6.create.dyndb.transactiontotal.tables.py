import boto3

dynamodb = boto3.resource('dynamodb',endpoint_url='https://dynamodb.us-east-1.amazonaws.com')


table = dynamodb.create_table(
TableName='TransactionTotal',
KeySchema=[
    {
        'AttributeName': 'CustomerId',
        'KeyType': 'HASH'
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
}
)

