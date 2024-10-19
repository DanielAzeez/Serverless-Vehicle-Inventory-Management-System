# DynamoDB Table Creation Guide

Follow these steps to create a DynamoDB table for storing vehicle data.

## Step 1: Open DynamoDB Console
1. Navigate to the **DynamoDB** section of the AWS Management Console.
2. Click **Create Table**.

## Step 2: Define Table Settings
1. **Table Name**: `locations`
2. **Primary Key**: `id` (String)

## Step 3: Configure Table Settings
1. Set **Provisioned Capacity** or **On-Demand** as per your requirements.
2. Optionally, configure **Auto Scaling** to automatically adjust read and write capacity.

## Step 4: Create the Table
1. Click **Create** to finish setting up the table.

## Step 5: Insert Data
Once the table is created, you can start inserting vehicle records using the Lambda function or through the DynamoDB console.

