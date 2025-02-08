# solita-train-case

Cloud Composer and BigQuery with Terraform
This project sets up a Cloud Composer environment and a BigQuery dataset using Terraform. It then leverages Cloud Composer to create an Airflow DAG that fetches train data from the Digitraffic API, stores it in BigQuery, and prepares it for future predictions.

Project Overview
Terraform is used to manage infrastructure on Google Cloud.
Google Cloud Composer (Apache Airflow) is used for orchestrating the ETL pipeline.
BigQuery is used for storing the fetched train data and performing predictions.
Architecture
Terraform Configuration:
Creates a Cloud Composer environment.
Creates a BigQuery dataset and a table to store train data.
Cloud Composer (Airflow):
Fetches data from the Digitraffic API.
Stores the fetched data into BigQuery.
Future steps will involve making predictions based on the stored data.
Prerequisites
Google Cloud account with necessary permissions.
Terraform installed.
gcloud CLI installed and configured.
Google Cloud SDK authentication set up with an appropriate service account or user.
Setup
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/terraform-composer-bigquery.git
cd terraform-composer-bigquery
2. Set Up Terraform
Initialize Terraform:
bash
Copy
Edit
terraform init
Configure your Google Cloud provider credentials (if not already done):
bash
Copy
Edit
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your-service-account-key.json"
Edit the variables.tf file to set your specific project details, including your project ID and region.
3. Apply Terraform Configuration
Once your variables are configured, run:

bash
Copy
Edit
terraform apply
This will create:

A Cloud Composer environment.
A BigQuery dataset and table for storing train data.
4. Composer DAG for Data Fetching and Prediction
Inside the Composer environment, a DAG will be triggered that:
Fetches train data from the Digitraffic API.
Stores the fetched data into BigQuery.
Prepares data for future predictions.
5. Future Work
Extend the workflow to run machine learning predictions using the data stored in BigQuery.
Set up alerts or triggers based on prediction results.
Directory Structure
bash
Copy
Edit
terraform-composer-bigquery/
│
├── main.tf           # Main Terraform configuration file for Composer and BigQuery
├── variables.tf      # Variables for Terraform configuration
├── outputs.tf        # Output values for Terraform
├── composer/         # Composer DAGs and other related files
│   ├── fetch_data.py # DAG to fetch data from the Digitraffic API and store in BigQuery
└── README.md         # Project readme (you are here!)
Clean Up
To destroy the resources created by Terraform, run:

bash
Copy
Edit
terraform destroy
This will remove the Cloud Composer environment and BigQuery dataset.