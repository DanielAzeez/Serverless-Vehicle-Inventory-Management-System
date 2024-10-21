# Vehicle Inventory Management System - Usage Instructions

## Prerequisites
- AWS Account
- DynamoDB table named `locations` with a primary key `id`.

## Step-by-Step Setup

1. Create a new AWS Lambda function in the AWS Console.
2. Upload the `lambda_function.py` file located in the `lambda/` folder.
3. Ensure your Lambda function has proper IAM permissions to access DynamoDB.
4. (Optional) Set up API Gateway to trigger the Lambda function via HTTP.
5. Test the function with appropriate event payloads.
