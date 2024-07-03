# Deprecations

## Описание.
Данный плагин позволяет провести анализ кластера или манифеста на предмет устаревших API версий.

## Установка.
```
kubectl krew install deprecations
```

## Примеры использования.
```
kubectl deprecations --k8s-version=v1.29.1
helm template -f values.yaml .0 | kubectl deprecations --k8s-version v1.29.1 --input-file=-

Работает только если есть права админа на кластер.
```

## Полезные ссылки.
GitHUB проекта: https://github.com/onatm/kubectl-allctx
