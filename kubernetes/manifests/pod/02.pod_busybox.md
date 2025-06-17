# Pod with busybox
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
    image: busybox
    imagePullPolicy: IfNotPresent
    resources:
      requests:
        cpu: "100m"
        memory: "100Mi"
      limits:
        memory: "120Mi"
    command: ["sh", "-c"]
    args: ["sleep 3650d"]
  restartPolicy: OnFailure
  hostname: busybox
  nodeSelector:
    kubernetes.io/os: linux
EOF
