# MEZAN ATLAS Helm Chart Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Upgrading](#upgrading)
6. [Rollback](#rollback)
7. [Uninstallation](#uninstallation)
8. [Advanced Usage](#advanced-usage)
9. [Troubleshooting](#troubleshooting)

## Introduction

The MEZAN ATLAS Helm chart provides a production-ready deployment of the multi-agent research orchestration system on Kubernetes. This chart includes:

- MEZAN ATLAS API and Worker deployments
- Redis cluster for caching and message brokering
- PostgreSQL for persistent storage (optional)
- Prometheus and Grafana monitoring stack
- Automatic scaling and high availability
- Security best practices

## Prerequisites

### Required
- Kubernetes 1.28+
- Helm 3.13+
- kubectl configured with cluster access

### Recommended
- cert-manager for automatic TLS certificates
- metrics-server for HPA functionality
- ingress-nginx controller

## Installation

### Quick Start

```bash
# Add the chart repository (if published)
helm repo add mezan-atlas https://charts.mezan-atlas.example.com
helm repo update

# Install with default values
helm install mezan-atlas mezan-atlas/mezan-atlas \
  --namespace mezan-atlas \
  --create-namespace

# Or install from local chart
helm install mezan-atlas ./MEZAN/ATLAS/atlas-core/helm \
  --namespace mezan-atlas \
  --create-namespace
```

### Production Installation

```bash
# 1. Create namespace
kubectl create namespace mezan-atlas-production

# 2. Create secrets
kubectl create secret generic mezan-atlas-secrets \
  --from-literal=ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY \
  --from-literal=OPENAI_API_KEY=$OPENAI_API_KEY \
  --from-literal=REDIS_PASSWORD=$(openssl rand -base64 32) \
  --from-literal=JWT_SECRET=$(openssl rand -base64 64) \
  --namespace mezan-atlas-production

# 3. Install with production values
helm install mezan-atlas ./MEZAN/ATLAS/atlas-core/helm \
  --namespace mezan-atlas-production \
  --values ./MEZAN/ATLAS/atlas-core/helm/values-prod.yaml \
  --set secrets.existingSecret=mezan-atlas-secrets \
  --wait --timeout 10m
```

## Configuration

### Key Configuration Options

| Parameter | Description | Default |
|-----------|-------------|---------|
| `image.repository` | Docker image repository | `mezan-atlas` |
| `image.tag` | Docker image tag | `3.5.0` |
| `api.replicaCount` | Number of API replicas | `3` |
| `api.resources.limits.memory` | API memory limit | `4Gi` |
| `worker.enabled` | Enable worker deployment | `true` |
| `worker.replicaCount` | Number of worker replicas | `2` |
| `redis.enabled` | Deploy Redis cluster | `true` |
| `postgresql.enabled` | Deploy PostgreSQL | `false` |
| `ingress.enabled` | Enable ingress | `true` |
| `ingress.hosts[0].host` | Ingress hostname | `mezan-atlas.example.com` |
| `monitoring.prometheus.enabled` | Enable Prometheus | `true` |
| `monitoring.grafana.enabled` | Enable Grafana | `true` |

### Custom Values File

Create a custom `values.yaml`:

```yaml
# my-values.yaml
image:
  repository: my-registry.example.com/mezan-atlas
  tag: custom-3.5.0

api:
  replicaCount: 5
  resources:
    requests:
      cpu: 1000m
      memory: 2Gi
    limits:
      cpu: 4000m
      memory: 8Gi

ingress:
  enabled: true
  className: nginx
  hosts:
    - host: api.my-domain.com
      paths:
        - path: /
          pathType: Prefix
  tls:
    - secretName: api-tls
      hosts:
        - api.my-domain.com

redis:
  auth:
    password: "my-secure-password"
```

Install with custom values:

```bash
helm install mezan-atlas ./helm \
  --values my-values.yaml
```

### Using --set for Overrides

```bash
helm install mezan-atlas ./helm \
  --set image.tag=3.5.1 \
  --set api.replicaCount=5 \
  --set ingress.hosts[0].host=api.example.com
```

## Upgrading

### Standard Upgrade

```bash
# Upgrade to new chart version
helm upgrade mezan-atlas ./helm \
  --namespace mezan-atlas \
  --values values-prod.yaml

# Upgrade with new image
helm upgrade mezan-atlas ./helm \
  --set image.tag=3.6.0 \
  --reuse-values
```

### Safe Production Upgrade

```bash
# 1. Diff changes
helm diff upgrade mezan-atlas ./helm \
  --namespace mezan-atlas-production \
  --values values-prod.yaml

# 2. Dry run
helm upgrade mezan-atlas ./helm \
  --namespace mezan-atlas-production \
  --values values-prod.yaml \
  --dry-run --debug

# 3. Upgrade with automatic rollback
helm upgrade mezan-atlas ./helm \
  --namespace mezan-atlas-production \
  --values values-prod.yaml \
  --atomic \
  --cleanup-on-fail \
  --timeout 10m

# 4. Verify
helm test mezan-atlas -n mezan-atlas-production
```

## Rollback

### Rollback to Previous Version

```bash
# View history
helm history mezan-atlas -n mezan-atlas

# Rollback to previous release
helm rollback mezan-atlas -n mezan-atlas

# Rollback to specific revision
helm rollback mezan-atlas 3 -n mezan-atlas
```

### Emergency Rollback

```bash
# Force rollback with cleanup
helm rollback mezan-atlas 0 \
  --force \
  --cleanup-on-fail \
  -n mezan-atlas
```

## Uninstallation

```bash
# Standard uninstall
helm uninstall mezan-atlas -n mezan-atlas

# Keep history for rollback
helm uninstall mezan-atlas -n mezan-atlas --keep-history

# Complete cleanup
helm uninstall mezan-atlas -n mezan-atlas
kubectl delete namespace mezan-atlas
```

## Advanced Usage

### Multi-Environment Deployment

```bash
# Development
helm install mezan-dev ./helm \
  --namespace dev \
  --values values-dev.yaml \
  --set environment=development

# Staging
helm install mezan-staging ./helm \
  --namespace staging \
  --values values-staging.yaml \
  --set environment=staging

# Production
helm install mezan-prod ./helm \
  --namespace prod \
  --values values-prod.yaml \
  --set environment=production
```

### Using Helm Hooks

```yaml
# Pre-install database migration
apiVersion: batch/v1
kind: Job
metadata:
  name: "{{ .Release.Name }}-db-migrate"
  annotations:
    "helm.sh/hook": pre-install,pre-upgrade
    "helm.sh/hook-weight": "-5"
    "helm.sh/hook-delete-policy": before-hook-creation
spec:
  template:
    spec:
      restartPolicy: Never
      containers:
      - name: db-migrate
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
        command: ["python", "-m", "atlas.migrate"]
```

### Helm Secrets Management

```bash
# Using helm-secrets plugin
helm plugin install https://github.com/jkroepke/helm-secrets

# Encrypt values
helm secrets enc values-prod.yaml

# Install with encrypted values
helm secrets install mezan-atlas ./helm \
  -f values-prod.yaml.enc
```

### GitOps with ArgoCD

```yaml
# argocd-app.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: mezan-atlas
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/AlaweinOS/MEZAN
    targetRevision: main
    path: MEZAN/ATLAS/atlas-core/helm
    helm:
      valueFiles:
        - values-prod.yaml
  destination:
    server: https://kubernetes.default.svc
    namespace: mezan-atlas-production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

### Custom Resource Definitions

```bash
# Install CRDs separately
kubectl apply -f crds/

# Install chart without CRDs
helm install mezan-atlas ./helm \
  --skip-crds
```

## Troubleshooting

### Common Issues

#### 1. Installation Failures

```bash
# Check helm release status
helm status mezan-atlas -n mezan-atlas

# View installation notes
helm get notes mezan-atlas -n mezan-atlas

# Check generated manifests
helm get manifest mezan-atlas -n mezan-atlas
```

#### 2. Values Not Applied

```bash
# Verify computed values
helm get values mezan-atlas -n mezan-atlas

# Show all values (including defaults)
helm get values mezan-atlas -n mezan-atlas --all

# Debug template rendering
helm template mezan-atlas ./helm \
  --values values-prod.yaml \
  --debug > rendered.yaml
```

#### 3. Dependency Issues

```bash
# Update dependencies
helm dependency update ./helm

# List dependencies
helm dependency list ./helm

# Build dependencies
helm dependency build ./helm
```

#### 4. Hook Failures

```bash
# List hooks
helm get hooks mezan-atlas -n mezan-atlas

# Delete failed hook resources
kubectl delete job -l "helm.sh/hook" -n mezan-atlas
```

### Debugging Templates

```bash
# Lint chart
helm lint ./helm

# Render specific template
helm template mezan-atlas ./helm \
  --show-only templates/deployment.yaml

# Test template functions
helm template mezan-atlas ./helm \
  --set debug=true
```

### Performance Issues

```bash
# Check resource usage
kubectl top pods -n mezan-atlas

# Increase resources
helm upgrade mezan-atlas ./helm \
  --set api.resources.requests.memory=2Gi \
  --set api.resources.limits.memory=8Gi
```

## Chart Development

### Structure

```
helm/
├── Chart.yaml           # Chart metadata
├── values.yaml          # Default values
├── values-prod.yaml     # Production values
├── templates/           # Kubernetes templates
│   ├── _helpers.tpl     # Template helpers
│   ├── deployment.yaml  # Deployments
│   ├── service.yaml     # Services
│   ├── ingress.yaml     # Ingress
│   └── NOTES.txt        # Installation notes
├── charts/              # Dependencies
└── crds/                # Custom Resource Definitions
```

### Testing

```bash
# Run helm tests
helm test mezan-atlas -n mezan-atlas

# Unit test templates
helm unittest ./helm

# Integration test
helm install test-release ./helm \
  --namespace test \
  --wait \
  --timeout 5m
```

### Publishing

```bash
# Package chart
helm package ./helm

# Create index
helm repo index . --url https://charts.example.com

# Push to registry
helm push mezan-atlas-3.5.0.tgz oci://registry.example.com/charts
```

## Best Practices

1. **Version Pinning**: Always specify exact versions in production
2. **Resource Limits**: Set appropriate resource requests and limits
3. **Security**: Use secrets management, RBAC, and network policies
4. **Monitoring**: Enable Prometheus and Grafana
5. **Backup**: Configure regular backups
6. **Documentation**: Keep values files well-documented
7. **Testing**: Test upgrades in staging first
8. **GitOps**: Use ArgoCD or Flux for declarative deployments

## Examples

### Complete Production Setup

```bash
#!/bin/bash
# production-deploy.sh

NAMESPACE="mezan-atlas-production"
RELEASE="mezan-atlas"

# Create namespace
kubectl create namespace $NAMESPACE

# Create secrets from environment
kubectl create secret generic mezan-atlas-secrets \
  --from-env-file=.env.production \
  --namespace $NAMESPACE

# Add helm repo
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

# Install with production configuration
helm upgrade --install $RELEASE ./helm \
  --namespace $NAMESPACE \
  --values values-prod.yaml \
  --set-string image.tag="$(git rev-parse --short HEAD)" \
  --set-string secrets.existingSecret=mezan-atlas-secrets \
  --atomic \
  --cleanup-on-fail \
  --create-namespace \
  --timeout 15m \
  --wait

# Verify deployment
helm test $RELEASE -n $NAMESPACE
kubectl get pods -n $NAMESPACE
```

## Support

- Documentation: https://docs.mezan-atlas.example.com
- GitHub Issues: https://github.com/AlaweinOS/MEZAN/issues
- Email: meshal@berkeley.edu