# Интеграция с Yandex Lockbox

## Описание. 
В данном мануале рассмотрим установку External Secret Operator и его интеграцию с Yandex Lockbox.

## Поехали!

### Установим External Secret Operator.
```
helm install external-secrets \
   external-secrets/external-secrets \
    -n external-secrets \
    --create-namespace
```
---------------------------------------------------------
### Создаём секрет, в котором будут находиться креды для доступа к Lockbox изнутри Managed Kubernetes.
```
kubectl create secret generic yc-auth --from-file=authorized-key=/Users/cameda/practicum/key.json
```
---------------------------------------------------------

### Сохраним креды в сущность SecretStore. Там же выберем провайдера. В данном случае это Lockbox.
```
kubectl apply -f - <<< '
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:
  name: secret-store
spec:
  provider:
    yandexlockbox:
      auth:
        authorizedKeySecretRef:
          name: yc-auth
          key: authorized-key'
```

### Создадим сущность ExternalSecret которая скопирует содержимое внешнего секрета и положит его в Secret внутри Kubernetes.
```
kubectl apply -f - <<< '
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: external-secret
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: secret-store
    kind: SecretStore
  target:
    name: k8s-secret
  data:
  - secretKey: ssh
    remoteRef:
      key: e6qlemd2ka4bs6njl8i7
      property: ssh'
```

Где e6qlemd2ka4bs6njl8i7 - идентификатор секрета Lockbox.
k8s-secret - название секрета, который будет дублировать значение из Lockbox.

## Особенности.
* При создании объекта ExternalSecret секрет копируется в кластер Kubernetes в объект Secret. Который спокойно раскодируется с помощью base64 -d.
* В Secret помещаем IAM токен для SA от имени которого происходит управление кластером Kubernetes.
Сервисный аккаунт для ресурсов.
* Команда создания ключа для SA: yc iam key create --service-account-id $SA --output key.json
* У SA должны быть достаточные права для доступа к Lockbox.
Минимальные: lockbox.payloadViewer
* secretKey: ssh в настройках ExternalSecret должен совпадать с ключём секрета в Lockbox. Поле payload_entry_keys в выводе yc lockbox secret get <lockbox_id>.
* В поле remoteRef.key вставляется идентификатор секрета в Lockbox.
* В поле provider объекта SecretStore вставляем имя того провайдера, который будем использовать для работы. В данном примере это yandexlockbox.
* В поле authorizedKeySecretRef.name вставляем имя секрета, где хранятся креды для доступа к Lockbox.
* Рефреш каждый час. На тот случай если секрет в Lockbox поменяется.

## Пример создания.

* Секрет в Lockbox.
```
yc lockbox secret get e6qlemd2ka4bs6njl8i7
id: e6qlemd2ka4bs6njl8i7
folder_id: b1gxxxxx
created_at: "2023-12-20T22:16:33.290Z"
name: lockbox-secret
description: k8s+lockbox
labels:
  prod: lb-k8s
kms_key_id: abjxxxxx
status: ACTIVE
current_version:
  id: e6q4i59lqt880o7a2p34
  secret_id: e6qlemd2ka4bs6njl8i7
  created_at: "2023-12-20T22:16:33.290Z"
  status: ACTIVE
  payload_entry_keys:
    - ssh
deletion_protection: true
```

* Установим External Secret Operator с помощью helm.
* Создадим секрет для доступа к Lockbox из Kubernetes.
```
kubectl create secret generic yc-auth --from-file=authorized-key=/Users/cameda/practicum/key.json
```
* Создадим SecretStore.
```
kubectl get ss
NAME           AGE   STATUS   CAPABILITIES   READY
secret-store   12s   Valid    ReadOnly       True
```

* Создадим ExternalSecret.
```
kubectl get es
NAME              STORE          REFRESH INTERVAL   STATUS         READY
external-secret   secret-store   1h                 SecretSynced   True
```

* Проверим Secret.
```
kubectl get secret
NAME         TYPE     DATA   AGE
k8s-secret   Opaque   1      8m51s
yc-auth      Opaque   1      22m
```
```
kubectl get secret k8s-secret --template={{.data.ssh}} | base64 -d
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDI98mJDBN9cnp6HOdBYTQILeAhUSDvDfoqA9iLmVPDyPLFRWs7tE4BjCAcFD6a3M50QIboCaohfa7h+PWksYibab7I3QHOR7y9pCW8FGonGRw2ACvt906qlaWHFj7jWOxuihFoiRROKqLCW5YE/Yc4XFIvW1gu3JQdvQ1wemWvujsI8EHE6PI1pEg7/41y6kn3IhNHIr8WRLe4dPyPGjwc4LpBCcaRSJiX4YjVXynSIHNk365UrL+nGv8ix7bW5FNCgGqSgfUTVCfMYLzQ/gYHPVQrcIvCeHjkwluH8Z3gXeN3OliejBjpLi+IWIzd9K6UADSUNU8oL+9941tDidp8APoe7RbB4h3bY6k8Bhy0yxohgQS2OWSYd1mjeEx8Ba5wzJKqfpUgmcPdrBJnBwLgLMFQyEfYG6vTPkYWAKEvkkJ6ZiA4tdoQvCb+B0xJV/ivHyLtoi3LFE59mbQFDUy8O51vX9JjBDLwzyTEeslWp7uOP66Ti5Q5ucNXbs5yXTU= cameda@cameda-osx
```
* Поменял секрет в Lockbox. И через час проверим изменения в Secret k8s-secret.
```
kubectl get secret k8s-secret --template={{.data.ssh}} | base64 -d
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDI98mJDBN9cnp6HOdBYTQILeAhUSDvDfoqA9iLmVPDyPLFRWs7tE4BjCAcFD6a3M50QIboCaohfa7h+PWksYibab7I3QHOR7y9pCW8FGonGRw2ACvt906qlaWHFj7jWOxuihFoiRROKqLCW5YE/Yc4XFIvW1gu3JQdvQ1wemWvujsI8EHE6PI1pEg7/41y6kn3IhNHIr8WRLe4dPyPGjwc4LpBCcaRSJiX4YjVXynSIHNk365UrL+nGv8ix7bW5FNCgGqSgfUTVCfMYLzQ/gYHPVQrcIvCeHjkwluH8Z3gXeN3OliejBjpLi+IWIzd9K6UADSUNU8oL+9941tDidp8APoe7RbB4h3bY6k8Bhy0yxohgQS2OWSYd1mjeEx8Ba5wzJKqfpUgmcPdrBJnBwLgLMFQyEfYG6vTPkYWAKEvkkJ6ZiA4tdoQvCb+B0xJV/ivHyLtoi3LFE59mbQFDUy8O51vX9JjBDLwzyTEeslWp7uOP66Ti5Q5ucNXbs5yXTU=
```

В конце нет имени пользователя. Потому что я его удалил. Синхронизация секрета выполнилась!
