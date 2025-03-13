# Pod with Ubuntu
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: cam-pod-ubuntu
  namespace: default
  labels:
    cam: ubuntu
  annotations:
    author: cameda
spec:
  containers:
  - name: ubuntu
    image: ubuntu
    imagePullPolicy: IfNotPresent
    resources:
      requests:
        cpu: "1"
        memory: "1G"
      limits:
        memory: "2G"
    command: ["sh", "-c"]
    args: ["sleep inherit"]
  restartPolicy: OnFailure
  hostname: ubuntu
  nodeSelector:
    kubernetes.io/os: linux
EOF
```
