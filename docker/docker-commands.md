# Полезные в работе с docker команды

## Создание имиджа и пуш его в реестр.
Создаём имидж на основе Dockerfile: docker build -t alpine -f Dockerfile .

Меняем тег: docker tag cr.yandex/<идентификатор_реестра>/alpine

Пушим созданный имидж в реджистри: docker push cr.yandex/<идентификатор_реестра>/alpine

## Работа с имиджами.
```
docker image list  # Просмотр информации об имиджах
docker rmi <image_name> <image_id> # Удаление имиджа
docker rmi $(docker images -aq) # Удаление всех имиджей
docker history <image_id>
```

## Запуск контейнера.
```
Запуск контейнера с имиджем nginx: docker run nginx
Запуск контейнера с имиджем nginx:1.19-alpine:  docker run -d --name webapp nginx:1.19-alpine
docker run -d -p 30082:8080 nginx
docker run -ti nginx
docker run -d -e MYSQL_ROOT_PASSWORD=db_pass123 --name mysql-db --network wp-mysql-network mysql
docker run -d --cpus=2 --memory=100m nginx
docker run -d --name stress75 --cpuset-cpus 0 --cpu-shares 768 nginx
docker run -it alpine ip addr show
docker run -it --pid=host alpine ps aux
```

## Использование контейнера отладчика.
```
docker run -d --name http nginx:alpine
docker run --net=container:http benhall/curl curl -s localhost
docker run --pid=container:http alpine ps aux
```

## Работа с контейнерами.
```
docker ps # Просмотр запущенных контейнеров
docker ps -a # Просмотр всех контейнеров

docker stop $(docker ps -aq) # Остановка всех запущенных контейнеров
docker rm $(docker ps -aq) # Удаление всех остановленных контейнеров

docker inspect <container_id>
docker history 
```

## Редкие комманды.
```
docker stats --no-stream
```

## Работа с сетями.
```
docker network ls
docker run -d --name alpine-2 --network=none alpine sleep 1d
docker network create --driver bridge --subnet 172.22.0.0/24 --gateway 172.22.0.1 wp-mysql-network
```


