# Deployment with kubectl

## SA, ClusterRole, ClusterRoleBinding.
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: ServiceAccount
metadata:
  annotations:
    kubernetes.io/enforce-mountable-secrets: "true"
  name: kubectl-access
  namespace: default
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: kubectl-access
  namespace: default
rules:
- apiGroups: ["*"]
  resources: ["*"]
  verbs:
  - create
  - get
  - list
  - watch
  - update
  - patch
  - delete
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: kubectl-access
  namespace: default
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: kubectl-access
subjects:
- kind: ServiceAccount
  name: kubectl-access
  namespace: default
EOF
```

## Deployment.
```
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cam-deploy-kubectl
  namespace: default
  labels:
    app: deploy-kubectl
    environment: test
  annotations:
    author: cameda
spec:
  replicas: 1
  selector:
    matchLabels:
      app: cam-deploy-kubectl
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
    type: RollingUpdate
  template:
    metadata:
      labels:
        app: cam-deploy-kubectl
    spec:
      containers:
      - name: cam-deploy-kubectl
        image: bitnami/kubectl
        imagePullPolicy: IfNotPresent
        command: ["sh", "-c"]
        args: ["sleep infinity"]
        resources:
          requests:
            cpu: 50m
            memory: 50Mi
          limits:
            memory: 80Mi
      restartPolicy: Always
      hostname: kubectl
      serviceAccountName: kubectl-access
      nodeSelector:
        kubernetes.io/os: linux
EOF
```
