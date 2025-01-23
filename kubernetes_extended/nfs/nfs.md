# NFS pv for k8s

## Описание.
Подключим хранилище на базе NFS к поду.

## Подготовка.
Создадим NFS сервер по мануалу: https://github.com/Cameda/public_solutions/blob/main/YandexCloud/manifests/compute/vm/04.nfs_server.md

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
    server: 10.142.0.13
EOF
```
где 10.142.0.13 - внутренний адрес NFS сервера.

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
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cam-nginx-nfs
  namespace: default
  labels:
    env: test
spec:
  replicas: 1
  selector:
    matchLabels:
      app: cam-nginx-nfs
  template:
    metadata:
      labels:
        app: cam-nginx-nfs
    spec:
      containers:
      - name: nginx-nfs-test
        image: nginx:1.24
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 80
        command: ["mkdir -p /tmp/nfs"]
        resources:
          requests:
            cpu: 200m
            memory: 150Mi
        volumeMounts:
        - name: my-nfs-share
          mountPath: /tmp/nfs
      restartPolicy: Always
      hostname: nginx-nfs
      nodeSelector:
        kubernetes.io/os: linux
      volumes:
      - name: my-nfs-share
        persistentVolumeClaim:
          claimName: cam-nfs-pvc
```
