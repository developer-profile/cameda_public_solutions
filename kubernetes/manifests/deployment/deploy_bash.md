# Deployment with Bash
```
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cam-deploy-bash
  namespace: default
  labels:
    app: deploy-bash
    environment: test
  annotations:
    author: cameda
spec:
  replicas: 1
  selector:
    matchLabels:
      app: cam-deploy-bash
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
    type: RollingUpdate
  template:
    metadata:
      labels:
        app: cam-deploy-bash
    spec:
      containers:
      - name: bash
        image: bash
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
      hostname: bash
      nodeSelector:
        kubernetes.io/os: linux
EOF
```
