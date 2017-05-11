#arn:aws:codestar:us-east-1:644009940612:project/wdillingham-fin

import boto3

client = boto3.client('codestar')
iam_client = boto3.client('iam')

create1response = iam_client.create_user(
    UserName='diane-codestar'
)
create2response = iam_client.create_user(
    UserName='zhen-codestar'
)

list_response = client.list_team_members(
    projectId='wdillingham-fin',
    )

arn_1 = create1response['User']['Arn']
print(arn_1)
