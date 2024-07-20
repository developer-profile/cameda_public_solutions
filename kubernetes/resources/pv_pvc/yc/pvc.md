# Yandex Cloud PVC

## yc-network-ssd.
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-dynamic-ssd
  namespace: default
  labels:
    cam: pvc-dynamic-ssd
  annotations:
    author: cameda
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: yc-network-ssd
  resources:
    requests:
      storage: 12Gi
```
----------------------------------------------------------------

## yc-network-hdd.
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-dynamic-hdd
  namespace: default
  labels:
    cam: pvc-dynamic-hdd
  annotations:
    author: cameda
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: yc-network-hdd
  resources:
    requests:
      storage: 12Gi
```
----------------------------------------------------------------

## yc-network-ssd-nonreplicated.
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-dynamic-nrd
  namespace: default
  labels:
    cam: pvc-dynamic-nrd
  annotations:
    author: cameda
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: yc-network-ssd-nonreplicated
  resources:
    requests:
      storage: 12Gi
```
