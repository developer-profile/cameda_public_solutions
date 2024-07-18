# Certificate Manager

## Создаём сертификат для валидации в Let's Encrypt.

```
yc certificate-manager certificate request \
  --folder-id $FOLDER \
  --name kube-infra \
  --domains "*.cameda1.ru" \
  --challenge dns
```
```
export CERT=$(yc cm certificate get kube-infra --folder-name cameda-practicum --format=json | jq -r ".id")
```
