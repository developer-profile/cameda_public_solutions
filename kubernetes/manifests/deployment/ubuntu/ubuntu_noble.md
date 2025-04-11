# Deployment with Ubuntu 24.04
```
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cam-deploy-ubuntu-noble
  namespace: default
  labels:
    app: ubuntu-noble
    environment: test
  annotations:
    author: cameda
spec:
  replicas: 1
  selector:
    matchLabels:
      app: cam-deploy-ubuntu-noble
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
    type: RollingUpdate
  template:
    metadata:
      labels:
        app: cam-deploy-ubuntu-noble
    spec:
      containers:
      - name: noble
        image: ubuntu:24.04
        imagePullPolicy: IfNotPresent
        command: ["bash", "-c"]
        args: ["apt update && apt -y install vim htop traceroute dstat && sleep infinity"]
        resources:
          requests:
            cpu: 900m
            memory: 900Mi
          limits:
            memory: 2Gi
      restartPolicy: Always
      hostname: noble
      nodeSelector:
        kubernetes.io/os: linux
EOF
```
