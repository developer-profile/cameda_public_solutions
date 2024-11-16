# Kubernetes-dashboard ingress

## Установка.
```
helm repo add jetstack https://charts.jetstack.io --force-update

helm upgrade --install cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.15.2 \
  --set crds.enabled=true

helm upgrade --install ingress-nginx ingress-nginx \
--repo https://kubernetes.github.io/ingress-nginx \
--namespace ingress-nginx --create-namespace \
--debug \
--set controller.service.loadBalancerIP=<YOUR_STATIC_IP> \
--set controller.ingressClass="nginx"
```

## Рабочий пример.

### Выпускаем сертификат.
```
cat <<EOF | kubectl apply -f -
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt
  namespace: cert-manager
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: cameda4@yandex.ru
    privateKeySecretRef:
      name: kubernetes-dashboard
    solvers:
    - http01:
        ingress:
          class: nginx
EOF
```
### Создаём ingress правило.
```
cat <<EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: kubernetes-dashboard
  namespace: kubernetes-dashboard
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt"
    nginx.ingress.kubernetes.io/backend-protocol: "HTTPS"
    nginx.ingress.kubernetes.io/auth-tls-verify-client: "false"
spec:
  ingressClassName: nginx
  tls:
    - hosts:
      - dashboard.cameda1.ru
      secretName: kubernetes-dashboard
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
