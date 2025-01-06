data "aws_iam_policy_document" "dynamodb_policy_doc" {
  statement {
    actions   = ["dynamodb:PutItem", "dynamodb:GetItem", "dynamodb:UpdateItem"]
    resources = [aws_dynamodb_table.requests_table.arn]
    effect    = "Allow"
  }
}

resource "aws_iam_policy" "dynamodb_policy" {
  name        = "${var.prefix}-dynamodb-requests"
  description = "Policy to allow writing requests to the DynamoDB table"
  policy      = data.aws_iam_policy_document.dynamodb_policy_doc.json
}

data "aws_eks_cluster" "cluster" {
  name = var.eks_cluster_name
}

data "aws_eks_cluster_auth" "cluster" {
  name = var.eks_cluster_name
}

# OIDC provider for the EKS cluster
data "aws_iam_openid_connect_provider" "oidc" {
  arn = var.eks_oidc_provider_arn
}

resource "aws_iam_role" "irsa_role" {
  name               = "${var.prefix}-irsa-role"
  assume_role_policy = data.aws_iam_policy_document.irsa_assume_role_doc.json
}

data "aws_iam_policy_document" "irsa_assume_role_doc" {
  statement {
    effect = "Allow"
    principals {
      type        = "Federated"
      identifiers = [data.aws_iam_openid_connect_provider.oidc.arn]
    }
    actions = ["sts:AssumeRoleWithWebIdentity"]

    condition {
      test     = "StringEquals"
      variable = "${data.aws_iam_openid_connect_provider.oidc.url}:sub"
      values   = ["system:serviceaccount:${var.k8s_namespace}:${var.service_account_name}"]
    }
  }
}

resource "aws_iam_role_policy_attachment" "attach_dynamodb_policy" {
  policy_arn = aws_iam_policy.dynamodb_policy.arn
  role       = aws_iam_role.irsa_role.name
}
