# Kubernetes-dashboard ingress

## Установка cert-manager.
Если не был установлен ранее.
```
helm repo add jetstack https://charts.jetstack.io --force-update

helm upgrade --install cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.17.0 \
  --set crds.enabled=true
```

## Установка ingress controller.
Если не был установлен ранее.
```
helm upgrade --install ingress-nginx ingress-nginx \
--repo https://kubernetes.github.io/ingress-nginx \
--namespace ingress-nginx --create-namespace \
--debug \
--set controller.service.loadBalancerIP=<YOUR_STATIC_IP> \
--set controller.ingressClass="nginx"
```

Установка дашборда описана тут: 
https://github.com/Cameda/public_solutions/blob/main/kubernetes_extended/kubernetes-dashboard/kubernetes-dashboard.md

## Рабочий пример.

### Создаём ingress правило без сертификата.
```
cat <<EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: kubernetes-dashboard
  namespace: kubernetes-dashboard
spec:
  ingressClassName: nginx
  rules:
    - host: dashboard.cameda1.ru
      http:
        paths:
        - path: /
          pathType: Prefix
          backend:
            service:
              name: kubernetes-dashboard
              port:
                number: 80
EOF
```

### Прописываем А запись для домена.
Например, в CloudDNS.

### Делаем запрос на сертификат.
```
cat <<EOF | kubectl apply -f -
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
  namespace: cert-manager
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: cameda@yandex.ru
    privateKeySecretRef:
      name: kubernetes-dashboard
    solvers:
    - http01:
        ingress:
          class: nginx
---
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: kubernetes-dashboard
  namespace: kubernetes-dashboard
spec:
  secretName: dashboard-tls-secret
  issuerRef:
    name: letsencrypt-prod
    kind: ClusterIssuer
  commonName: dashboard.cameda1.ru
  dnsNames:
  - dashboard.cameda1.ru
EOF
```

#### Получилось так.
```
kubectl get clusterissuer
NAME               READY   AGE
letsencrypt-prod   True    3m9s


kubectl get cert -A
NAMESPACE              NAME                   READY   SECRET                 AGE
kubernetes-dashboard   kubernetes-dashboard   True    dashboard-tls-secret   108s
```

### Создаём ingress правило с сертификатом.
```
cat <<EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: kubernetes-dashboard
  namespace: kubernetes-dashboard
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
    nginx.ingress.kubernetes.io/backend-protocol: "HTTPS"
    nginx.ingress.kubernetes.io/auth-tls-verify-client: "false"
spec:
  ingressClassName: nginx
  tls:
    - hosts:
      - dashboard.cameda1.ru
      secretName: dashboard-tls-secret
  rules:
    - host: dashboard.cameda1.ru
      http:
        paths:
        - path: /
          pathType: Prefix
          backend:
            service:
              name: kubernetes-dashboard
              port:
                number: 443
EOF
```
