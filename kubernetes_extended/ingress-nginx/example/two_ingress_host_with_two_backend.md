# Пример одного Ingress с двумя бакендами.

## Deployment.
```
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cam-deploy1-test-two
  namespace: default
  labels:
    app: app-nginx12
    env: test
  annotations:
    author: cameda
spec:
  replicas: 1
  selector:
    matchLabels:
      app: app-nginx12
  template:
    metadata:
      labels:
        app: app-nginx12
    spec:
      containers:
      - name: cam-nginx12
        image: nginx:alpine
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 80
        resources:
          requests:
            cpu: 50m
            memory: 50M
          limits:
            memory: 120M
      restartPolicy: Always
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cam-deploy2-test-two
  namespace: default
  labels:
    app: app-nginx22
    env: test
  annotations:
    author: cameda
spec:
  replicas: 1
  selector:
    matchLabels:
      app: app-nginx22
  template:
    metadata:
      labels:
        app: app-nginx22
    spec:
      containers:
      - name: cam-nginx22
        image: nginx:alpine
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 80
        resources:
          requests:
            cpu: 50m
            memory: 50M
          limits:
            memory: 120M
      restartPolicy: Always
EOF
```

## Service.
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  name: cam-svc1-test-two
  namespace: default
  labels:
    service: test
    env: test
  annotations:
    author: cameda
spec:
  type: ClusterIP
  selector:
    app: app-nginx12
  ports:
  - name: http
    port: 80
    targetPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: cam-svc2-test-two
  namespace: default
  labels:
    service: test
    env: test
  annotations:
    author: cameda
spec:
  type: ClusterIP
  selector:
    app: app-nginx22
  ports:
  - name: http
    port: 80
    targetPort: 80
EOF
```

## Ingress.
```
cat <<EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-with-two-backend-test
  namespace: default
  labels:
    ingress: test
    env: test
  annotations:
    author: cameda
spec:
  ingressClassName: nginx
  rules:
    - host: dog.cameda1.ru
      http:
        paths:
        - path: /
          pathType: Prefix
          backend:
            service:
              name: cam-svc1-test-two
              port:
                number: 80
    - host: rat.cameda1.ru
      http:
        paths:
        - path: /
          pathType: Prefix
          backend:
            service:
              name: cam-svc2-test-two
              port:
                number: 80
EOF
```
