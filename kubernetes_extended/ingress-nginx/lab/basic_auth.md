# Basic auth

## Поехали!

### Создаём секрет.
```
htpasswd -c auth cameda
kubectl create secret generic basic-auth --from-file=auth
```

### Создаём приложение, которое будет защищено паролем из секрета.
```
cat <<EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: cam-ingress-with-basic-auth
  labels:
    ing: test
  annotations:
    nginx.ingress.kubernetes.io/auth-type: basic
    nginx.ingress.kubernetes.io/auth-secret: basic-auth
    nginx.ingress.kubernetes.io/auth-realm: 'Authentication Required - Alex Wolf'
spec:
  ingressClassName: nginx
  rules:
    - host: testdeploy.cameda1.ru
      http:
        paths:
        - path: /
          pathType: Prefix
          backend:
            service:
              name: srv-with-basic-auth
              port:
                number: 80
---
apiVersion: v1
kind: Service
metadata:
  name: srv-with-basic-auth
  labels:
    srv: test
spec:
  selector:
    pod: app
  type: ClusterIP
  ports:
  - port: 80
    name: http
    targetPort: 80
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-deployment-for-basic-auth
  labels:
    deploy: test
spec:
  replicas: 1
  selector:
    matchLabels:
      pod: app
  template:
    metadata:
      labels:
        pod: app
    spec:
      containers:
      - name: app
        image: nginx:alpine
        imagePullPolicy: IfNotPresent
        resources:
          requests:
            cpu: 20m
            memory: 20Mi
          limits:
            memory: 40Mi
        ports:
        - containerPort: 80
EOF
```
