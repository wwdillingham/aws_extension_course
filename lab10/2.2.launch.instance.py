import boto3

client = boto3.client('ec2')

response = client.run_instances(
  ImageId='ami-0b33d91d',
  InstanceType='t2.micro',
  SecurityGroups=[
          'ACME_LinuxWebSecurityGroup',
      ],
  KeyName='initial_key',
  MinCount=1,
  MaxCount=1
)
print(response)
