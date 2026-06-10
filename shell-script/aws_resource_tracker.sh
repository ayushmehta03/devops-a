#!/bin/bash


# to implement cron job:

#crontab -e
#*/5 * * * * /Users/ayushmehta/aws_resource_tracker.sh



# this script will report the aws resource usage

############################

# AWS S3
# AWS EC2
# AWS Lambda
# AWS IAM Users

set -x

# list s3 buckets
aws s3 ls

# list ec2 instances
aws ec2 describe-instances | jq '.Reservations[].ReservationId'

# list lambda functions
aws lambda list-functions

# list iam users
aws iam list-users