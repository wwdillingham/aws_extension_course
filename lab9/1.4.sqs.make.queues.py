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




