provider "aws" {
  region = var.region
}

resource "aws_dynamodb_table" "requests_table" {
  name           = var.dynamodb_table_name
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "requestId"
  attribute {
    name = "requestId"
    type = "S"
  }
}
