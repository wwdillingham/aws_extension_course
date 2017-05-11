#arn:aws:codestar:us-east-1:644009940612:project/wdillingham-fin
import boto3

client = boto3.client('codestar')
iam_client = boto3.client('iam')

me = iam_client.get_user(
    UserName='wdillingham'
)

create1response = iam_client.create_user(
    UserName='diane-codestar'
)
create2response = iam_client.create_user(
    UserName='zhen-codestar'
)
arn_diane = create1response['User']['Arn']
arn_zhen = create2response['User']['Arn']
arn_me = me['User']['Arn']
print(arn_me)

associate_me = associate_team_member(
    projectId = 'wdillingham-fin',
    userArn = arn_me,
    projectRole = 'Owner'
)
associate_diane = associate_team_member(
    projectId = 'wdillingham-fin',
    userArn = arn_diane,
    projectRole = 'Contributor'
)
associate_zhen = associate_team_member(
    projectId = 'wdillingham-fin',
    userArn = arn_zhen,
    projectRole = 'Contributor'
)
list_response = client.list_team_members(
    projectId='wdillingham-fin',
    )

print(list_response)