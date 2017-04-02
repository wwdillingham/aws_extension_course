from __future__ import print_function # Python 2/3 compatibility
# The following two lines are a fix for Windows boto3 issue
import os
os.environ["TZ"]="UTC"
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb',endpoint_url='https://dynamodb.us-east-1.amazonaws.com')
try:
   table = dynamodb.Table('ACMESTAFF')
   print("Instantiate a table: ",table.creation_date_time)
   print("Ready to load data\n")
   incr = 0
   with open("staff.json") as json_file:
    staffs = json.load(json_file, parse_float = decimal.Decimal)
    for staff in staffs:
        incr += 1
        first_name = int(staff['first_name'])
        last_name = staff['last_name']
        print("Adding staff member ", incr," first name: ",first_name," last name ",last_name,)

        table.put_item(
           Item={
               'first_name': first_name,
               'last_name': last_name,
            }
        )
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
