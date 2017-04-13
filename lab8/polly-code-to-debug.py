from boto3 import client
import boto3
import StringIO   # something needs to be fixed here
from contextlib import closing

polly = client("polly", 'us-east-1' )
response = polly.synthesize_speech(
    Text="Hi from Diane",
    OutputFormat="mp3",
    VoiceId="Kendra")

print(response)

if "AudioStream" in response:
    with closing(response["AudioStream"]) as stream:
        data = stream.read()
        fo = open("output.mp3", "w+")  # something needs to be fixed here
        fo.write(data)
        fo.close()
