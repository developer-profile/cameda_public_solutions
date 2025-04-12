# Deployment with Ubuntu 16.04
```
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cam-deploy-ubuntu-xenial
  namespace: default
  labels:
    app: ubuntu-xenial
    environment: test
  annotations:
    author: cameda
spec:
  replicas: 1
  selector:
    matchLabels:
      app: cam-deploy-ubuntu-xenial
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
    type: RollingUpdate
  template:
    metadata:
      labels:
        app: cam-deploy-ubuntu-xenial
    spec:
      containers:
      - name: xenial
        image: ubuntu:16.04
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
      hostname: xenial
      nodeSelector:
        kubernetes.io/os: linux
EOF
```
