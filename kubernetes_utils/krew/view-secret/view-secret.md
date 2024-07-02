# View secret

## Описание.
Данный плагин позволяет просмотреть секрет в кластере в уже расшифрованном виде.

## Установка.
```
kubectl krew install view-secret
```

## Команды.
```
kubectl view-secret cam-secret -a
```
### Примеры использования.
```
kubectl create secret generic cam-secret --from-literal=user=cameda --from-literal=password=pass
kubectl view-secret cam-secret -a
password='pass'
user='cameda'
```
### Стандартный способ декодирования.
```
kubectl get secrets/cam-secret --template={{.data.user}} | base64 -D
kubectl get secrets/cam-secret1 --template={{.data.password}} | base64 -D
```

## Полезные ссылки.
GitHUB проекта: https://github.com/ahmetb/kubectl-extras
