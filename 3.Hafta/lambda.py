import json

import boto3
from botocore.exceptions import NoCredentialsError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('user')

def lambda_handler(event, context):
    # Kullanıcıdan gelen bilgiler
    name = event['queryStringParameters']['name']
    email = event['queryStringParameters']['email']
    print("name",name)
    

    try:
        # DynamoDB'ye kullanıcı kaydı ekleme
        table.put_item(Item={
            'email': str(email),
            'name': str(name)
        })
        
        return {
            'statusCode': 200,
            'body': json.dumps(event)
        }
    except NoCredentialsError:
        return {
            'statusCode': 403,
            'body': json.dumps('Credentials not available')
        }
