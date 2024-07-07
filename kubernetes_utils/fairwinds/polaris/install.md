# Install polaris with helm

```
helm repo add fairwinds-stable https://charts.fairwinds.com/stable
helm upgrade --install polaris fairwinds-stable/polaris --namespace polaris --create-namespace
kubectl port-forward --namespace polaris svc/polaris-dashboard 8080:80
```

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
