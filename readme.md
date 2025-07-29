# Medium post
https://medium.com/@spiegelhaltercurt/end-to-end-ci-cd-with-argocd-github-actions-and-fastapi-on-kubernetes-8fdcab6c12df

# Production CI/CD Pipeline Demo

A complete GitOps CI/CD pipeline demonstrating modern DevOps practices with automated testing, deployment, and monitoring.

## 🏗️ Architecture Overview

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌──────────────┐
│   GitHub    │───▶│ GitHub       │───▶│   ArgoCD    │───▶│ Kubernetes   │
│   Repo      │    │ Actions      │    │  (GitOps)   │    │   Cluster    │
└─────────────┘    └──────────────┘    └─────────────┘    └──────────────┘
                           │                                      │
                           ▼                                      ▼
                   ┌──────────────┐                    ┌──────────────┐
                   │   Container  │                    │ Prometheus   │
                   │   Registry   │                    │ & Grafana    │
                   │   (GHCR)     │                    │ Monitoring   │
                   └──────────────┘                    └──────────────┘
```

## 🛠️ Technology Stack

- **Application**: FastAPI with Prometheus metrics
- **CI/CD**: GitHub Actions for automated testing and building
- **GitOps**: ArgoCD for declarative deployments  
- **Container**: Docker with GitHub Container Registry
- **Orchestration**: Kubernetes (Kind cluster for local dev)
- **Monitoring**: Prometheus for metrics collection
- **Visualization**: Grafana for dashboards and alerting
- **Testing**: pytest for automated test validation

## ✨ Key Features

### 🔄 Continuous Integration
- ✅ Automated testing on every commit
- ✅ Docker image building and pushing
- ✅ Branch-based deployment strategies
- ✅ Quality gates and test validation

### 🚀 Continuous Deployment  
- ✅ GitOps workflow with ArgoCD
- ✅ Zero-downtime rolling deployments
- ✅ Automatic sync and self-healing
- ✅ Rollback capabilities

### 📊 Observability
- ✅ Prometheus metrics collection
- ✅ Grafana visualization dashboards
- ✅ Real-time performance monitoring
- ✅ Custom application metrics

### 🔐 Production Ready
- ✅ Automated testing pipeline
- ✅ Container security scanning
- ✅ Infrastructure as Code
- ✅ Audit trails via Git history

## 🚀 Quick Start

### Prerequisites
- Docker
- kubectl
- kind
- helm
- Git

### 1. Setup Local Cluster
```bash
# Create kind cluster
kind create cluster --name todo-dev

# Install ArgoCD
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Install Prometheus & Grafana
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install monitoring prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace
```

### 2. Deploy Application
```bash
# Apply manifests
kubectl apply -f k8s-manifest/

# Access services
kubectl port-forward svc/argocd-server -n argocd 8080:443 &
kubectl port-forward svc/monitoring-grafana -n monitoring 3000:80 &
kubectl port-forward svc/todo-api 8000:80 &
```

### 3. Access UIs
- **Application**: http://localhost:8000
- **ArgoCD**: https://localhost:8080 (admin/[get-password])
- **Grafana**: http://localhost:3000 (admin/prom-operator)

## 📈 Demo Workflow

### 1. Make Code Change
```bash
# Edit application code
vim todo-api/main.py

# Commit and push
git add .
git commit -m "Update application"
git push origin main
```

### 2. Watch Pipeline Execute
1. **GitHub Actions**: Builds and tests automatically
2. **Container Registry**: New image tagged and pushed  
3. **ArgoCD**: Detects changes and syncs deployment
4. **Kubernetes**: Rolling update with zero downtime

### 3. Verify Deployment
```bash
# Test API
curl http://localhost:8000

# Generate traffic for metrics
for i in {1..100}; do curl http://localhost:8000; done

# View metrics
curl http://localhost:8000/metrics
```

## 🎯 Key Metrics & Monitoring

### Application Metrics
- `hits_total`: Total API requests
- `http_request_duration_seconds`: Response times
- `container_cpu_usage_seconds_total`: CPU utilization
- `container_memory_usage_bytes`: Memory consumption

### GitOps Metrics
- Deployment frequency
- Lead time for changes  
- Mean time to recovery
- Change failure rate

## 🔧 Configuration Files

```
CICDpipeline/
├── .github/workflows/deploy.yml     # CI/CD pipeline
├── todo-api/
│   ├── main.py                      # FastAPI application
│   ├── test_main.py                 # Automated tests
│   ├── Dockerfile                   # Container build
│   └── requirements.txt             # Dependencies
├── k8s-manifest/
│   ├── deployment.yaml              # K8s deployment
│   ├── service.yaml                 # K8s service
│   ├── servicemonitor.yaml          # Prometheus config
│   └── argocd-app.yaml              # ArgoCD application
└── README.md                        # This file
```

## 🎤 Interview Talking Points

### Technical Depth
- "Implemented GitOps principles with ArgoCD for declarative deployments"
- "Designed automated testing gates to prevent broken deployments" 
- "Built observability into the application with Prometheus metrics"
- "Configured zero-downtime rolling deployments with Kubernetes"

### Production Considerations
- "This pattern scales to hundreds of microservices in production"
- "Implemented proper RBAC and security scanning in real environments"
- "Added monitoring and alerting for SRE practices and SLA management"
- "Used infrastructure as code for repeatable, auditable deployments"

### Problem Solving
- "Debugged DNS resolution issues in the local Kind cluster"
- "Configured branch-specific workflows for different environments"
- "Implemented proper testing strategies to catch regressions early"
- "Designed rollback strategies for rapid incident recovery"

## 🏆 Production Enhancements

For production use, consider adding:
- **Security**: RBAC, Pod Security Standards, image scanning
- **Scalability**: HPA, VPA, resource limits and requests
- **Reliability**: Health checks, circuit breakers, retry logic
- **Observability**: Distributed tracing, log aggregation, SLI/SLO monitoring
- **Compliance**: Policy enforcement, audit logging, secret management

## 📚 Additional Resources

- [GitOps Principles](https://opengitops.dev/)
- [ArgoCD Documentation](https://argo-cd.readthedocs.io/)
- [Prometheus Best Practices](https://prometheus.io/docs/practices/)
- [Kubernetes Production Readiness](https://kubernetes.io/docs/concepts/)

---

**Built with ❤️ for demonstrating modern DevOps practices**