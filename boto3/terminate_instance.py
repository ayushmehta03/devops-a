import boto3
import os
from dotenv import load_dotenv

load_dotenv()

ec2_client = boto3.client(
    "ec2",
    region_name=os.getenv("AWS_REGION")
)

instance_id = os.getenv("INSTANCE_ID")

response = ec2_client.terminate_instances(
    InstanceIds=[instance_id]
)

print(
    f"Terminating EC2 Instance {instance_id}..."
)