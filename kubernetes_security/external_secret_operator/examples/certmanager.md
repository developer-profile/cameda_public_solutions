# Интеграция с Yandex Certificate Manager

## Описание.
С помощью данной интеграции можно создать в Yandex Certificate Manager сертификат и подключить во все кластера Kubernetes.

## Поехали!
```
Секрет в Certificate Manager создаём в мануале 01.create_user_cert.md.
export SA=$(yc iam service-account get cameda-practicum --folder-name cameda-practicum --format json | jq -r '.id')
export CERT=$(yc cm certificate get cam-cert --folder-name cameda-practicum --format=json | jq -r ".id")
```
### Задаём права для SA на доступ к секрету..
yc cm certificate add-access-binding --id $CERT \
  --service-account-id $SA \
  --role certificate-manager.certificates.downloader \
  --async

### Установим External Secret Operator.
```
helm install external-secrets \
   external-secrets/external-secrets \
    -n external-secrets \
    --create-namespace
```
---------------------------------------------------------

### Создаём секрет, в котором будут находиться креды для доступа к CM изнутри Managed Kubernetes.
```
kubectl create secret generic yc-auth-cm --from-file=authorized-key=/Users/cameda/practicum/key.json
```
---------------------------------------------------------

### Сохраним креды в сущность SecretStore. Там же выберем провайдера. В данном случае это Certificate Manager.
```
kubectl apply -f - <<< '
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:
  name: secret-store-cm
spec:
  provider:
    yandexcertificatemanager:
      auth:
        authorizedKeySecretRef:
          name: yc-auth-cm
          key: authorized-key'
```

### Создадим сущность ExternalSecret которая скопирует содержимое внешнего секрета и положит его в Secret внутри Kubernetes.
```
kubectl apply -f - <<< '
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: external-secret-cm
spec:
  refreshInterval: 22h
  secretStoreRef:
    name: secret-store-cm
    kind: SecretStore
  target:
    name: k8s-secret-cm
    template:
      type: kubernetes.io/tls
  data:
  - secretKey: tls.crt # the target k8s secret key
    remoteRef:
      key: fpqrffkcjs5d2gsd4575 # the certificate ID
      property: chain
  - secretKey: tls.key # the target k8s secret key
    remoteRef:
      key: fpqrffkcjs5d2gsd4575 # the certificate ID
      property: privateKey'
```
--------------------------------------------------------------------------------------
### Результат.
```
kubectl get es
NAME                 STORE             REFRESH INTERVAL   STATUS         READY
external-secret      secret-store      1h                 SecretSynced   True
external-secret-cm   secret-store-cm   22h                SecretSynced   True
```

### Обратить внимание!
* Обязательно нужно выдать права на сертификат для SA. По-умолчанию их нет.
* Имена tls.crt и tls.key не имеют значения. Важно чтобы кодировка была PEM.

## Мануал.
https://external-secrets.io/main/provider/yandex-certificate-manager/
