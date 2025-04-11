# Deployment with hello-world
```
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cam-deploy-hello-world
  namespace: default
  labels:
    app: deploy-hello-world
    environment: test
  annotations:
    author: cameda
spec:
  replicas: 1
  selector:
    matchLabels:
      app: cam-deploy-hello-world
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
    type: RollingUpdate
  template:
    metadata:
      labels:
        app: cam-deploy-hello-world
    spec:
      containers:
      - name: cam-deploy-hello-world
        image: hello-world
        imagePullPolicy: IfNotPresent
        resources:
          requests:
            cpu: 50m
            memory: 50Mi
          limits:
            memory: 80Mi
      restartPolicy: Always
      hostname: hello-world
      nodeSelector:
        kubernetes.io/os: linux
EOF
```
