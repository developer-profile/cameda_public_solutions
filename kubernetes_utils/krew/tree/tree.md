# Tree

## Описание.
Плагин предназначен для представления ресурсов в древовидной форме. Например, deployment, replicaset, pod.

## Установка.
```
kubectl krew install tree
```

## Примеры использования.
```
kubectl tree deployment app
```

### Пример вывода.
```
kubectl tree deployment app
NAMESPACE  NAME                                       READY  REASON  AGE
default    Deployment/app                             -              9h
default    ├─ReplicaSet/app-566b89db69                -              9h
default    │ └─Pod/app-566b89db69-9t9kt               True           9h
default    │   └─CiliumEndpoint/app-566b89db69-9t9kt  -              9h
default    ├─ReplicaSet/app-6c4ffd46f8                -              9h
default    └─ReplicaSet/app-78f86ff9bf                -              9h
```

## Полезные ссылки.
GitHUB проекта: https://github.com/ahmetb/kubectl-tree
