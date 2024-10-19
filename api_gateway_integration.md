# API Gateway Integration Guide

This guide explains how to set up API Gateway to integrate with the Lambda function for the Serverless Vehicle Inventory Management System.

## Steps:

1. **Create a new REST API:**
   - Go to the **API Gateway** service in the AWS Management Console.
   - Click **Create API**, then choose **REST API**.

2. **Create Resources and Methods:**
   - Add a new resource `/vehicle`.
     - Create **POST** method for adding vehicles.
     - Create **PUT** method for updating reservations.
     - Create **GET** method for retrieving vehicle details.

3. **Configure Lambda Integration:**
   - For each method (POST, PUT, GET), set up integration with the Lambda function.
   - In **Method Execution**:
     - Choose **Lambda Function** as the integration type.
     - Enter your Lambda function’s name.
     - Enable **Lambda Proxy Integration**.

4. **Deploy the API:**
   - Once the resources and methods are configured, click **Deploy API**.
   - Choose an existing stage or create a new one, and note the **Invoke URL** for testing.

5. **Testing the API:**
   - You can use tools like **Postman** or **curl** to test the API endpoints.
   - Example `POST` request:
     ```bash
     curl -X POST https://your-api-id.execute-api.region.amazonaws.com/dev/vehicle \
     -H 'Content-Type: application/json' \
     -d '{
           "vehicle": {
             "id": "1",
             "available": "true",
             "type": "scooter"
           }
         }'
     ```
