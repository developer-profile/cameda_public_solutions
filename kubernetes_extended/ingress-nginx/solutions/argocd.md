# ArgoCD ingress

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

Установка ArgoCD описана тут: https://github.com/Cameda/public_solutions/blob/main/kubernetes_extended/argocd/argocd.md

## Рабочий пример.

### Выпускаем сертификат.
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
      name: argocd
    solvers:
    - http01:
        ingress:
          class: nginx
---
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: cert-main
  namespace: argocd
spec:
  secretName: argocd-tls-secret
  issuerRef:
    name: letsencrypt-prod
    kind: ClusterIssuer
  commonName: argocd.cameda1.ru
  dnsNames:
  - argocd.cameda1.ru
EOF
```

## Создаём ingress правило.
```
cat <<EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: argocd-ingress
  namespace: argocd
  labels:
    ingress: argocd
    env: test
  annotations:
    author: cameda
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
    ingress.kubernetes.io/secure-backends: "true"
    nginx.ingress.kubernetes.io/backend-protocol: "HTTPS"
    nginx.ingress.kubernetes.io/use-proxy-protocol: "true"
    nginx.ingress.kubernetes.io/auth-tls-verify-client: "off"
spec:
  tls:
    - hosts:
      - argocd.cameda1.ru
      secretName: argocd-tls-secret
  ingressClassName: nginx
  rules:
    - host: argocd.cameda1.ru
      http:
        paths:
        - path: /
          pathType: Prefix
          backend:
            service:
              name: argo-cd-argocd-server
              port:
                number: 443
EOF
```
