# Сервис типа NodePort. Следит за подами с меткой app: nginx

## Пример.
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  namespace: default
  name: nginx-svc-with-affinity-nodeport
  labels:
    environment: prod
  annotations:
    author: cameda
spec:
  type: NodePort
  selector:
    cam: nginx
  ports:
  - name: http
    protocol: TCP
    port: 80
    targetPort: 80
    nodePort: 30010
  - name: https
    protocol: TCP
    port: 443
    targetPort: 443
    nodePort: 30011
  externalTrafficPolicy: Local
  sessionAffinity: ClientIP
---
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
    - containerPort: 443
  restartPolicy: OnFailure
  hostname: nginx
  nodeSelector:
    kubernetes.io/os: linux
EOF
```
