# Сервис с дефолтным типом - ClusterIP. Обрабатывает трафик с двух портов.

## Следит за подами с меткой app: nginx.
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  namespace: default
  name: nginx-svc-clusterip
  labels:
    environment: test
  annotations:
    author: cameda
spec:
  type: ClusterIP
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

## Пример с подом.
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: cam-pod-nginx
  namespace: default
  labels:
    cam: nginx
    environment: test
  annotations:
    author: cameda
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    imagePullPolicy: IfNotPresent
    resources:
      requests:
        cpu: "20m"
        memory: "20Mi"
      limits:
        memory: "50Mi"
    ports:
    - containerPort: 80
  restartPolicy: OnFailure
  hostname: nginx
  nodeSelector:
    kubernetes.io/os: linux
---
apiVersion: v1
kind: Service
metadata:
  namespace: default
  name: nginx-svc-clusterip
  labels:
    environment: test
  annotations:
    author: cameda
spec:
  type: ClusterIP
  selector:
    cam: nginx
  ports:
  - name: http
    protocol: TCP
    port: 80
EOF
```
