# NFS pv for k8s

## Описание.
Подключим хранилище на базе NFS к поду.

## Подготовка.
Создадим NFS сервер по мануалу: https://github.com/Cameda/public_solutions/blob/main/YandexCloud/manifests/compute/vm/04.nfs_server_with_fip.md

## Поехали!

### Создаём PV and PVC.
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: PersistentVolume
metadata:
  name: cam-nfs-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  nfs:
    path: /mnt/data
    server: 158.160.159.135
EOF
```
где 158.160.159.135 - внешний адрес NFS сервера.

```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: cam-nfs-pvc
  namespace: default
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
  storageClassName: ""
  volumeName: cam-nfs-pv
EOF
```

### Создаём Deployment и подключаем PVC.
```
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cam-busybox-nfs
  namespace: default
  labels:
    env: test
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nfs
  template:
    metadata:
      labels:
        app: nfs
    spec:
      containers:
      - name: nfs-test
        image: busybox
        imagePullPolicy: IfNotPresent
        command: ["sh", "-c"]
        args: ["sleep 24h"]
        resources:
          requests:
            cpu: 100m
            memory: 70Mi
        volumeMounts:
        - name: my-nfs-share
          mountPath: /tmp
      restartPolicy: Always
      hostname: nfs
      nodeSelector:
        kubernetes.io/os: linux
      volumes:
      - name: my-nfs-share
        persistentVolumeClaim:
          claimName: cam-nfs-pvc
EOF
```
