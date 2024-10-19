import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key
import logging
import json

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize DynamoDB resource
session = boto3.Session()
dynamodb = session.resource("dynamodb")

# Replace with the DynamoDB table name
table_name = "locations"
table = dynamodb.Table(table_name)

# Create an item in DynamoDB
def create_item(item):
    try:
        response = table.put_item(Item=item)
        logger.info({"operation": "create_item", "details": response})
    except ClientError as err:
        logger.error({"operation": "create_item_error", "details": str(err)})

# Update an item in DynamoDB
def update_item(item_id, reserve):
    try:
        response = table.update_item(
            Key={'id': item_id},
            UpdateExpression="set reserve = :r",
            ExpressionAttributeValues={':r': reserve},
            ReturnValues="UPDATED_NEW"
        )
        logger.info({"operation": "update_item", "details": response})
    except ClientError as err:
        logger.error({"operation": "update_item_error", "details": str(err)})

# Retrieve an item from DynamoDB
def get_item(item_id):
    try:
        response = table.get_item(Key={'id': item_id})
        if 'Item' in response:
            return response['Item']
        else:
            logger.info(f"Item with ID {item_id} not found")
            return None
    except ClientError as err:
        logger.error({"operation": "get_item_error", "details": str(err)})

# Lambda function handler
def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        item = body['vehicle']
        item_id = item['id']

        create_item(item)
        update_item(item_id, "yes")
        vehicle = get_item(item_id)

        return {
            'statusCode': 200,
            'body': json.dumps(vehicle),
            'headers': {'Content-Type': 'application/json'}
        }
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({"error": "Internal Server Error"})
        }
