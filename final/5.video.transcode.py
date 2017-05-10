#create a bucket and list buckets
import json
import boto3
s3 = boto3.resource('s3')
s3_client = boto3.client('s3')
sns_client = boto3.client('sns')
transcode_client = boto3.client('elastictranscoder')

#create buckets
s3.create_bucket(Bucket='in-code-wdillingham')
s3.create_bucket(Bucket='out-code-wdillingham')

#upload the video to the in bucket
inbucket = 'in-code-wdillingham'
data = open('/tmp/Wildlife.wmv', 'rb')
s3.Bucket(inbucket).put_object(Key='Wildlife.wmv', Body=data)

create_topic_response = sns_client.create_topic(
    Name='TranscodeComplete',
)
the_arn = create_topic_response['TopicArn']

subscribe_response = sns_client.subscribe(
    TopicArn=the_arn,
    Protocol='email',
    Endpoint='wes_dillingham@harvard.edu'
)

pipeline_response = transcode_client.create_pipeline(
    Name='prob5_transcode_pipeline',
    InputBucket='in-code-wdillingham',
    OutputBucket='out-code-wdillingham',
    Role='arn:aws:iam::644009940612:role/Elastic_Transcoder_Default_Role',
    Notifications={
        'Completed': the_arn,
        'Error': the_arn,
        'Progressing': the_arn,
        'Warning': the_arn
        
    },
)

job_response = transcode_client.create_job(
    PipelineId='prob5_transcode_pipeline',
    OutputKeyPrefix='output.mp4',
)
