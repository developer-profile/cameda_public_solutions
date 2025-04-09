# Create fio container and create Pod

## Описание.
Запустим тесты fio на случайное чтение (randread).

### План действий.
1. Создадим имидж на основе Alpine и установим в него fio.
2. Запушим полученный имидж в Container Registry.
3. Создадим ConfigMap для работы fio.
4. Создадим PV на основе csi-s3 для хранения отчётов о работе fio.
5. Создадим PV для тестируемого диска.
6. Создадим под и зашедулим его.
7. Проверим работу системы.
--------------------------------------------------------------------------

1. Создадим имидж на основе Dockerfile из resource/dockerfile.
```
podman build -t cr.yandex/crp59ldu2qv9q43uq5jh/fio:1.0.0 -f Dockerfile .
podman images                      # Проверяем что имидж с тегом 1.0.0 создался. 
```

2. Запушим полученный имидж в Container Registry.
```
export YC_IAM_TOKEN=$(yc iam create-token)
podman login \
  --username iam \
  --password $YC_IAM_TOKEN \
  cr.yandex

podman push cr.yandex/crp59ldu2qv9q43uq5jh/fio:1.0.0
```

3. Создадим PV на основе csi-s3 для хранения отчётов о работе fio.
  
  3.1. Установим csi-s3 из чарта по мануалу: https://github.com/Cameda/Yandex-Cloud/blob/main/manifests/k8s-marketplace/csi-s3.md
  
  3.2. Создадим PVC.
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: csi-s3-pvc-dynamic
  namespace: default
spec:
  accessModes:
  - ReadWriteMany
  resources:
    requests:
      storage: 5Gi
  storageClassName: csi-s3
EOF
```

4. Создадим PV для тестируемого диска.
PVC создаём отсюда: https://github.com/Cameda/public_solutions/blob/main/kubernetes/manifests/pv_pvc/yc/pvc.md
Пример:
```
cat <<EOF | kubectl apply -f -
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
      storage: 120Gi
EOF
```

```
kubectl get pvc
NAME                 STATUS    VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS     VOLUMEATTRIBUTESCLASS   AGE
csi-s3-pvc-dynamic   Bound     pvc-eb0817cc-34c3-486f-a9a9-9bbb96d01668   5Gi        RWX            csi-s3           <unset>                 22m
pvc-dynamic-ssd      Pending                                                                        yc-network-ssd   <unset>                 10s

kubectl get pv
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                        STORAGECLASS     VOLUMEATTRIBUTESCLASS   REASON   AGE
pvc-eb0817cc-34c3-486f-a9a9-9bbb96d01668   5Gi        RWX            Retain           Bound    default/csi-s3-pvc-dynamic   csi-s3           <unset>                          23m
```

5. Зашедулим поды. Спеки подов лежат в resources. Один под для read тестов. Другой для write.

## Результат.
```
randread: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=16
...
fio-3.38
Starting 8 processes

randread: (groupid=0, jobs=8): err= 0: pid=13: Mon Apr  7 11:55:57 2025
  read: IOPS=4016, BW=15.7MiB/s (16.5MB/s)(1884MiB/120036msec)
    slat (nsec): min=1888, max=7546.6k, avg=8225.71, stdev=18587.14
    clat (usec): min=93, max=80886, avg=31852.91, stdev=3656.34
     lat (usec): min=1354, max=80894, avg=31861.14, stdev=3656.15
    clat percentiles (usec):
     |  1.00th=[15008],  5.00th=[30016], 10.00th=[30802], 20.00th=[31327],
     | 30.00th=[31327], 40.00th=[31589], 50.00th=[31851], 60.00th=[32113],
     | 70.00th=[32375], 80.00th=[32375], 90.00th=[32900], 95.00th=[34866],
     | 99.00th=[43254], 99.50th=[45876], 99.90th=[53216], 99.95th=[56886],
     | 99.99th=[63701]
   bw (  KiB/s): min=15411, max=47742, per=100.00%, avg=16089.98, stdev=257.22, samples=1912
   iops        : min= 3852, max=11934, avg=4021.27, stdev=64.30, samples=1912
  lat (usec)   : 100=0.01%
  lat (msec)   : 2=0.02%, 4=0.51%, 10=0.39%, 20=0.23%, 50=98.64%
  lat (msec)   : 100=0.19%
  cpu          : usr=0.21%, sys=0.73%, ctx=456694, majf=0, minf=197
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=100.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=482184,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=16

Run status group 0 (all jobs):
   READ: bw=15.7MiB/s (16.5MB/s), 15.7MiB/s-15.7MiB/s (16.5MB/s-16.5MB/s), io=1884MiB (1975MB), run=120036-120036msec

Disk stats (read/write):
  vdb: ios=481637/5, sectors=3853096/56, merge=0/2, ticks=15334598/164, in_queue=14375024, util=100.00%
```
