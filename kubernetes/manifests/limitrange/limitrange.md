# LimitRange

## Описание.
LimitRange проверяет, что значения реквестов и лимтов для подов укладываются в минимальные и максимальные значения, указанные в его спецификации.
Также он устанавливает дефолтные значения для контейнеров, если они не были установлены руками.

## Пример с контейнером.
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: LimitRange
metadata:
  name: cam-limits
  namespace: default
  labels:
    limit: pod
    environment: prod
  annotations:
    author: cameda
spec:
  limits:
  - type: Container
    default: # this section defines default limits
      cpu: 500m
    defaultRequest: # this section defines default requests
      cpu: 500m
      memory: 1Gi 
    max: # max and min define the limit range
      cpu: "1"
    min:
      cpu: 100m
EOF
```

## Пример с хранилищем.
```
apiVersion: v1
kind: LimitRange
metadata:
  name: storage-limit-range
  namespace: default
spec:
  limits:
  - type: PersistentVolumeClaim
    min:
      storage: 1Gi
    max:
      storage: 10Gi
```

## Пример с Ratio.
```
apiVersion: v1
kind: LimitRange
metadata:
  name: ratio-limit-range
spec:
  limits:
  - type: Container
    maxLimitRequestRatio:
      cpu: 2
      memory: 2
```

## Заметки.
1. Если не указывать реквесты и лимиты при созданном LimitRange, то подставятся дефолтные значения.
2. При попытке указать реквесты/лимиты за пределами рэнджа, выдастся ошибка.

Примеры ошибок:
```
Error from server (Forbidden): error when creating "pod.yaml": pods "cam-pod-nginx1" is forbidden: minimum cpu usage per Container is 100m, but request is 20m

Error from server (Forbidden): error when creating "pod.yaml": pods "cam-pod-nginx1" is forbidden: maximum cpu usage per Container is 1, but limit is 2
```

## Полезные ссылки.
1. https://kubernetes.io/docs/concepts/policy/limit-range/
2. https://www.compilenrun.com/docs/devops/kubernetes/kubernetes-administration/kubernetes-limitranges
