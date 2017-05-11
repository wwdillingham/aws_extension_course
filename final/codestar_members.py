#arn:aws:codestar:us-east-1:644009940612:project/wdillingham-fin

import boto3

client = boto3.client('codestar')

response = client.list_team_members(
    projectId='string',
    )
print(response)