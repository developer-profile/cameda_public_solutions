# Открыть весь IPv4 трафик
```
cat <<EOF | kubectl apply -f -
apiVersion: cilium.io/v2
kind: CiliumNetworkPolicy
metadata:
  name: allow-all-ipv4
spec:
  endpointSelector: {}  # Применяется ко всем подам
  ingress:
    - fromEndpoints:
        - {}  # Разрешает трафик от всех Pod'ов
    - fromCIDR:
        - 0.0.0.0/0  # Разрешает трафик из любого IPv4-адреса
  egress:
    - toEndpoints:
        - {}  # Разрешает трафик ко всем Pod'ам
    - toCIDR:
        - 0.0.0.0/0  # Разрешает трафик в любой IPv4-адрес
EOF
```
