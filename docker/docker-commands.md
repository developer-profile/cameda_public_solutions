# Полезные в работе с docker команды

## Создание имиджа и пуш его в реестр.
Создаём имидж на основе Dockerfile: docker build -t alpine -f Dockerfile .
Меняем тег: docker tag cr.yandex/<идентификатор_реестра>/alpine
Пушим созданный имидж в реджистри: docker push cr.yandex/<идентификатор_реестра>/alpine

## Работа с имиджами.
```
Просмотр информации об имиджах: docker image list
Удаление имиджа: docker rmi <image_name> <image_id>
Удаление всех имиджей: docker rmi $(docker images -aq)
```

## Запуск контейнера.
```
Запуск контейнера с имиджем nginx: docker run nginx
Запуск контейнера с имиджем nginx:1.19-alpine:  docker run -d --name webapp nginx:1.19-alpine
docker run -d -p 30082:8080 nginx
docker run -ti nginx
```

## Работа с контейнерами.
```
Просмотр запущенных контейнеров: docker ps
Просмотр всех контейнеров: docker ps -a

Остановка всех запущенных контейнеров: docker stop $(docker ps -aq)
Удаление всех остановленных контейнеров: docker rm $(docker ps -aq)
```
