# LimitRange

## Описание.
LimitRange проверяет, что значения реквестов и лимтов для подов укладываются в минимальные и максимальные значения, указанные в его спецификации.
Также он устанавливает дефолтные значения для контейнеров, если они не были установлены руками.

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
    max: # max and min define the limit range
      cpu: "1"
    min:
      cpu: 100m
EOF
```
