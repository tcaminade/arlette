# Mistral Inference Service

This directory contains the Kubernetes manifests required to deploy a local Ollama inference runtime on the k0s cluster.

The service is intended to provide a cluster-native LLM backend for Arlette and related workloads.

The runtime is deployed as a standard Kubernetes workload and exposed through an ingress endpoint.


## Architecture

```
Arlette / Clients
↓
Ingress
↓
Ollama Service
↓
Ollama Deployment
↓
Persistent Model Storage
```

The deployment is intentionally minimal:

single replica
persistent model cache
OpenEBS-backed storage
ingress exposure
no authentication layer yet

## Directory Structure

```
services/mistral/
├── deployment.yaml
├── ingress.yaml
├── kustomization.yaml
├── namespace.yaml
├── pvc.yaml
├── README.md
└── service.yaml
```

## Components
### Namespace

The runtime is deployed inside the dedicated namespace:

```
ai
```

### Persistent Storage

The model cache is stored on a PersistentVolumeClaim backed by OpenEBS LVM.

This ensures:

model persistence across pod restarts
no model re-download
stable runtime lifecycle
### Ollama Deployment

The deployment runs:

Ollama runtime
local Mistral model inference
HTTP API on port 11434

The container stores models in:

```
/root/.ollama
```

### Service Exposure

The runtime is exposed internally through:

```
Service: ollama
Port: 11434
```

### Ingress

The runtime is exposed externally through ingress-nginx using:

```
http://ollama.lab.local
```

DNS resolution must be configured externally.

Example:

```
192.168.1.50 ollama.lab.local
```

### Deployment

Apply manifests using kustomize:

```
kubectl apply -k services/mistral
```

## Validation

Verify runtime resources:

```
kubectl get pods -n ai
kubectl get pvc -n ai
kubectl get ingress -n ai
kubectl get svc -n ai
```

Expected pod state:

```
1/1 Running
```

## Pulling the Model

Connect into the pod:

```
kubectl exec -it -n ai deploy/ollama -- bash
```

Pull the Mistral model:

```
ollama pull mistral
```

The model will be stored persistently in the PVC.

## Testing the Runtime

Port-forward locally:

```
kubectl port-forward -n ai svc/ollama 11434:11434
```

Then test inference:

```
curl http://localhost:11434/api/generate -d '{
"model": "mistral",
"prompt": "hello",
"stream": false
}'
```

Or directly through ingress:

```
curl http://ollama.lab.local/api/generate -d '{
"model": "mistral",
"prompt": "hello",
"stream": false
}'
```

## Current Limitations

This deployment intentionally does not yet include:

authentication
TLS
GPU scheduling
autoscaling
inference batching
rate limiting
observability
model routing
multi-model support

These concerns will be addressed later as part of the platform evolution.

## Design Philosophy

This runtime is considered:

a cluster-native inference backend
external to Arlette itself
replaceable by other inference engines later

Arlette must only depend on:

HTTP inference API
provider abstraction
model capability

The application must never depend directly on:

Ollama internals
local developer machines
specific node implementations

This separation is intentional and foundational to the platform architecture.