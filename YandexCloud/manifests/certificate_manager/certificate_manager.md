# Certificate Manager

## Создаём сертификат для валидации в Let's Encrypt.
```
export FOLDER=$(yc resource folder get cameda-practicum --format=json | jq -r ".id")
```
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
