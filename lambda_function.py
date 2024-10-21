# AWS SDK for Python (Boto3) - https://aws.amazon.com/sdk-for-python/
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key
import logging
import json

# AWS Lambda Function Logging in Python - https://docs.aws.amazon.com/lambda/latest/dg/python-logging.html
logger = logging.getLogger()
logger.setLevel(logging.INFO)

session = boto3.Session()
dynamodb = session.resource("dynamodb")

table_name = "locations"  # Change this to the actual table name in your environment
table = dynamodb.Table(table_name)

# DynamoDB create item in table logic
def create_item(item):
    try:
        ret = table.put_item(Item=item)
        logger.info({"operation": "create an item", "details": ret})
    except ClientError as err:
        print(err)
        logger.debug({"operation": "item creation", "details": err})

# DynamoDB update Item from table logic
def update_item(item, reserve):
    try:
        ret = table.update_item(
            Key={'id': item["id"]},
            UpdateExpression="set reserve = :ad",
            ExpressionAttributeValues={':ad': reserve},
            ReturnValues="UPDATED_NEW"
        )
        logger.info({"operation": "update an item", "details": ret})
    except ClientError as err:
        logger.debug({"operation": "item update", "details": err})

# DynamoDB get Item from table logic
def get_item(id):
    try:
        ret = table.get_item(Key={'id': id})
        logger.info({"operation": "query an item", "details": ret})
        return ret['Item']
    except ClientError as err:
        logger.debug({"operation": "item query", "details": err})

# function to handle API Gateway Lambda proxy integration event
def api_gateway_handler(event):
    body = json.loads(event['body'])
    item = body['vehicle']
    item_id = item['id']
    create_item(item)
    update_item(item, "yes")
    ret = get_item(item_id)
    
    return {
        'statusCode': '200',
        'body': json.dumps(ret),
        'headers': {
            'Content-Type': 'application/json',
        }
    }

# Function to handle Lambda Local Test
def local_test_handler(event):
    item = event['vehicle']
    item_id = item['id']
    create_item(item)
    update_item(item, "yes")
    ret = get_item(item_id)
    return ret

def lambda_handler(event, context):
    logger.info(event)
    try:
        ret = api_gateway_handler(event)
    except:
        ret = local_test_handler(event)
    return ret
