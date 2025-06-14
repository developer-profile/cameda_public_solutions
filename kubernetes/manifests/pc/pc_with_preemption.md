# PriorityClass

## Описание.
Создаём приоритет чуть выше дефолтного. Который равен нулю. 
Поды с меньшим приоритетом будут принудительно выселяться. 
```
cat <<EOF | kubectl apply -f -
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: cam-pc
  namespace: default
  labels:
    pc: main
  annotations:
    author: cameda
value: 200
globalDefault: false
description: "PC with preemption"
EOF
```

## Пример с подом.
```
cat <<EOF | kubectl apply -f -
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: cam-pc
  namespace: default
  labels:
    pc: main
  annotations:
    author: cameda
value: 200
globalDefault: false
description: "PC with preemption"
---
apiVersion: v1
kind: Pod
metadata:
  name: cam-nginx
  namespace: default
  labels:
    app: nginx
    env: prod
  annotations:
    author: cameda
spec:
  containers:
  - name: cam-nginx
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
    - containerPort: 443
    livenessProbe:
      failureThreshold: 10
      successThreshold: 1
      httpGet:
        path: /
        port: 80
      periodSeconds: 10
      timeoutSeconds: 1
      initialDelaySeconds: 5
  restartPolicy: Always
  hostname: nginx
  nodeSelector:
    kubernetes.io/os: linux
  priorityClassName: cam-pc
EOF
```
