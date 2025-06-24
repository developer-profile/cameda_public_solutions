# RoleBinding

## Описание.
Данный объект кластера k8s связывает роль и аккаунт. Для того чтобы предоставить аккаунту необходимые для работы роли.

## Пример.
```
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: podonlybind
  namespace: default
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: pod-only
subjects:
- kind: ServiceAccount
  name: cam-sa
  namespace: default
```
