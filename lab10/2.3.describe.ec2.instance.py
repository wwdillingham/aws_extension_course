#describe instance

import boto3

client = boto3.client('ec2')

response = client.describe_instances(
    InstanceIds=[
        'i-069637b51da1ea574',
    ],
)