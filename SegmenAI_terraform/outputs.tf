# Output the bucket name
output "bucket_name" {
  description = "The name of the Cloudflare R2 bucket used for customer data"
  value       = var.bucket_name
}

# Output the path/key of the uploaded CSV
output "uploaded_csv_key" {
  description = "The key (path) of the customer CSV uploaded to the R2 bucket"
  value       = cloudflare_r2_object.customer_csv.key
}

# Output the full URL of the uploaded CSV
output "uploaded_csv_url" {
  description = "Full URL to access the uploaded CSV in the R2 bucket"
  value       = "${var.S3_ENDPOINT}/${cloudflare_r2_object.customer_csv.key}"
}