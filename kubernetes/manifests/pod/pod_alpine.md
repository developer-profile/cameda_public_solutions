# Pod with Alpine
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: cam-pod-alpine
  namespace: default
  labels:
    cam: alpine
  annotations:
    author: cameda
spec:
  containers:
  - name: alpine
    image: alpine
    imagePullPolicy: IfNotPresent
    command:
      - sh
      - -c
      - |
        sleep infinity
    resources:
      requests:
        cpu: "20m"
        memory: "20Mi"
      limits:
        memory: "140Mi"
  restartPolicy: OnFailure
  hostname: ubuntu
  nodeSelector:
    kubernetes.io/os: linux
EOF
```
