# Service ExternalName

## Описание.
Пример сервиса с типом ExternalName.

## Пример.
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  name: my-service
  namespace: default
spec:
  type: ExternalName
  externalName: <db>
EOF
```
