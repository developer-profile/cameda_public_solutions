# Load Balancer 

## Описание.
Сервис типа LoadBalancer с одним открытым портом в таргете. Осуществляет слежение за подами с меткой app: nginx

## Примеры.

### Пример с одним портом.
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  namespace: default
  name: nginx-svc-lb-default
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
EOF
```

### Пример с двумя портами.
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  namespace: default
  name: nginx-svc-lb-default
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
EOF
```
