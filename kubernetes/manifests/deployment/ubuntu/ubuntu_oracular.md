# Deployment with Ubuntu 24.10
```
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cam-deploy-ubuntu-oracular
  namespace: default
  labels:
    app: ubuntu-oracular
    environment: test
  annotations:
    author: cameda
spec:
  replicas: 1
  selector:
    matchLabels:
      app: cam-deploy-ubuntu-oracular
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
    type: RollingUpdate
  template:
    metadata:
      labels:
        app: cam-deploy-ubuntu-oracular
    spec:
      containers:
      - name: noble
        image: ubuntu:24.10
        imagePullPolicy: IfNotPresent
        command: ["bash", "-c"]
        args: ["apt update && apt -y install vim htop traceroute dstat git dnsutils && sleep infinity"]
        resources:
          requests:
            cpu: 200m
            memory: 200Mi
          limits:
            memory: 300Mi
      restartPolicy: Always
      hostname: oracular
      nodeSelector:
        kubernetes.io/os: linux
EOF
```
