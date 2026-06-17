output "public_ip" {
  description = "EC2 Public IP Address"
  value       = aws_instance.devops_server.public_ip
}

output "instance_id" {
  description = "EC2 Instance ID"
  value       = aws_instance.devops_server.id
}

output "public_dns" {
  description = "EC2 Public DNS"
  value       = aws_instance.devops_server.public_dns
}