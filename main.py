import json
import boto3

def lambda_handler(event, context):
    rekognition = boto3.client("rekognition")
    s3 = boto3.client("s3")
    fileObj = s3.get_object(Bucket= "imgakashbucketrecognition", Key="horse.jpg" )
    file_content = fileObj["Body"].read()
    response = rekognition.detect_labels(Image= {"S3Object" : {"Bucket" : "imgakashbucketrecognition", "Name": "horse.jpg"}})
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
