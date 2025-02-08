variable "bucket_name" {
  description = "The name of the GCP Storage bucket"
  type        = string
  default     = ""
}

variable "region" {
  description = "The region for GCP resources"
  type        = string
  default     = "europe-north1" 
}

variable "project_id" {
  description = "The GCP project ID"
  type        = string
  default =  ""
}