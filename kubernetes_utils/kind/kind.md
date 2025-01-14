# Kind

## Описание.
Простое решение для запуска кластера k8s как docker контейнера на локальном компьютере. Для работы требуются go > 1.16 и docker.

## Установка для Mac.
```
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.26.0/kind-darwin-amd64
chmod +x ./kind
cp kind /usr/local/bin
```

### Команды.
1. Создание кластера: kind create cluster

2. Удаление кластера: kind delete cluster

## Полезные ссылки.
1. О решении: https://kind.sigs.k8s.io/

2. Установка: https://kind.sigs.k8s.io/docs/user/quick-start/#installation
