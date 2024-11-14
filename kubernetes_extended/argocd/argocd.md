# ArgoCD

## Описание.
Решение для пулла изменений из Git репозитория в кластер k8s. Реализует GitOps подход.

## Установка.
```
export HELM_EXPERIMENTAL_OCI=1 && \
helm pull oci://cr.yandex/yc-marketplace/yandex-cloud/argo/chart/argo-cd \
--version=7.3.11-2 \
--untar && \
helm install -n argocd \
  --create-namespace \
  argocd argo-cd 
```
