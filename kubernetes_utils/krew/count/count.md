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

### Пример вывода.
```
kubectl count pods,ds,deploy
+-------------+------------------------+------------+-------+
|  Namespace  |      GroupVersion      |    Kind    | Count |
+-------------+------------------------+------------+-------+
| strimzi     | v1                     | Pod        |     1 |
+-------------+                        +            +-------+
| default     |                        |            |     3 |
+-------------+                        +            +-------+
| kube-system |                        |            |    23 |
+-------------+------------------------+------------+-------+
| strimzi     | metrics.k8s.io/v1beta1 | PodMetrics |     1 |
+-------------+                        +            +-------+
| default     |                        |            |     3 |
+-------------+                        +            +-------+
| kube-system |                        |            |    22 |
+             +------------------------+------------+-------+
|             | apps/v1                | DaemonSet  |     7 |
+-------------+                        +------------+-------+
| strimzi     |                        | Deployment |     1 |
+-------------+                        +            +       +
| default     |                        |            |       |
+-------------+                        +            +-------+
| kube-system |                        |            |     5 |
+-------------+------------------------+------------+-------+
```

## Полезные ссылки.
GitHUB проекта: https://github.com/chenjiandongx/kubectl-count
