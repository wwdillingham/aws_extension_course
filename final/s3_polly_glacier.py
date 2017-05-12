import sys, boto3, StringIO, contextlib
from boto3 import client
from contextlib import closing
import time
polly = client("polly", 'us-east-1' )
s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')
cf_client = boto3.client('cloudformation')
glacier_client = boto3.client('glacier')
cf_bucket = 'cloudformation-input-bucket'
target_bucket = 'neighborhood-development-translation-bucket11'

s3_resource.create_bucket(Bucket=cf_bucket) #this is the bucket where cloudformation JSON objects live
data = open('s3_cf.json', 'rb')
s3_resource.Bucket(cf_bucket).put_object(Key='s3_cf.json', Body=data)


# create the stack (which in turn creates an s3 bucket for future polly files)
cf_response = cf_client.create_stack(
    StackName='neighborhood-development-stack11',
    TemplateURL='https://s3.amazonaws.com/cloudformation-input-bucket/s3_cf.json'
    )
time.sleep(60)
#do the polly translation
portugese_response = polly.synthesize_speech(
    Text="Welcome to the City of Boston \
          Office of Neighborhood Development \
          your neighborhood liason is \
          Bob Smith You can contact him at 617 555 2356",
    OutputFormat="mp3",
    VoiceId="Cristiano")

if "AudioStream" in portugese_response:
    with closing(portugese_response["AudioStream"]) as stream:
        data = stream.read()
        fo = open("portugese.mp3", "w+")
        fo.write(data)
        fo.close()

spanish_response = polly.synthesize_speech(
    Text="Welcome to the City of Boston \
          Office of Neighborhood Development \
          your neighborhood liason is \
          Bob Smith You can contact him at 617 555 2356",
    OutputFormat="mp3",
    VoiceId="Miguel")

if "AudioStream" in spanish_response:
    with closing(spanish_response["AudioStream"]) as stream:
        data = stream.read()
        fo = open("spanish.mp3", "w+")
        fo.write(data)
        fo.close()
        
data = open('portugese.mp3', 'rb')
s3_resource.Bucket(target_bucket).put_object(Key='portugese.mp3', Body=data)
data = open('spanish.mp3', 'rb')
s3_resource.Bucket(target_bucket).put_object(Key='spanish.mp3', Body=data)

#create the glacier vault of the same name
vault_creation_response = glacier_client.create_vault(
    vaultName=target_bucket
)

#upload to glacier vault
vault_bucket = s3_resource.Bucket(target_bucket) 
for object in vault_bucket.objects.all():
    print(object.key)
    with open(object.key, 'rb') as archive:
        glacier_response = glacier_client.upload_archive(
            vaultName=target_bucket,
            archiveDescription='neighborhood services translation',
            body=archive
            )
print(glacier_response)