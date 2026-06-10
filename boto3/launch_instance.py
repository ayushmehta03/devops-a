import boto3
import os
from dotenv import load_dotenv

load_dotenv()

ec2_client = boto3.client(
    "ec2",
    region_name=os.getenv("AWS_REGION")
)

response = ec2_client.run_instances(
    ImageId=os.getenv("AMI_ID"),
    InstanceType=os.getenv("INSTANCE_TYPE"),
    KeyName=os.getenv("KEY_NAME"),
    SecurityGroupIds=[
        os.getenv("SECURITY_GROUP_ID")
    ],
    MinCount=1,
    MaxCount=1,
    TagSpecifications=[
        {
            "ResourceType": "instance",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": os.getenv("INSTANCE_NAME")
                }
            ]
        }
    ]
)

instance_id = response["Instances"][0]["InstanceId"]

print("EC2 Instance Created Successfully")
print(f"Instance ID : {instance_id}")