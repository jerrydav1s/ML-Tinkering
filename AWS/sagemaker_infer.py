import boto3
import json

# Set up the SageMaker runtime client
runtime = boto3.client('runtime.sagemaker')

# Specify the endpoint name
endpoint_name = 'huggingface-pytorch-inference-2024-04-18-07-51-46-273' # CHange this to your endpoint

# Prepare the input data
input_data = {
    "inputs": {
        "question": "What is my name?",
		"context": "My name is Jeff and I live in Berkeley."	
    }
}

# Convert the input data to JSON string
payload = json.dumps(input_data)

# Make a request to the endpoint
response = runtime.invoke_endpoint(
    EndpointName=endpoint_name,
    ContentType='application/json',
    Body=payload
)

# Parse the response
output = json.loads(response['Body'].read().decode())
answer = output['answer']

# Print the model's prediction
print(answer)
