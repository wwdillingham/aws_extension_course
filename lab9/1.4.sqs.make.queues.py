#Create 2 queues called: UserNotificationQueue and 
#CreditCollectionQueue and list your new queues.  CCA Lab 12, Steps 23 – 27.  
#Do this in Python.


import boto3
client = boto3.client('sqs')

#create the queues
create_collection_queue_response = client.create_queue(
    QueueName='CreditCollectionQueue',
)
create_notification_queue_response = client.create_queue(
    QueueName='UserNotificationQueue',
)

queues = client.list_queues()
print(queues)




