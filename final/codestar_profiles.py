import boto3

client = boto3.client('codestar')
iam_client = boto3.client('iam')

me = iam_client.get_user(
    UserName='wdillingham'
)
diane = iam_client.get_user(
    UserName='diane-codestar'
)
zhen = iam_client.get_user(
    UserName='zhen-codestar'
)
arn_diane = diane['User']['Arn']
arn_zhen = zhen['User']['Arn']
arn_me = me['User']['Arn']

me_response = client.create_user_profile(
    userArn=arn_me,
    displayName='Wes Dillingham',
    emailAddress='wes_dillingham@harvard.edu'
)
zhen_response = client.create_user_profile(
    userArn=arn_zhen,
    displayName='Zhenyu Zhao',
    emailAddress='fake_1@harvard.edu'
)
diane_response = client.create_user_profile(
    userArn=arn_diane,
    displayName='Diane Howard',
    emailAddress='fake_2@harvard.edu'
)

describe_me = client.describe_user_profile(
    userArn=arn_me
)
describe_zhen = client.describe_user_profile(
    userArn=arn_zhen
)
describe_diane = client.describe_user_profile(
    userArn=arn_diane
)
print(describe_me)
print(describe_zhen)
print(describe_diane)