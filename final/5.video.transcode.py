#create a bucket and list buckets
import json
import boto3
s3 = boto3.resource('s3')
client = boto3.client('s3')

#create buckets
s3.create_bucket(Bucket='in-code-wdillingham')
s3.create_bucket(Bucket='out-code-yourfirstinitialandlastname')


#upload the video to the in bucket
inbucket = 'in-code-wdillingham'
data = open('Wildlife.wmv', 'rb')
s3.Bucket(inbucket).put_object(Key='HappyFace.jpg', Body=data)




