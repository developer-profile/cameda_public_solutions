# Htpasswd

## Описание.
Плагин предназначен для создания секрета с шифрованием bcrypt. Подходит для basic_auth авторизации в ingress-nginx.

## Установка.
```
kubectl krew install htpasswd
```

## Примеры использования.
```
kubectl htpasswd create secretname USER1=PASSWORD1 USER2=PASSWORD2
kubectl htpasswd create secretname USER1=PASSWORD1 USER2=PASSWORD2 -o yaml --dry-run
```

## Полезные ссылки.
GitHUB проекта: https://github.com/shibumi/kubectl-htpasswd
