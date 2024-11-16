# Kubernetes-dashboard

## Описание.
Простенький, базовый дашборд для работы с Kubernetes. Поддерживается сообществом.

## Установка.
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
```

## Доступ к дашборду.

### Proxy.
```
kubectl proxy

# Адрес странички в интернете.
http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/
```

### Ingress.
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

## Полезные вещи.


## Полезные ссылки.
https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/
