# Deployment with Nginx
```
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cam-deploy-nginx
  namespace: default
  labels:
    app: deploy-nginx
    environment: test
  annotations:
    author: cameda
spec:
  replicas: 1
  selector:
    matchLabels:
      app: cam-deploy-nginx
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
    type: RollingUpdate
  template:
    metadata:
      labels:
        app: cam-deploy-nginx
    spec:
      containers:
      - name: cam-deploy-nginx
        image: nginx:alpine
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 80
        resources:
          requests:
            cpu: 20m
            memory: 20Mi
          limits:
            memory: 50Mi
      restartPolicy: Always
      hostname: nginx
      nodeSelector:
        kubernetes.io/os: linux
EOF
```
