#wes dillingham
#list all remote buckets

import boto
import boto3
import boto.s3.connection
s3 = boto3.resource('s3')
client=boto3.client('s3')
conn = boto.connect_s3(
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )

bucketname = 'acme-wdillingham'
#create a bucket
bucket = conn.create_bucket(bucketname)


#list all buckets
for bucket in conn.get_all_buckets():
        print "{name}\t{created}".format(
                name = bucket.name,
                created = bucket.creation_date,
        )

#upload wanted files into the bucket

data = open('index.html', 'rb')
s3.Bucket(bucketname).put_object(Key='index.html', Body=data)
data = open('848px-Tux_Mono.svg.png', 'rb')
s3.Bucket(bucketname).put_object(Key='848px-Tux_Mono.svg.png', Body=data)
