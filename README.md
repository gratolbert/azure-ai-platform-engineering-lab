> Portfolio Project
>
> Production-style Azure AI Platform demonstrating secure cloud-native application deployment using Azure Container Apps, Cosmos DB, Key Vault, Managed Identity, and Azure Monitoring.

# Azure AI Platform Engineering Lab

![Azure](https://img.shields.io/badge/Azure-AI%20Platform-blue)
![Containers](https://img.shields.io/badge/Containers-AKS%20%7C%20ACA-green)
![Status](https://img.shields.io/badge/Status-Phase%2015%20Complete-success)
![AI](https://img.shields.io/badge/AI-Vector%20Search-orange)

## Executive Summary

This project demonstrates the deployment of a secure cloud-native AI platform on Microsoft Azure.

Production-style Azure AI Platform demonstrating secure cloud-native application deployment using Azure OpenAI, Azure Functions, Azure Container Apps, Azure Container Registry, Cosmos DB, Key Vault, Managed Identity, Service Bus, and Azure Monitoring.

The solution follows Azure Well-Architected Framework principles emphasizing:

- Security
- Reliability
- Operational Excellence
- Cost Optimization
- Performance Efficiency
- FastAPI AI Microservice
- Azure OpenAI Ticket Summarization API
- Dockerized REST API Deployment

## Table of Contents

- Executive Summary
- Solution Architecture
- Technologies Used
- Phase 3 – Container Apps
- Phase 4 – Managed Identity & Key Vault
- Phase 5 – Cosmos DB
- Phase 6 – Service Bus
- Phase 7 – Azure Functions & Identity
- Phase 8 – Azure OpenAI
- Phase 9 – Containerization and Azure Container Apps
- Phase 10 – FastAPI AI Microservice
- Security Architecture
- Skills Demonstrated
- Resume Value
- Future Enhancements

## Overview

This project demonstrates the design and deployment of an Azure AI platform using modern cloud-native services.

The lab covers:

- Azure Container Registry (ACR)
- Azure Container Apps
- Azure Service Bus
- Azure Functions
- Azure Cosmos DB
- Azure Key Vault
- Managed Identity
- Azure RBAC
- Azure Monitor
- Log Analytics
- Application Insights

## Technologies Used

### Application Frameworks

- FastAPI
- Pydantic


### Azure Services

- Azure Container Registry
- Azure Container Apps
- Azure Functions
- Azure Service Bus
- Azure Cosmos DB
- Azure Key Vault
- Managed Identity
- Azure Monitor
- Log Analytics
- Application Insights
- Azure OpenAI
- Azure AI Foundry


### Development Tools

- Docker
- Git
- GitHub
- Azure Portal
- Azure CLI
- Azure Functions Core Tools


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

## Solution Architecture

The platform consists of multiple Azure services working together to provide a secure and scalable AI application foundation.


GitHub
   │
   ▼
Azure Container Registry
   │
   ▼
Azure Container Apps
(FastAPI API)
   │
   ▼
Azure OpenAI

Azure Service Bus
   │
   ▼
Azure Functions
   │
   ▼
Azure Cosmos DB

Application Insights
   │
   ▼
Log Analytics


![Complete Architecture](screenshots/39-complete-ai-platform-architecture.png)

### Azure Resource Visualizer

Azure Resource Visualizer was used to validate resource relationships and dependency mapping across the platform.

![Resource Visualizer](screenshots/41-resource-visualizer.png)

### Architecture Components

| Service | Purpose |
|----------|----------|
| Azure Container Apps | Application Hosting |
| Azure Container Registry | Container Image Storage |
| Azure Key Vault | Secret Management |
| Azure Cosmos DB | Data Storage |
| Managed Identity | Authentication |
| Log Analytics | Monitoring |
| Resource Group | Resource Organization |



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

Container App
      │
Managed Identity
      │
RBAC Authorization
      │
Azure Key Vault
      │
Application Secrets

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
| Key Vault Secrets User | func-ai-platform-grant01 |

This allows the application to securely retrieve secrets without storing credentials in code.

![Key Vault RBAC](screenshots/11-keyvault-rbac.png)

### Security Benefits

- No hardcoded secrets
- Managed Identity authentication
- Role-Based Access Control (RBAC)
- Centralized secret management
- Production-ready Azure security pattern

## Phase 5 – Azure Cosmos DB

### Objective

Deploy a globally distributed NoSQL database to support AI application data storage and retrieval.

### Components Created

- Cosmos DB Account
- SQL Database
- Container
- Connection String Secret
- Key Vault Integration

### Configuration

| Setting | Value |
|----------|----------|
| API | NoSQL |
| Capacity Mode | Serverless |
| Region | East US |
| Backup Policy | Periodic |
| Authentication | Key-Based |

### Database Creation

![Cosmos DB Overview](screenshots/19-cosmosdb-overview.png)

### Database

Database Name:

ai-platform-db

![Database Created](screenshots/20-cosmosdb-database-created.png)

### Container

Container Name:

chat-history

Partition Key:

/partitionKey

![Container Created](screenshots/21-cosmosdb-container-created.png)

### Secure Secret Storage

Cosmos DB connection strings were stored securely in Azure Key Vault.

![Cosmos DB Keys](screenshots/22-cosmosdb-keys.png)

![Key Vault Cosmos Secret](screenshots/23-keyvault-cosmos-secret.png)

## Security Architecture

The platform implements a Zero Trust security model.

### Security Controls

- Managed Identity Authentication
- Azure RBAC Authorization
- Key Vault Secret Storage
- No Hardcoded Credentials
- Encrypted Communications
- Azure AD Integration

### Authentication Flow

Container App
↓
Managed Identity
↓
Azure RBAC
↓
Azure Key Vault
↓
Cosmos DB Credentials

### Benefits

- Eliminates credential sprawl
- Reduces attack surface
- Supports enterprise compliance
- Enables secret rotation

## Phase 6 – Azure Service Bus

### Objective

Implement asynchronous messaging using Azure Service Bus.

### Components

- Service Bus Namespace
- Queue
- Message Processing Workflow

### Queue

chat-processing

### Benefits

- Loose coupling
- Event-driven architecture
- Reliable messaging
- Cloud-native scalability

### Skills Demonstrated

- Azure Service Bus
- Messaging Systems
- Event-Driven Design
- Cloud Integrations

## Phase 7 – Azure Functions and Identity Integration

### Objective

Implement serverless compute using Azure Functions and secure resource access using Managed Identity.

### Components Created

- Azure Function App
- Application Insights
- Storage Account
- Function App Managed Identity

### Security Configuration

Assigned:

- Azure Service Bus Data Receiver
- Key Vault Secrets User

### Benefits

- Event-driven processing
- Serverless execution
- Secretless authentication
- Enterprise RBAC model

### Validation

![Function App Overview](screenshots/40-function-app-overview.png)

![Function Managed Identity](screenshots/35-functionapp-managed-identity.png)

![Key Vault Role Assignment](screenshots/37-keyvault-role-assignment-complete.png)

## Phase 8 – Azure Functions and Azure OpenAI Integration

### Objective

Build a serverless AI-powered API using Azure Functions and Azure OpenAI.

### Components

* Azure Function App (Python 3.12)
* Azure OpenAI GPT-4.1-mini
* Azure AI Foundry
* Azure CLI
* Azure Functions Core Tools

### Solution

A Python-based HTTP-triggered Azure Function was developed and deployed to Azure. The function accepts IT support ticket text, submits the content to Azure OpenAI, and returns an AI-generated summary.

### Validation

* Local Function execution successful
* Azure OpenAI connectivity validated
* GPT-4.1-mini deployment validated
* Function App deployment successful
* Cloud endpoint tested successfully

![Function App Overview](screenshots/50-function-app-overview.png)

![Managed Identity](screenshots/51-function-managed-identity.png)

![Environment Variables](screenshots/52-function-environment-variables.png)

![Deployment Success](screenshots/55-function-publish-success.png)

![Cloud Function Test](screenshots/56-cloud-function-test.png)



### Result

The solution demonstrates serverless AI integration using Azure-native services and provides a reusable pattern for automated ticket summarization, incident enrichment, and AI-assisted operations workflows.

## Phase 9 – Containerization and Azure Container Apps

### Objective

Containerize the Azure OpenAI test application and deploy it using Azure Container Registry (ACR) and Azure Container Apps.

### Components

- Docker Desktop
- Azure Container Registry (ACR)
- Azure Container Apps
- Azure Managed Identity
- Azure RBAC
- Azure OpenAI
- Azure CLI

### Solution

A Python-based Azure OpenAI test application was containerized using Docker and built into a reusable container image. The image was tagged and pushed to Azure Container Registry, then deployed to Azure Container Apps using a system-assigned managed identity for secure image access.

The deployment process included configuring registry authentication, assigning the AcrPull role, and validating Azure OpenAI connectivity from within the containerized workload.

### Validation

- Docker image built successfully
- Local container execution successful
- Azure Container Registry authentication successful
- Container image pushed to ACR successfully
- Managed Identity configured
- AcrPull role assigned
- Azure Container App configured to use custom container image
- Azure OpenAI connectivity validated from containerized application


### Troubleshooting

Container App revision diagnostics revealed that the containerized application was implemented as a one-time execution script rather than a long-running service. The application successfully authenticated to Azure OpenAI, generated a response, and exited normally.

This behavior validated the container image and Azure OpenAI integration while demonstrating the operational differences between short-lived container workloads and continuously running containerized services.

### Result

Successfully demonstrated containerization, Azure Container Registry integration, managed identity authentication, Azure RBAC authorization, and Azure Container Apps deployment workflows while validating Azure OpenAI functionality from a containerized environment.

## Phase 10 – FastAPI AI Microservice Deployment

### Objective

Build and deploy a production-style AI-powered REST API using FastAPI, Azure OpenAI, Docker, Azure Container Registry, and Azure Container Apps.

### Components

* FastAPI
* Azure OpenAI
* Docker
* Azure Container Registry (ACR)
* Azure Container Apps
* Azure CLI
* Azure AI Foundry

### Solution

A FastAPI-based microservice was developed to expose Azure OpenAI capabilities through a secure REST API.

The service accepts IT support ticket text through an HTTP POST endpoint and returns AI-generated ticket summaries using Azure OpenAI.

The application was containerized using Docker, stored in Azure Container Registry, and deployed to Azure Container Apps with external HTTPS ingress enabled.

### API Endpoints

#### Health Endpoint

```http
GET /
```

Response:

```json
{
  "status": "healthy"
}
```

#### Ticket Summarization Endpoint

```http
POST /summarize
```

Example Request:

```json
{
  "text": "User cannot connect to VPN after password reset and receives MFA errors."
}
```

Example Response:

```json
{
  "summary": "User is unable to connect to VPN following a password reset and is encountering MFA authentication issues."
}
```

### Validation

* FastAPI application developed successfully
* Docker image built successfully
* Image pushed to Azure Container Registry
* Azure Container App deployed successfully
* Public HTTPS endpoint validated
* Azure OpenAI integration validated
* AI ticket summarization validated
* Health endpoint validated

### Skills Demonstrated

* FastAPI Development
* REST API Design
* Azure OpenAI Integration
* Docker Containerization
* Azure Container Registry
* Azure Container Apps
* Cloud-Native Application Deployment
* AI Platform Engineering

### Result

Successfully deployed a production-style AI microservice on Azure that exposes Azure OpenAI functionality through a containerized REST API architecture.


### Screenshots

![Docker Version](screenshots/57-docker-version-validation.png)

![Docker Build Success](screenshots/60-docker-build-success.png)

![ACR Login](screenshots/62-acr-login-success.png)

![Image Push](screenshots/64-acr-image-pushed.png)

![Container App Image](screenshots/68-container-app-running-custom-image.png)

![Revision Diagnostics](screenshots/69-container-app-revision-diagnostics.png)

![Local Container Success](screenshots/70-local-container-successful-execution.png)

![Local Container Success](screenshots/83-fastapi-health-endpoint-success.png)

## Phase 11 – GitHub Actions CI/CD Pipeline

### Objective
Automate containerized application deployments using GitHub Actions.

### Technologies
- GitHub Actions
- Azure Container Registry (ACR)
- Azure Container Apps
- Docker
- Azure Service Principal Authentication

### Pipeline Workflow

Developer Push
↓
GitHub Actions
↓
Build Docker Image
↓
Push to Azure Container Registry
↓
Deploy New Container App Revision

### Outcomes
- Automated build process
- Automated container image publishing
- Automated deployment to Azure Container Apps
- Secure secret management through GitHub Repository Secrets
- Production-ready CI/CD workflow

### Evidence

| Screenshot | Description |
|------------|-------------|
| 86 | GitHub Actions pipeline completed successfully |
| 87 | Production deployment workflow |
| 88 | Container App running after automated deployment |
| 89 | New revision created via GitHub Actions |
| 90 | Container image published to ACR |
| 91 | Health endpoint validation |
| 92 | Azure OpenAI summarization endpoint validation |

### Lessons Learned

During deployment validation, Azure OpenAI authentication failures were traced to an outdated API key stored within Azure Container Apps environment variables. After rotating Azure OpenAI keys, dependent workloads must be updated and redeployed to consume the new credential.

Troubleshooting involved:

* GitHub Actions pipeline validation
* Azure Container Apps revision analysis
* Container log inspection
* FastAPI exception tracing
* Azure OpenAI authentication diagnostics

The issue was resolved by updating the Azure Container App environment variable with the current Azure OpenAI API key, triggering a new deployment revision.


### Cloud Platforms

- Microsoft Azure

### Compute

- Azure Container Apps
- Containerized Applications

### Containers

- Docker
- Azure Container Registry

### Security

- Azure Key Vault
- Managed Identity
- RBAC
- Secret Management

### Databases

- Azure Cosmos DB
- NoSQL

### Monitoring

- Log Analytics
- Azure Monitoring

### DevOps

- Git
- GitHub
- CI/CD Concepts

### Architecture

- Cloud Architecture Design
- Resource Visualization
- Production Deployments

### Advanced Skills Demonstrated
- Azure Cosmos DB
- NoSQL Database Design
- Serverless Databases
- Secure Secret Management
- Cloud Data Architecture
- Azure Key Vault
- Managed Identity
- RBAC
- Zero-Trust Security
- Secretless Authentication

## Skills Matrix

| Category   | Skills                              |
|----------- |-------------------------------------|
| Compute    | Container Apps, Azure Functions     |
| Security   | Key Vault, RBAC, Managed Identity   |
| Messaging  | Service Bus                         |
| Databases  | Cosmos DB                           |
| Monitoring | Application Insights, Log Analytics |
| DevOps     | Git, GitHub, Docker                         |
| Cloud      | Microsoft Azure                     |
| Compute    | Container Apps, Azure Functions     |

## Project Outcomes

- Deployed 12+ Azure services
- Developed and deployed a FastAPI AI microservice
- Integrated Azure OpenAI into serverless and containerized workloads
- Built and published Docker images to Azure Container Registry
- Deployed production-style REST APIs to Azure Container Apps

## Resume Value

This project demonstrates:

- Azure Container Apps
- Azure Functions
- Azure Service Bus
- Azure Cosmos DB
- Azure Key Vault
- Managed Identity
- Azure RBAC
- Application Insights
- Log Analytics
- Event-Driven Architecture
- Serverless Computing
- Cloud-Native Security
- Production Troubleshooting
- Azure OpenAI
- Azure AI Foundry
- Azure Container Registry
- Docker
- Azure CLI
- AI Platform Engineering
- Containerized Workloads
- FastAPI
- REST API Development
- Docker Containerization
- Azure Container Registry
- Azure Container Apps
- Azure OpenAI Integration
- AI Microservices

## Future Enhancements

- GitHub Actions Container CI/CD Pipeline
- Automated ACR Image Builds
- Automated Azure Container Apps Deployments
- API Authentication and Authorization
- OpenAPI / Swagger Documentation