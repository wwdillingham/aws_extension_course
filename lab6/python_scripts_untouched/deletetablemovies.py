from __future__ import print_function # Python 2/3 compatibility
# The following two lines are a fix for Windows boto3 issue
import os
os.environ["TZ"]="UTC"
import boto3
import sys

# Get the service resoure
# Next line needs to be changed to reach DynamoDB in Amazon's cloud!  
# Hint: http://boto3.readthedocs.io/en/latest/guide/dynamodb.html
# http://boto3.readthedocs.io/en/latest/reference/services/dynamodb.html#table
dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

try:
   table = dynamodb.Table('Movies')
   table.delete()
   print('Deleted table called: Movies')
   print("Another trivia is coming fine folks!")
   print("Who is the famous cartoon fella who tries to hunt down the Roadrunner using ACME bombs? You must have his full name. Jot it down after your output. +1 unless you already have 100")

except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise