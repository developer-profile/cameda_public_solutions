# Pod with network-utils
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: cam-pod-net-test
  namespace: default
  labels:
    cam: fortest
  annotations:
    author: cameda
spec:
  containers:
  - name: cam-net-test
    image: amouat/network-utils
    imagePullPolicy: IfNotPresent
    resources:
      requests:
        cpu: "50m"
        memory: "50Mi"
      limits:
        memory: "100Mi"
    command: ["sh", "-c"]
    args: ["sleep 3650d"]
  restartPolicy: OnFailure
  hostname: nettest
  nodeSelector:
    kubernetes.io/os: linux
EOF
```
