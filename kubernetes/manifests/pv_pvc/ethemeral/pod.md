# Пример пода с эфемерным хранилищем

```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: new-pod-with-ethemeral
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
      ephemeral:
        volumeClaimTemplate:
          spec:
            accessModes:
            - ReadWriteOncePod
            resources:
              requests:
                storage: 50Gi
            storageClassName: yc-network-ssd
            volumeMode: Filesystem
EOF
```
