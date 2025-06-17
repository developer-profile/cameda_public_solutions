# Deployment with busybox
```
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cam-deploy-busybox
  namespace: default
  labels:
    app: deploy-busybox
    environment: test
  annotations:
    author: cameda
spec:
  replicas: 1
  selector:
    matchLabels:
      app: cam-deploy-busybox
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
    type: RollingUpdate
  template:
    metadata:
      labels:
        app: cam-deploy-busybox
    spec:
      containers:
      - name: cam-deploy-busybox
        image: busybox
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
      hostname: busybox
      nodeSelector:
        kubernetes.io/os: linux
EOF
```
