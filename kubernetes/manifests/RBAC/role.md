# Role

## Описание.
Эта сущность описывает набор действий (verbs), которые можно производить с объектами кластера Kubernetes. Такими как: Pod, Service, etc.

## Примеры использования.

### Предоставление всех прав на все ресурсы в пределах namespace dev.
```
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: dev
  name: admin-dev-ns
rules:
- apiGroups: [""] # "" indicates the core API group
  resources: ["*"]   
  verbs: ["*"]
```

```
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: cam-role
  namespace: default
rules:
- apiGroups:
  - ""
  resources:
  - pods
  - pods/status
  - service
  - pods/log
  verbs:
  - create
  - get
  - list
  - watch
```

```
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: cam-role
  namespace: default
rules:
- apiGroups:
  - "apps"
  resources:
  - deployments
  verbs:
  - create
  - get
  - list
  - watch
  - update
  - patch
  - delete
```

### Императивный способ создания.
```
kubectl create role cam-role --verb=create,get,list,watch --resource=pods,pods/status
```

### Список действий (verbs).
```
verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
```
