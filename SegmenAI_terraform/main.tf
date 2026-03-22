terraform {
  required_providers {
    cloudflare = {
      source  = "cloudflare/cloudflare"
      version = ">= 5.0.0"
    }
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.100.0"
    }
  }
  required_version = ">= 1.14.7"
}

provider "cloudflare" {
  email   = var.cloudflare_email
  api_key = var.cloudflare_api_key
}

provider "aws" {
  access_key = var.R2_ACCESS_KEY_ID
  secret_key = var.R2_SECRET_ACCESS_KEY
  region     = "auto"
  s3_force_path_style = true
  endpoint   = var.R2_ENDPOINT_URL
}

# Reference existing bucket
data "cloudflare_r2_bucket" "existing_bucket" {
  account_id  = var.cloudflare_account_id
  bucket_name = var.bucket_name
}

# Upload new customer data CSV
resource "cloudflare_r2_object" "customer_csv" {
  bucket = data.cloudflare_r2_bucket.existing_bucket.name
  key    = "customerdata.csv"        # name in the bucket
  content = file(var.local_csv_path) # path to CSV in your repo

  depends_on = [data.cloudflare_r2_bucket.existing_bucket]
}