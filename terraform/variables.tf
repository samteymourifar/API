variable "region" {
  type    = string
  default = "us-east-1"
}

variable "eks_cluster_name" {
  type = string
#   default = "dev"
  default = "education-eks-2we6PjFu"
}

variable "eks_oidc_provider_arn" {
  type = string
  default = "arn:aws:iam::533267095186:oidc-provider/oidc.eks.us-east-1.amazonaws.com/id/2BE79E797C751654A84789802F8D17B9"
}

variable "dynamodb_table_name" {
  type    = string
  default = "requests-log-table"
}

variable "prefix" {
  type    = string
  default = "demo"
}

variable "k8s_namespace" {
  type    = string
  default = "default"
}

variable "service_account_name" {
  type    = string
  default = "app-serviceaccount"
}
