terraform {
  backend "gcs" {
    bucket = ""  
    prefix = "terraform/state" 
  }
}

provider "google" {
  project = var.project_id
  region  = var.region

}

# Define Google Cloud Storage bucket
resource "google_storage_bucket" "my_bucket" {
  name          = var.bucket_name
  location      = var.region
  storage_class = "STANDARD"
  force_destroy = true

  versioning {
    enabled = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 30
    }
  }
}


resource "google_bigquery_dataset" "default" {
  dataset_id                      = "ingestion_project"
  default_partition_expiration_ms = 2592000000  # 30 days
  default_table_expiration_ms     =  259200000 # 3 days
  description                     = "Top level ingestion dataset"
  location                        = "EU"
  max_time_travel_hours           = 96 # 4 days

}

# Composer resources

resource "google_composer_environment" "basic_env" {
  name   = "basic-composer-env"
  region = var.region

  config {
    software_config {
      image_version = "composer-2-airflow-2"
    }
  }
}


