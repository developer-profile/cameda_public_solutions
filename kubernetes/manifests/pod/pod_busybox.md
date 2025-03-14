# Pod with busybox alpine
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: cam-pod-busybox
  namespace: default
  labels:
    cam: busybox
  annotations:
    author: cameda
spec:
  containers:
  - name: busybox
    image: busybox:alpine
    imagePullPolicy: IfNotPresent
    resources:
      requests:
        cpu: "20m"
        memory: "20Mi"
      limits:
        memory: "50Mi"
    command: ["sh", "-c"]
    args: ["sleep inherit"]
  restartPolicy: OnFailure
  hostname: busybox
  nodeSelector:
    kubernetes.io/os: linux
EOF
