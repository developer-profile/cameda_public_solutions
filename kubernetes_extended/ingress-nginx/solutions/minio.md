# MinIO ingress

## MinIO ingress.
```
cat <<EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: minio
  namespace: minio-dev
spec:
  ingressClassName: nginx
  rules:
    - host: minio.cameda1.ru
      http:
        paths:
        - path: /
          pathType: Prefix
          backend:
            service:
              name: minio
              port:
                number: 9090
EOF
```
Связываем ip адрес балансировщика с А записью домена.

## Подключаем SSL сертификат от Let's Encrypt.
Предполагаю, что Cert Manager уже установлен. 
Если не установлен, то ставим: https://github.com/Cameda/public_solutions/blob/main/kubernetes_extended/cert-manager/helm.md
```
cat <<EOF | kubectl apply -f -
apiVersion: cert-manager.io/v1
kind: Issuer
metadata:
  name: minio
  namespace: minio-dev
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: cameda@yandex.ru
    privateKeySecretRef:
      name: minio
    solvers:
    - http01:
        ingress:
          class: nginx
---
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: minio
  namespace: minio-dev
spec:
  secretName: minio-tls-secret
  issuerRef:
    name: minio
    kind: Issuer
  commonName: minio.cameda1.ru
  dnsNames:
  - minio.cameda1.ru
EOF
```
### Получается так.
```
kubectl get cert -n minio-dev
NAME    READY   SECRET             AGE
minio   True    minio-tls-secret   117s
```

## Ingress with cert.
```
cat <<EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: minio
  namespace: minio-dev
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod-minio"
    nginx.ingress.kubernetes.io/auth-tls-verify-client: "false"
spec:
  ingressClassName: nginx
  tls:
    - hosts:
      - minio.cameda1.ru
      secretName: minio-tls-secret
  rules:
    - host: minio.cameda1.ru
      http:
        paths:
        - path: /
          pathType: Prefix
          backend:
            service:
              name: minio
              port:
                number: 9090
EOF
```
