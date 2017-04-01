# The following two lines are a fix for Windows boto3 issue
import os
os.environ["TZ"]="UTC"
import boto3
import json
import sys

# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="apigateway.us-east-1.amazonaws.com")
table_var='acmestaff'
# Create the DynamoDB table.
try:
    table = dynamodb.create_table(
    TableName=table_var,
    KeySchema=[
        {
            'AttributeName': 'first_name',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'last_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'first_name',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists
    table.meta.client.get_waiter('table_exists').wait(TableName=table_var)

# Print out data about the table.
    print("Table:",table_var,"created on date:",table.creation_date_time)
    print("Total row count in table",table_var,":",table.item_count)


except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
