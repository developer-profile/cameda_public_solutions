# Дополнительные примеры.

## Staging vs Production Environments.
```
cat <<EOF | kubectl apply -f -
# For staging
apiVersion: v1
kind: LimitRange
metadata:
  name: staging-limits
  namespace: staging
spec:
  limits:
  - type: Container
    default:
      cpu: "0.5"
      memory: "256Mi"
    max:
      cpu: "1"
      memory: "1Gi"

# For production
apiVersion: v1
kind: LimitRange
metadata:
  name: production-limits
  namespace: production
spec:
  limits:
  - type: Container
    default:
      cpu: "1"
      memory: "512Mi"
    max:
      cpu: "4"
      memory: "8Gi"
EOF
```

## Cost Optimization.
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: LimitRange
metadata:
  name: cost-saving-limits
spec:
  limits:
  - type: Container
    defaultRequest:
      cpu: "100m"  # Start with minimal CPU
      memory: "128Mi"  # Start with minimal memory
    default:
      cpu: "300m"  # Cap at reasonable levels
      memory: "256Mi"
EOF
```
