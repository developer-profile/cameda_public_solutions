# MinIO

## Описание.
Известное хранилище с поддержкой S3. 

## Установка.
```
1. curl https://raw.githubusercontent.com/minio/docs/master/source/extra/examples/minio-dev.yaml -O
2. kubectl label no <NODE_NAME> cam=minio
3. Добавляем в файл minio-dev.yaml блок tolerations. И меняем nodeSelector на cam: minio.
kubectl apply -f minio-dev.yaml
```

### Содержимое файла minio-dev.yaml у меня.
```
# Deploys a new Namespace for the MinIO Pod
apiVersion: v1
kind: Namespace
metadata:
  name: minio-dev # Change this value if you want a different namespace name
  labels:
    name: minio-dev # Change this value to match metadata.name
---
# Deploys a new MinIO Pod into the metadata.namespace Kubernetes namespace
#
# The `spec.containers[0].args` contains the command run on the pod
# The `/data` directory corresponds to the `spec.containers[0].volumeMounts[0].mountPath`
# That mount path corresponds to a Kubernetes HostPath which binds `/data` to a local drive or volume on the worker node where the pod runs
#
apiVersion: v1
kind: Pod
metadata:
  labels:
    app: minio
  name: minio
  namespace: minio-dev # Change this value to match the namespace metadata.name
spec:
  containers:
  - name: minio
    image: quay.io/minio/minio:latest
    command:
    - /bin/bash
    - -c
    args:
    - minio server /data --console-address :9090
    volumeMounts:
    - mountPath: /data
      name: localvolume # Corresponds to the `spec.volumes` Persistent Volume
  nodeSelector:
    cam: minio
  tolerations:
  - key: cam
    value: minio
    operator: Equal
    effect: NoSchedule
  volumes:
  - name: localvolume
    hostPath: # MinIO generally recommends using locally-attached volumes
      path: /mnt/disk1/data # Specify a path to a local drive or volume on the Kubernetes worker node
      type: DirectoryOrCreate # The path to the last directory must exist
---
apiVersion: v1
kind: Service
metadata:
  name: minio
  namespace: minio-dev
spec:
  type: ClusterIP
  selector:
    app: minio
  ports:
  - port: 9000
    name: minio
    targetPort: 9090
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: minio
  namespace: minio-dev
spec:
  ingressClassName: nginx
  rules:
    - host: minio.cameda1.ru
      http:
        paths:
        - path: /
          pathType: Prefix
          backend:
            service:
              name: minio
              port:
                number: 9090
```

### Подключаем SSL сертификат от Let's Encrypt.
Предполагаю, что Cert Manager уже установлен. 
Если не установлен, то ставим: https://github.com/Cameda/public_solutions/blob/main/kubernetes_extended/cert-manager/helm.md
```
cat <<EOF | kubectl apply -f -
apiVersion: cert-manager.io/v1
kind: Issuer
metadata:
  name: minio
  namespace: minio-dev
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: cameda@yandex.ru
    privateKeySecretRef:
      name: minio
    solvers:
    - http01:
        ingress:
          class: nginx
---
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: minio
  namespace: minio-dev
spec:
  secretName: minio-tls-secret
  issuerRef:
    name: minio
    kind: Issuer
  commonName: minio.cameda1.ru
  dnsNames:
  - minio.cameda1.ru
EOF
```

### Ingress with cert.
```
cat <<EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: minio
  namespace: minio-dev
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod-minio"
    nginx.ingress.kubernetes.io/backend-protocol: "HTTPS"
    nginx.ingress.kubernetes.io/auth-tls-verify-client: "false"
spec:
  ingressClassName: nginx
  tls:
    - hosts:
      - minio.cameda1.ru
      secretName: minio-tls-secret
  rules:
    - host: minio.cameda1.ru
      http:
        paths:
        - path: /
          pathType: Prefix
          backend:
            service:
              name: minio
              port:
                number: 443
EOF
```

## Полезные ссылки.
MinIO: https://min.io/docs/minio/kubernetes/upstream/index.html
