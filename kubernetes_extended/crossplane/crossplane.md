# Crossplane

## Описание.
Данное решение является представителем семейства IaC. Как и Terraform позволяет создавать ресурсы в облаке. Но в отличие от Terraform, Crossplane работает из Kubernetes.

## Установка.
```
helm pull oci://cr.yandex/yc-marketplace/yandex-cloud/crossplane/crossplane \
  --version 1.15.0 \
  --untar && \
helm install \
  --namespace crossplane \
  --create-namespace \
  --set-file providerJetYc.creds=/Users/cameda/practicum/key.json \
  crossplane ./crossplane/
```

## Полезные ссылки.
Провайдер в YC: https://github.com/yandex-cloud/crossplane-provider-yc?ysclid=m38lzcbtjw856691222
Examples: https://github.com/yandex-cloud/crossplane-provider-yc/tree/main/examples
