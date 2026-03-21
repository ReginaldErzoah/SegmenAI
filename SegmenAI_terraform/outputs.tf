output "s3_bucket_name" {
  description = "Name of S3 bucket for SegmenAI models"
  value       = aws_s3_bucket.segmenai_bucket.bucket
}

output "iam_role_arn" {
  description = "ARN of IAM role for Streamlit app"
  value       = aws_iam_role.segmenai_role.arn
}