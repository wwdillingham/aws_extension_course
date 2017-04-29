#create a bucket and list buckets

import boto3
s3 = boto3.resource('s3')

#create bucket
s3.create_bucket(Bucket='acme-source-wdillingham')
s3.create_bucket(Bucket='acme-logs-wdillingham')

provided_policy = './policy.json'
with open(provided_policy, 'r') as policy:
        the_policy = json.load(policy)

response1 = client.put_bucket_policy(
    Bucket='acme-source-wdillingham',
    Policy='string'
)
response2 = client.put_bucket_policy(
    Bucket='acme-logs-wdillingham',
    Policy=json.dumps(the_policy)
)
print(response1)
print(response2)
#list buckets
for bucket in s3.buckets.all():
        print(bucket.name)
