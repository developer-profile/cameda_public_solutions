# Полезные в работе с docker команды

## Создание имиджа и пуш его в реестр.
Создаём имидж на основе Dockerfile: docker build -t alpine -f Dockerfile .
Меняем тег: docker tag cr.yandex/<идентификатор_реестра>/alpine
Пушим созданный имидж в реджистри: docker push cr.yandex/<идентификатор_реестра>/alpine

## Работа с имиджами.
```
Просмотр информации об имиджах: docker image list
Удаление имиджа: docker rmi <image_name> <image_id>
```
