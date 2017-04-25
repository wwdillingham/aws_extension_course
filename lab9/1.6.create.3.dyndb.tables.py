import boto3


#Define a table called Customer with a Primary partition key called CustomerId  as a String.  Note: There is no Primary sort key.
#Define a table called Transactions with a Primary partition key called CustomerId  as a String and Primary sort key called TransactionId as a String.
#Define a table called TransactionTotal  with a Primary partition key called CustomerId  as a String
#Note: There is no Primary sort key.	
#Also for all 3 tables Set Provisioned read capacity units and Provisioned write capacity units =5.


dynamodb = boto3.resource('dynamodb',endpoint_url='https://dynamodb.us-east-1.amazonaws.com')


table = dynamodb.create_table(
TableName='Customer',
KeySchema=[
    {
        'AttributeName': 'CustomerId',
        'KeyType': 'HASH' 
    }
],
AttributeDefinitions=[
    {
        'AttributeName': 'string',
        'AttributeType': 'S'
    },
],
ProvisionedThroughput={
    'ReadCapacityUnits': 5,
    'WriteCapacityUnits': 5
}
)