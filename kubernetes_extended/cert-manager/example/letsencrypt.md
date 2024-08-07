# Запрос сертификата от Let's Encrypt

## Описание.
Создадим Issuer Let's Encrypt и сделаем запрос на сертификат, который подпишем с помощью Issuer.
Запрос будем делать на боевой сервер. Он используется для отработки запроса.

Здесь отмечу, что у LE есть строгие лимиты на количество запросов к ACME серверам.
https://letsencrypt.org/docs/rate-limits/

## Поехали!

### Создадим ClusterIssuer.
```
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: ya-issuer
  namespace: default
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: cameda@yandex.ru
    privateKeySecretRef:
      name: cat.cameda1-secret
    solvers:
    - http01:
        ingress:
          ingressClassName: nginx
---
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: cat-cameda1
  namespace: default
spec:
  secretName: tls-secret
  issuerRef:
    name: ya-issuer
    kind: ClusterIssuer
  commonName: cat.cameda1.ru
  dnsNames:
  - cat.cameda1.ru
```

### Далее создадим Deployment, Service, Ingress.
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cam-deploy-test-one
  namespace: default
  labels:
    app: app-nginx
    env: test
  annotations:
    author: cameda
spec:
  replicas: 1
  selector:
    matchLabels:
      app: app-nginx
  template:
    metadata:
      labels:
        app: app-nginx
    spec:
      containers:
      - name: cam-nginx1
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
apiVersion: v1
kind: Service
metadata:
  name: cam-svc-test-one
  namespace: default
  labels:
    service: test
    env: test
  annotations:
    author: cameda
spec:
  type: ClusterIP
  selector:
    app: app-nginx
  ports:
  - name: http
    port: 80
    targetPort: 80
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-with-one-backend-test
  namespace: default
  labels:
    ingress: test
    env: test
  annotations:
    author: cameda
spec:
  ingressClassName: nginx
  tls:
    - hosts:
      - cat.cameda1.ru
      secretName: tls-secret
  rules:
    - host: cat.cameda1.ru
      http:
        paths:
        - path: /
          pathType: Prefix
          backend:
            service:
              name: cam-svc-test-one
              port:
                number: 80
```
