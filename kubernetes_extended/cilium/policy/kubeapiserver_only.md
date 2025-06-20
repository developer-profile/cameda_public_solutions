# Политика, разрешающая взаимодействие только с API Server.
```
cat <<EOF | kubectl apply -f -
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "rule1"
spec:
  description: "test-api"
  endpointSelector:
    matchLabels:
      org: empire
      class: deathstar
  ingress:
    - fromEntities:
      - kube-apiserver
  egress:
    - toEntities:
      - kube-apiserver
EOF
```

## Тестируем.
```
kubectl exec -ti deathstar-995dc966-gpwjl -- curl -X GET https://10.1.2.31/api/v1/namespaces/default/pods \
  -H "Authorization: Bearer $(yc iam create-token)" \
  -H "Accept: application/json" --insecure
```
