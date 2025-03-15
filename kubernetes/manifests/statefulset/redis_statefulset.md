# StatefulSet with Redis
```
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: cam-redis-sts
  namespace: default
  labels:
    app: sts-redis
    environment: test
  annotations:
    author: cameda
spec:
  selector:
    matchLabels:
      app: redis-sts
  serviceName: "cam-redis"
  replicas: 2
  minReadySeconds: 10 # by default is 0
  template:
    metadata:
      labels:
        app: redis-sts
    spec:
      terminationGracePeriodSeconds: 30
      containers:
      - name: redis
        image: redis
        imagePullPolicy: IfNotPresent
        resources:
          requests:
            cpu: 1
            memory: 500Mi
        ports:
        - containerPort: 6379
        volumeMounts:
        - name: redis
          mountPath: /var/db
      restartPolicy: Always
      hostname: redis
      nodeSelector:
        kubernetes.io/os: linux
  volumeClaimTemplates:
  - metadata:
      name: redis
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: yc-network-ssd
      resources:
        requests:
          storage: 8Gi
---
apiVersion: v1
kind: Service
metadata:
  name: redis-svc-sts
  labels:
    app: redis
spec:
  ports:
  - name: redis
    port: 6379
  clusterIP: None
  selector:
    app: redis-sts
EOF
```
