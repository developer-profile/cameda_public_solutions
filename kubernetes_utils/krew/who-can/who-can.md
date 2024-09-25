# Who-can

## Описание.
Плагин предназначен для просмотра информации о пользователе, который имеет некоторый набор прав (действий) в отношении сущности Kubernetes.

## Установка.
```
kubectl krew install who-can
```

## Примеры использования.
```
kubectl who-can watch secret -A
kubectl who-can get po -n kube-system
```
```
kubectl who-can watch secret -A
CLUSTERROLEBINDING                           SUBJECT                          TYPE            SA-NAMESPACE
ccm-binding                                  system:cloud-controller-manager  User
cluster-admin                                system:masters                   Group
ingress-nginx                                ingress-nginx                    ServiceAccount  ingress-nginx
multi-kyverno                                multi-kyverno                    ServiceAccount  kyverno
secretprovidersyncing-rolebinding            secrets-store-csi-driver         ServiceAccount  hcv
system:controller:generic-garbage-collector  generic-garbage-collector        ServiceAccount  kube-system
system:controller:resourcequota-controller   resourcequota-controller         ServiceAccount  kube-system
system:kube-controller-manager               system:kube-controller-manager   User
yc:admin                                     yc:admin                         Group
yc:editor                                    yc:editor                        Group
```

## Полезные ссылки.
GitHUB проекта: https://github.com/aquasecurity/kubectl-who-can
Habr статья, где есть пример использования: https://habr.com/ru/companies/rtlabs/articles/732858/
