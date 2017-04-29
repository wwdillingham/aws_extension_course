#Create an IAM Group to allow users to have full access to CloudTrail with the Name= ACMECloudTrailGroup in Python.

import boto3
client = boto3.client('iam')

create_response = client.create_group(
    GroupName='ACMECloudTrailGroup'
)

print(create_response)

policy_response = client.attach_group_policy(
    GroupName='ACMECloudTrailGroup',
    PolicyArn='arn:aws:iam::aws:policy/AWSCloudTrailFullAccess',
)

print(policy_response)