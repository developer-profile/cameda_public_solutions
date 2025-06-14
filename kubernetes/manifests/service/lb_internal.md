# Load Balancer internal

## Описание.
Внутренний балансировщик. Для работы нужно указать подсеть из которой будет выдаваться адрес.
Обрабатывает трафик с нескольких портов.
Следит за подами с меткой app: nginx

## Примеры.

### Пример с двумя портами.
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  namespace: default
  name: nginx-svc-lb-internal
  annotations:
    # Тип балансировщика: внутренний.
    yandex.cloud/load-balancer-type: internal
    yandex.cloud/subnet-id: <subnet-id>
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

### Пример с одним портом.
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  namespace: default
  name: nginx-svc-lb-internal
  annotations:
    # Тип балансировщика: внутренний.
    yandex.cloud/load-balancer-type: internal
    yandex.cloud/subnet-id: <subnet-id>
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
