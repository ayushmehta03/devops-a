# Terraform AWS EC2 Deployment (Local State)

This project demonstrates how to provision and manage a basic AWS infrastructure using Terraform with a local state backend. It sets up an Amazon Linux 2023 EC2 instance inside a specified AWS region.

## Prerequisites

Before running the Terraform commands, ensure you have completed the following setup:

1. **Install Terraform**: Download and install the Terraform CLI on your local machine.
2. **Configure AWS CLI**: Run `aws configure` in your terminal to set up your AWS credentials (`Access Key ID` and `Secret Access Key`) and your default deployment region.

---

## Essential Terraform Commands

The following workflow is used to manage the infrastructure lifecycle:

* **`terraform init`** Initializes the working directory. This downloads the necessary cloud provider plugins (like the AWS provider) specified in the configuration.
  
* **`terraform plan`** Generates a dry-run execution plan, allowing you to preview the exact changes Terraform will make to your cloud infrastructure before applying them.
  
* **`terraform apply`** Executes the configuration script and provisions the real-world resources inside your AWS account.
  
* **`terraform destroy`** Completely terminates, deprovisions, and cleans up all infrastructure resources managed by this configuration.

---

## Configuration Breakdown (`main.tf`)

The infrastructure blueprint is divided into four main sections:

1. **Terraform & Provider Block** Defines the minimum required Terraform version (`>= 1.5.7`) and downloads the correct version of the HashiCorp AWS provider (`~> 6.0`).
   
2. **AWS Provider Setup** Configures the target AWS region (e.g., `us-west-2`) where all your resources will be deployed.
   
3. **Dynamic AMI Data Source** Uses built-in filters to dynamically query and fetch the latest, official **Amazon Linux 2023 AMI** ID at runtime, avoiding the need to hardcode brittle image IDs.
   
4. **EC2 Resource Definition** Deploys a Free Tier eligible `t3.micro` instance using the dynamically fetched AMI ID and assigns specific identification tags (`Name = "Terraform_Demo"`).

---

## Important Security Note

This project is configured to use a **Local Backend**, meaning your infrastructure's source of truth is stored in a local `terraform.tfstate` file. 

* **Do not modify** the `.tfstate` file manually.
* Ensure your `.gitignore` file is active to **never push** `.terraform/` binaries or `*.tfstate` secrets to your remote Git repository.