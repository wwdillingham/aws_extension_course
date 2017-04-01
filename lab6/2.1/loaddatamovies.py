from __future__ import print_function # Python 2/3 compatibility
# The following two lines are a fix for Windows boto3 issue
import os
os.environ["TZ"]="UTC"
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
try:
   table = dynamodb.Table('Movies')
   print("Instantiate a table: ",table.creation_date_time)
   print("Ready to load data\n")
   incr = 0
   with open("moviedata.json") as json_file:
    movies = json.load(json_file, parse_float = decimal.Decimal)
    for movie in movies:
        incr += 1
        year = int(movie['year'])
        title = movie['title']
        info = movie['info']
        print("Adding movie # ", incr," Year: ",year," Title of Movie: ",title,)

        table.put_item(
           Item={
               'year': year,
               'title': title,
               'info': info,
            }
        )
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise