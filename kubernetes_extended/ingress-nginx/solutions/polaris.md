# Ingress для Polaris

После установки Polaris можно к нему подключаться с помощью port-forward или proxy, а можно создать ingress.

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
