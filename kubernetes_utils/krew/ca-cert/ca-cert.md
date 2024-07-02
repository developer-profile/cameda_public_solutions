# Ca-cert

## Описание.
Плагин предназначен для просмотра корневого сертификата кластера Kubernetes.

## Установка.
```
kubectl krew install ca-cert
```

## Примеры использования.
```
kubectl ca-cert

Вывод можно отправить в файл, а далее получить информацию из сертификата.
kubectl ca-cert > ca.crt
openssl x509 -in ca.crt -text
```

## Полезные ссылки.
GitHUB проекта: https://github.com/ahmetb/kubectl-extras
