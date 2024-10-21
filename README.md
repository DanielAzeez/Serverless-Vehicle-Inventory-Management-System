# Serverless-Vehicle-Inventory-Management-System

This is a serverless vehicle inventory management system built using **AWS Lambda** and **Amazon DynamoDB**. It allows you to manage vehicle inventory with the ability to **create**, **update**, and **query** vehicle data. The system is built entirely using **Python (Boto3)**, and integrates with AWS services such as DynamoDB and optionally API Gateway.

## 🌟 Features

- **Create a Vehicle**: Add a new vehicle to the inventory.
- **Update a Vehicle**: Modify vehicle attributes such as `reserve` status.
- **Query a Vehicle**: Retrieve vehicle details using its `id`.

---

## 🛠 Technologies Used

- **AWS Lambda**: Used for running the serverless vehicle management code.
- **Amazon DynamoDB**: NoSQL database to store vehicle inventory.
- **Python (Boto3)**: AWS SDK for Python to interact with DynamoDB.
- **API Gateway**: (Optional) To expose Lambda as an HTTP endpoint.

---

## 📖 Setup and Installation

### Prerequisites
- AWS Account
- A DynamoDB table named `locations` with the primary key as `id`.

### Step-by-Step Guide

1. **Clone this repository**:

    ```bash
    git clone https://github.com/your-username/Serverless-Vehicle-Inventory-Management-System.git
    cd Serverless-Vehicle-Inventory-Management-System
    ```

2. **Upload Lambda function**:
    - Go to the AWS Lambda console and create a new function.
    - Upload the `lambda_function.py` file located in the `lambda/` folder.

3. **Configure Lambda to access DynamoDB**:
    - Attach the necessary IAM role to allow the Lambda function to interact with DynamoDB.
    - Example policy:
    ```json
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:GetItem",
        "dynamodb:PutItem",
        "dynamodb:UpdateItem"
      ],
      "Resource": "arn:aws:dynamodb:region:account-id:table/locations"
    }
    ```

4. **DynamoDB Table Setup**:
    - Create a DynamoDB table called `locations` with the primary key as `id` (String).

5. **(Optional) Set Up API Gateway**:
    - If you want to trigger the Lambda function via HTTP requests, create a new API Gateway and integrate it with the Lambda function.
    - Use a POST method to send vehicle data in the request body.

---

## 📋 Usage

### Example Request

- **Payload**: This is an example JSON payload to add a vehicle to the inventory.

```json
{
  "vehicle": {
    "id": "1",
    "available": "true",
    "type": "scooter"
  }
}
```

- **Response**: The Lambda function will respond with the vehicle details, including its `reserve` status.

```json
{
  "id": "1",
  "available": "true",
  "type": "scooter",
  "reserve": "yes"
}
```

---

## 🚀 Testing the Lambda Locally

If you want to test the function locally before deploying it to AWS, you can use sample event data in the following format:

```python
event = {
    "vehicle": {
        "id": "1",
        "available": "true",
        "type": "scooter"
    }
}
```

Then call the `lambda_handler()` function in your Python environment:

```python
result = lambda_handler(event, None)
print(result)
```

---

