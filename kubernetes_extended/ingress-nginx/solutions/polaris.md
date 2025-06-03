# Ingress для Polaris

После установки Polaris можно к нему подключаться с помощью port-forward или proxy, а можно создать ingress.
IP адрес привязываем к А записи домена.

## Create ingress for polaris dashboard
```
cat <<EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: polaris
  namespace: polaris
spec:
  ingressClassName: nginx
  rules:
    - host: polaris.cameda1.ru
      http:
        paths:
        - path: /
          pathType: Prefix
          backend:
            service:
              name: polaris-dashboard
              port:
                number: 8080
EOF
```

### Добавим сертификат.
```
cat <<EOF | kubectl apply -f -
apiVersion: cert-manager.io/v1
kind: Issuer
metadata:
  name: polaris-issuer
  namespace: polaris
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: cameda@yandex.ru
    privateKeySecretRef:
      name: polaris
    solvers:
    - http01:
        ingress:
          class: nginx
---
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: polaris
  namespace: polaris
spec:
  secretName: polaris-tls-secret
  issuerRef:
    name: polaris-issuer
    kind: Issuer
  commonName: polaris.cameda1.ru
  dnsNames:
  - polaris.cameda1.ru
EOF
```

### и подключаем сертификат к Ingress.
```
cat <<EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: polaris
  namespace: polaris
  annotations:
    cert-manager.io/issuer: "polaris-issuer"
    nginx.ingress.kubernetes.io/auth-tls-verify-client: "false"
spec:
  ingressClassName: nginx
  tls:
    - hosts:
      - polaris.cameda1.ru
      secretName: polaris-tls-secret
  rules:
    - host: polaris.cameda1.ru
      http:
        paths:
        - path: /
          pathType: Prefix
          backend:
            service:
              name: polaris-dashboard
              port:
                number: 8080
EOF
```
