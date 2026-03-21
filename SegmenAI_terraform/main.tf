# ---------------------
# S3 Bucket for models
# ---------------------
resource "aws_s3_bucket" "segmenai_bucket" {
  bucket = var.s3_bucket_name
  acl    = "private"

  versioning {
    enabled = true
  }

  tags = {
    Name        = "SegmenAI Model Bucket"
    Environment = "Dev"
  }
}

# ---------------------
# IAM Role for Streamlit app
# ---------------------
resource "aws_iam_role" "segmenai_role" {
  name = var.iam_role_name

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action    = "sts:AssumeRole"
        Effect    = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"  # adjust if using Lambda/App Runner
        }
      }
    ]
  })
}

# ---------------------
# IAM Policy to access S3
# ---------------------
resource "aws_iam_policy" "segmenai_s3_policy" {
  name        = "SegmenAI_S3_Policy"
  description = "Allow access to S3 bucket for SegmenAI app"
  policy      = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action   = [
          "s3:GetObject",
          "s3:PutObject",
          "s3:ListBucket"
        ]
        Effect   = "Allow"
        Resource = [
          aws_s3_bucket.segmenai_bucket.arn,
          "${aws_s3_bucket.segmenai_bucket.arn}/*"
        ]
      }
    ]
  })
}

# Attach policy to IAM role
resource "aws_iam_role_policy_attachment" "segmenai_attach" {
  role       = aws_iam_role.segmenai_role.name
  policy_arn = aws_iam_policy.segmenai_s3_policy.arn
}