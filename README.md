# Azure AI Platform Engineering Lab

![Azure](https://img.shields.io/badge/Azure-AI%20Platform-blue)
![Containers](https://img.shields.io/badge/Containers-AKS%20%7C%20ACA-green)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![AI](https://img.shields.io/badge/AI-Vector%20Search-orange)

## Overview

This project demonstrates the design and deployment of an Azure AI platform using modern cloud-native services.

The lab covers:

- Azure Container Registry (ACR)
- Azure Container Apps
- Azure Kubernetes Service (AKS)
- Azure Cosmos DB Vector Search
- PostgreSQL pgvector
- Azure Managed Redis
- Azure Service Bus
- Azure Event Grid
- Azure Functions
- Azure Key Vault
- Managed Identities
- OpenTelemetry
- Azure Monitor
## Azure Container Registry

An Azure Container Registry (ACR) instance was deployed to provide a private container image repository for Container Apps and Azure Kubernetes Service (AKS).

### Configuration

- SKU: Basic
- Authentication: Azure AD
- Purpose: Container image storage and distribution
## Phase 3 – Azure Container Apps

### Objective

Deploy a containerized application using Azure Container Apps and validate external HTTP access.

### Components Deployed

- Azure Container Apps Environment
- Azure Container App
- Log Analytics Workspace
- External HTTP Ingress

### Configuration

| Setting | Value |
|----------|--------|
| Region | East US |
| Workload Profile | Consumption |
| CPU | 0.25 |
| Memory | 0.5 Gi |
| Ingress | Enabled |
| Target Port | 80 |

### Validation

The application was successfully deployed and exposed through a public HTTPS endpoint.

**Application URL Validation**

![Container App Running](screenshots/07-container-app-running.png)

### Troubleshooting Encountered

During deployment, the initial Container Apps Environment entered a `ScheduledForDelete` state which prevented new application deployments.

Resolution:

- Created replacement environment `cae-ai-platform-v2`
- Redeployed application
- Verified successful application availability

### Skills Demonstrated

- Azure Container Apps
- Serverless Containers
- Application Ingress
- Azure Monitoring Integration
- Deployment Troubleshooting
## Phase 4 – Managed Identity and Azure Key Vault

### Objective

Implement secure secret management using Azure Key Vault and System Assigned Managed Identity.

### Architecture

```text
Container App
      │
Managed Identity
      │
RBAC Authorization
      │
Azure Key Vault
      │
Application Secrets
```

### Managed Identity Configuration

System Assigned Managed Identity was enabled on the Azure Container App.

![Managed Identity Enabled](screenshots/08-managed-identity-enabled.png)

### Azure Key Vault

Created:

- kv-ai-platform-grant

Stored Secrets:

- openai-api-key
- cosmos-connection-string

![Key Vault Overview](screenshots/09-keyvault-overview.png)

![Key Vault Secrets](screenshots/10-keyvault-secrets.png)

### RBAC Authorization

Assigned:

| Role | Principal |
|--------|-----------|
| Key Vault Secrets User | cae-ai-platform-v2 |

This allows the application to securely retrieve secrets without storing credentials in code.

![Key Vault RBAC](screenshots/11-keyvault-rbac.png)

### Security Benefits

- No hardcoded secrets
- Managed Identity authentication
- Role-Based Access Control (RBAC)
- Centralized secret management
- Production-ready Azure security pattern

### Skills Demonstrated

- Azure Key Vault
- Managed Identity
- RBAC
- Zero-Trust Security
- Secretless Authentication