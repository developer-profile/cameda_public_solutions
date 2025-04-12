# Deployment with Ubuntu 25.04
```
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cam-deploy-ubuntu-plucky
  namespace: default
  labels:
    app: ubuntu-plucky
    environment: test
  annotations:
    author: cameda
spec:
  replicas: 1
  selector:
    matchLabels:
      app: cam-deploy-ubuntu-plucky
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
    type: RollingUpdate
  template:
    metadata:
      labels:
        app: cam-deploy-ubuntu-plucky
    spec:
      containers:
      - name: noble
        image: ubuntu:25.04
        imagePullPolicy: IfNotPresent
        command: ["bash", "-c"]
        args: ["apt update && apt -y install vim htop traceroute inetutils-ping git dnsutils && sleep infinity"]
        resources:
          requests:
            cpu: 200m
            memory: 200Mi
          limits:
            memory: 300Mi
      restartPolicy: Always
      hostname: plucky
      nodeSelector:
        kubernetes.io/os: linux
EOF
```
