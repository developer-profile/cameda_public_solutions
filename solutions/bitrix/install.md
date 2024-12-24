# Установка Bitrix в Yandex Cloud

## Описание.
Установим Bitrix в Managed Kubernetes с помощью daemonset. Директорию upload будем хранить в S3.

## Поехали!

### Создадим бакет в S3 и скопируем в него папку upload.
```
export FOLDER=$(yc resource folder get cameda-practicum --format=json | jq -r ".id")
export bucket_name=cam-bitrix

yc storage bucket create \
  --folder-id $FOLDER \
  --name $bucket_name \
  --default-storage-class STANDARD \
  --max-size 200 \
  --async
```

Копируем в этот бакет директорию upload. Для этого установим утилиту s3cmd и сконфигурируем её.

Устанавливаем s3cmd: https://s3tools.org/usage
```
s3cmd --configure
s3cmd --storage-class STANDARD --recursive put upload s3://cam-bitrix
```
