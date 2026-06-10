import boto3
import os
from dotenv import load_dotenv

load_dotenv()

ec2_client = boto3.client(
    "ec2",
    region_name=os.getenv("AWS_REGION")
)

instance_id = os.getenv("INSTANCE_ID")

response = ec2_client.describe_instance_status(
    InstanceIds=[instance_id]
)

statuses = response.get("InstanceStatuses", [])

if not statuses:
    print(
        f"Instance {instance_id} is pending or not found."
    )
else:
    state = statuses[0]["InstanceState"]["Name"]

    print(
        f"Instance {instance_id} is {state}"
    )