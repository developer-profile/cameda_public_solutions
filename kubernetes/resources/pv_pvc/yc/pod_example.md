# Пример пода

```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: new-pod
spec:
  containers:
  - name: new-container
    image: cr.yandex/crp59ldu2qv9q43uq5jh/debian:latest
    imagePullPolicy: IfNotPresent
    volumeMounts:
    - mountPath: "/User/worker/data"
      name: my-csi
  volumes:
  - name: my-csi
    persistentVolumeClaim:
      claimName: pvc-dynamic-ssd
EOF
```
