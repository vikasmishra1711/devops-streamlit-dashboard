variable "aws_region" {
  description = "AWS Region"
  default     = "ap-south-1"
}

variable "instance_type" {
  description = "EC2 Instance Type"
  default     = "t3.micro"
}

variable "key_name" {
  description = "AWS Key Pair Name"
  type        = string
}

variable "ami_id" {
  description = "Amazon Linux 2023 AMI"
  type        = string
}