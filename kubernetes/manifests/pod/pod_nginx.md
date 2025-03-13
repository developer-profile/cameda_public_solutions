# Pod with nginx alpine
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: cam-pod-nginx
  namespace: default
  labels:
    cam: nginx
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
EOF
```
