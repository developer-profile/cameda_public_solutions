# Pod example QoS class

## BestEffort.
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: cam-pod-nginx-besteffort
  namespace: default
  labels:
    cam: nginx
  annotations:
    author: cameda
spec:
  containers:
  - name: nginx-besteffort
    image: nginx:alpine
    imagePullPolicy: IfNotPresent
    ports:
    - containerPort: 80
  restartPolicy: OnFailure
  hostname: nginx
  nodeSelector:
    kubernetes.io/os: linux
EOF
```

## Burstable.
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: cam-pod-nginx-burstable
  namespace: default
  labels:
    cam: nginx
  annotations:
    author: cameda
spec:
  containers:
  - name: nginx-burstable
    image: nginx:alpine
    imagePullPolicy: IfNotPresent
    resources:
      requests:
        cpu: "20m"
        memory: "20Mi"
      limits:
        memory: "50Mi"
    ports:
    - containerPort: 80
  restartPolicy: OnFailure
  hostname: nginx
  nodeSelector:
    kubernetes.io/os: linux
EOF
```

## Guaranteed.
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: cam-pod-nginx-guaranteed
  namespace: default
  labels:
    cam: nginx
  annotations:
    author: cameda
spec:
  containers:
  - name: nginx-guaranteed
    image: nginx:alpine
    imagePullPolicy: IfNotPresent
    resources:
      requests:
        cpu: "20m"
        memory: "20Mi"
      limits:
        cpu: "20m"
        memory: "20Mi"
    ports:
    - containerPort: 80
  restartPolicy: OnFailure
  hostname: nginx
  nodeSelector:
    kubernetes.io/os: linux
EOF
```
