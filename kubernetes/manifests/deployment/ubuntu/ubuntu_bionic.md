# Deployment with Ubuntu 18.04
```
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cam-deploy-ubuntu-bionic
  namespace: default
  labels:
    app: ubuntu-bionic
    environment: test
  annotations:
    author: cameda
spec:
  replicas: 1
  selector:
    matchLabels:
      app: cam-deploy-ubuntu-bionic
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
    type: RollingUpdate
  template:
    metadata:
      labels:
        app: cam-deploy-ubuntu-bionic
    spec:
      containers:
      - name: bionic
        image: ubuntu:18.04
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
      hostname: bionic
      nodeSelector:
        kubernetes.io/os: linux
EOF
```
