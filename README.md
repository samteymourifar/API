## Table of Contents

- [Prerequisites](#prerequisites)
- [Usage](#usage)
  - [Q1_1](#q11)
    - [Running the Script](#running-the-script)
    - [Example Results](#example-results)
  - [Q1_2](#q12)
    - [Running the Application](#running-the-application)
    - [Making Requests](#making-requests)
- [Improvements](#improvements)


---

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.x** is installed on your machine.
- **kubectl** is installed and configured to interact with your Kubernetes cluster.
- **Terraform** is installed for infrastructure management.

---

## Usage

### Q1_1

#### Running the Script

To execute the `sum_pairs.py` script, navigate to the repository directory in your terminal and run:

```bash
python sum_pairs.py

Example #1 result:
Pairs: (4, 12) (6, 10) have sum: 16
Pairs: (22, 32) (12, 42) have sum: 54
Pairs: (12, 21) (11, 22) have sum: 33
Pairs: (10, 22) (11, 21) have sum: 32
Pairs: (10, 54) (22, 42) have sum: 64
Pairs: (11, 32) (21, 22) have sum: 43
Pairs: (21, 32) (11, 42) have sum: 53
Example #2 result:
Pairs: (4, 12) (6, 10) have sum: 16
Pairs: (22, 32) (12, 42) have sum: 54
Pairs: (12, 21) (11, 22) have sum: 33
Pairs: (10, 22) (11, 21) have sum: 32
Pairs: (10, 54) (22, 42) have sum: 64
Pairs: (11, 32) (21, 22) have sum: 43
Pairs: (21, 32) (11, 42) have sum: 53

Example #3 result:
Pairs: (23, 67) (4, 86) have sum: 90
```


Q1_2
Running the Application
To start the application, run:

```bash
python app.py

# Use the following curl commands to interact with the application:

curl -X GET -H "Content-Type: application/json" \
     -d '{"data":[6,4,4,4,4,4,12,10,22,54,32,42,21,11]}' \
     http://127.0.0.1:5000/assignment

```

Q2:
Use port forward to access app without ingress
```bash
kubectl port-forward service/assignment-service 5001:5000
curl -X GET -H "Content-Type: application/json" \
     -d '{"data":[6,4,4,4,4,4,12,10,22,54,32,42,21,11]}' \
     http://127.0.0.1:5001/assignment

json
{
  "results": [
    {"pairs": [[4, 12], [6, 10]], "sum": 16},
    {"pairs": [[22, 32], [12, 42]], "sum": 54},
    {"pairs": [[12, 21], [11, 22]], "sum": 33},
    {"pairs": [[10, 22], [11, 21]], "sum": 32},
    {"pairs": [[10, 54], [22, 42]], "sum": 64},
    {"pairs": [[11, 32], [21, 22]], "sum": 43},
    {"pairs": [[21, 32], [11, 42]], "sum": 53}
  ]
}
```
Improvements
Here are some potential enhancements for the project:

### Add Tests in CI:
Integrate automated tests into the Continuous Integration (CI) pipeline to ensure code quality and reliability.

### Implement Proper Continuous Deployment (CD) to Kubernetes:
Utilize tools like Helm, Argo CD, or Flux v2 for streamlined and automated deployments to Kubernetes clusters.

### Update IAM Roles for Service Accounts (IRSA):
Transition from using IRSA to Pod Identity for accessing DynamoDB, leveraging the latest best practices.

### Modularize Terraform Configuration:
Create reusable Terraform modules instead of maintaining all configurations in a single folder to enhance maintainability and scalability.

### Enhance Kubernetes Resilience:
Add Pod Disruption Budgets and other resilience features to Kubernetes deployments to ensure high availability and fault tolerance.

### Implement Ingress Management:
Configure and manage Ingress resources to handle external access to the services more effectively.




