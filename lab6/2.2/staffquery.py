from __future__ import print_function # Python 2/3 compatibility
# The following two lines are a fix for Windows boto3 issue
import os
os.environ["TZ"]="UTC"
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

try:
# Helper class to convert a DynamoDB item to JSON.
   class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

   dynamodb = boto3.resource('dynamodb',endpoint_url='https://dynamodb.us-east-1.amazonaws.com')
   table = dynamodb.Table('ACMESTAFF')

   print("ITEMS in ACMESTAFF:")

   response = table.query(
      KeyConditionExpression=Key('first_name').exists()
)

   for i in response['Items']:
       print(i['first_name'], ":", i['last_name'])

except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
