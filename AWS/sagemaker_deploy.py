import sagemaker
import boto3
from sagemaker.huggingface import HuggingFaceModel

try:
	role = sagemaker.get_execution_role()
except ValueError:
	iam = boto3.client('iam')
	role = iam.get_role(RoleName='PythonSDK')['Role']['Arn'] # CHANGE THE ROLE NAME TO YOUR ENDPOINT

# Hub Model configuration. https://huggingface.co/models
hub = {
	'HF_MODEL_ID':'distilbert/distilbert-base-uncased-distilled-squad',
	'HF_TASK':'question-answering'
}

# create Hugging Face Model Class
huggingface_model = HuggingFaceModel(
	transformers_version='4.37.0',
	pytorch_version='2.1.0',
	py_version='py310',
	env=hub,
	role=role, 
)

# deploy model to SageMaker Inference
predictor = huggingface_model.deploy(
	initial_instance_count=1, # number of instances
	instance_type='ml.m5.xlarge' # ec2 instance type
)


result = predictor.predict({
	"inputs": {
		"question": "What is my name?",
		"context": "My name is Clara and I live in Berkeley."
	},
})

print(result)