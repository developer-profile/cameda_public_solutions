# Load Balancer maximum

## Описание.
Сервис типа LoadBalancer с политикой Local и включённой привязкой сессий. Следит за двумя портами на таргетах.
Также можно указать зарезервированный ранее IP адрес.
Следит за подами с меткой app: nginx

## Примеры.

### Пример с зарезервированным адресом.
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  namespace: default
  name: nginx-svc-lb-max
  labels:
    environment: test
  annotations:
    author: cameda
spec:
  type: LoadBalancer
  selector:
    app: nginx
  ports:
  - name: http
    protocol: TCP
    port: 80
    targetPort: 80
  - name: https
    protocol: TCP
    port: 443
    targetPort: 443
  externalTrafficPolicy: Local
  loadBalancerIP: <заранее зарезервированный IP-адрес>
  sessionAffinity: ClientIP
EOF
```

### Пример без зарезервированного адреса.
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  namespace: default
  name: nginx-svc-lb-max
  labels:
    environment: test
  annotations:
    author: cameda
spec:
  type: LoadBalancer
  selector:
    app: nginx
  ports:
  - name: http
    protocol: TCP
    port: 80
    targetPort: 80
  - name: https
    protocol: TCP
    port: 443
    targetPort: 443
  externalTrafficPolicy: Local
  sessionAffinity: ClientIP
EOF
```
