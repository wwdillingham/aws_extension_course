import boto3

client = boto3.client('codestar')

response = client.list_projects()
print(response)
