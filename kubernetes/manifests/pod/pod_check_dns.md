# Pod for check dns
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: check-dns
  namespace: default
  labels:
    env: test
  annotations:
    author: cameda
spec:
  containers:
  - name: check-dns
    image: k8s.gcr.io/jessie-dnsutils
    imagePullPolicy: IfNotPresent
    resources:
      requests:
        cpu: "20m"
        memory: "20Mi"
      limits:
        memory: "50Mi"
    command: ["/bin/sh"]
    args: ["-c", "sleep 1d"]
  restartPolicy: Never
  hostname: check-dns
  nodeSelector:
    kubernetes.io/os: linux
EOF
```
