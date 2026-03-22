provider "cloudflare" {
  email   = var.cloudflare_email
  api_key = var.cloudflare_api_key
}

# Reference existing bucket
data "cloudflare_r2_bucket" "existing_bucket" {
  name    = var.bucket_name
  zone_id = var.cloudflare_account_id
}

# Upload new customer data CSV
resource "cloudflare_r2_object" "customer_csv" {
  bucket = data.cloudflare_r2_bucket.existing_bucket.name
  key    = "customerdata.csv"        # name in the bucket
  content = file(var.local_csv_path) # path to CSV in your repo

  depends_on = [data.cloudflare_r2_bucket.existing_bucket]
}