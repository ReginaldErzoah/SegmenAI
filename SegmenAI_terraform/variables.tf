variable "aws_region" {
  description = "AWS region to deploy resources"
  default     = "us-east-1"
}

variable "s3_bucket_name" {
  description = "S3 bucket to store SegmenAI model and scaler"
  default     = "segmenai-model-bucket-reginald-2026"  
}

variable "iam_role_name" {
  description = "IAM role name for SegmenAI Streamlit app"
  default     = "SegmenAI_Streamlit_Role"
}