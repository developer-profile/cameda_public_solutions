# Service nodePort

## Описание.
Сервис типа NodePort. Следит за подами с меткой app: nginx

## Примеры.

### Пример с устанавливаемым nodePort.
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  namespace: default
  name: nginx-svc-nodeport-2ports
  labels:
    environment: test
  annotations:
    author: cameda
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
  - name: http
    protocol: TCP
    port: 80
    nodePort: 30012
  - name: https
    protocol: TCP
    port: 443
    nodePort: 30013
EOF
```

### Пример с автоматической подстановкой порта.
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  namespace: default
  name: nginx-svc-nodeport-2ports
  labels:
    environment: test
  annotations:
    author: cameda
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
  - name: http
    protocol: TCP
    port: 80
  - name: https
    protocol: TCP
    port: 443
EOF
```

### Пример с одним портом.
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  namespace: default
  name: nginx-svc-nodeport
  labels:
    environment: test
  annotations:
    author: cameda
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
  - name: http
    protocol: TCP
    port: 80
    nodePort: 31115
EOF
```
