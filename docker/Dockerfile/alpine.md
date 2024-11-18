# Alpine 3.16 from scratch

## Описание.
Создадим базовый образ с Alpine.

## Поехали!
Создадим Dockerfile с содержимым ниже.

```
FROM scratch
ADD alpine-minirootfs-3.16.2-x86_64.tar.gz /
RUN adduser -D -g '' worker
RUN adduser -D -g '' auditor
CMD ["/bin/sh"]
USER worker
```

Архив качаем с официального сайта Alpine и кладём в туже директорию, что Dockerfile.
https://dl-cdn.alpinelinux.org/alpine/v3.16/releases/

### Собираем образ.
```
docker build -t alpine:worker -f Dockerfile .
```

Где alpine:worker является тегом образа.
```
docker images
REPOSITORY   TAG       IMAGE ID       CREATED              SIZE
alpine       worker    664d6e5e6c1a   About a minute ago   5.55MB
```

## Если надо удалить что-то из архива, то можно его распаковать, удалить что-то и упаковать заново. Или можно запустить команду RUN для удаления из образа лишнего.
```
FROM scratch
ADD alpine-no-ps-minirootfs.tar.gz /
RUN adduser -D -g '' worker
RUN adduser -D -g '' auditor
CMD ["/bin/sh"]
RUN rm -rf /bin/ls
USER worker
```
