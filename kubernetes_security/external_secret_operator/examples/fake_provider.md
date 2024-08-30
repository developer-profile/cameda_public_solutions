# Fake provider

## Описание.
Предназначен для теста. Работает ли в принципе External Secret или нет.

## Поехали!
-------------------------------------------------------------------------
```
cat <<EOF | kubectl apply -f -
apiVersion: external-secrets.io/v1beta1
kind: ClusterSecretStore
metadata:
  name: fake
spec:
  provider:
    fake:
      data:
      - key: "/foo/bar"
        value: "HELLO1"
        version: "v1"
      - key: "/foo/bar"
        value: "HELLO2"
        version: "v2"
      - key: "/foo/baz"
        value: '{"john": "doe"}'
        version: "v1"
EOF
```
```
kubectl apply -f - <<< '
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: example
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: fake
    kind: ClusterSecretStore
  target:
    name: secret-to-be-created
  data:
  - secretKey: foo_bar
    remoteRef:
      key: /foo/bar
      version: v1
  dataFrom:
  - extract:
      key: /foo/baz
      version: v1'
```
----------------------------------------------------------------

## Результат.
```
kubectl get css
NAME   AGE   STATUS   CAPABILITIES   READY
fake   37s   Valid    ReadWrite      True
```
```
kubectl get es
NAME                 STORE             REFRESH INTERVAL   STATUS         READY
example              fake              1h                 SecretSynced   True
```

## Мануал.
https://external-secrets.io/main/provider/fake/
