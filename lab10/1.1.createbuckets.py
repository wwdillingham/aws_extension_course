#create a bucket and list buckets

import boto3
s3 = boto3.resource('s3')

#create bucket
s3.create_bucket(Bucket='acme-source-wdillingham')
s3.create_bucket(Bucket='acme-logs-wdillingham')

provided_policy = './policy.json'
with open(provided_policy, 'r') as policy:
        the_policy = json.load(policy)

policy_response = client.put_bucket_policy(
    Bucket='acme-logs-wdillingham',
    Policy=json.dumps(the_policy)
)
print(policy_response)
#list buckets
for bucket in s3.buckets.all():
        print(bucket.name)
