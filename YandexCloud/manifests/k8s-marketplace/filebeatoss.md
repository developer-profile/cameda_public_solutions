# Filebeat OSS

## Описание.
Агент выгрузки логов в Opensearch.

## Поехали!
```
helm pull oci://cr.yandex/yc-marketplace/yandex-cloud/filebeat-oss/chart/filebeat-oss \
  --version 7.12.1-1 \
  --untar && \
helm install \
  --namespace filebeat \
  --create-namespace \
  --set app.url='https://rc1d-p8f9lrc26irvhdce.mdb.yandexcloud.net:9200' \
  --set app.username='admin' \
  --set app.password='P@$$w0rd' \
  filebeatoss ./filebeat-oss/
```
