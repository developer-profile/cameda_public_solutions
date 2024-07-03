# Count

## Описание.
Данный плагин позволяет подсчетать количество объектов в кластере. Например, сколько pod, deployment, secret, etc.
Есть возможность смотреть как во всём кластере, так и в отдельном namespace.

## Установка.
```
kubectl krew install count
```

## Примеры использования.
```
# display a table of specified resources counts, kinds split by comma.
  kubectl count pods,ds,deploy

# display kube-system namespace resources counts info in yaml format.
  kubectl count -oy -n kube-system rs,ep

# Вывод в формате json список объектов по всем ns.
  kubectl count service,ds,rs -oj -A

# Ещё небольшой пример.
  kubectl count -oy -n kube-system deploy,svc
```

## Полезные ссылки.
GitHUB проекта: https://github.com/chenjiandongx/kubectl-count
