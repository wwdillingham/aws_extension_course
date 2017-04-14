#Create 1 SNS topic in Python called: HighAccountBalanceAlertSNSTopic with attribute DisplayName=HABTopic.  CCA Lab 12, Steps 11 – 15.  Do this in Python.
#Show your code, your SNS Topic and your ARN from Console or from Python.

import boto3
client = boto3.client('sns')

response = client.create_topic(
    Name='HighAccountBalanceAlertSNSTopic',
    DisplayName='HABTopic'
)