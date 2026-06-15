# Why Remote State in Terraform?

Terraform stores the current state of infrastructure in a state file (`terraform.tfstate`).

Keeping the state file on a local machine is not recommended because:

- The file can be accidentally modified or deleted.
- Team members cannot collaborate effectively.
- Different copies of the state file can cause infrastructure drift.
- Sensitive information may be stored in the state file.
- Losing the state file can make infrastructure management difficult.

# Solution

Store the Terraform state file in a centralized and secure location such as an Amazon S3 bucket.

Benefits:

- Single source of truth for infrastructure state.
- Shared access for all team members.
- Improved durability and availability.
- Easier collaboration across environments.

# State Locking with DynamoDB

To prevent multiple users from modifying the infrastructure simultaneously, Terraform state locking is implemented using DynamoDB.

Benefits:

- Prevents concurrent `terraform apply` operations.
- Avoids state corruption.
- Ensures only one user can update the state at a time.

# Architecture

```text
Developer
    |
    v
Terraform
    |
    +--> S3 Bucket (Remote State Storage)
    |
    +--> DynamoDB Table (State Locking)
```