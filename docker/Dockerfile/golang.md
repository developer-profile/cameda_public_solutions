


FROM golang:alpine
ENV GO111MODULE=auto
WORKDIR /app
ADD . /app
RUN cd /app && go build -o goapp
ENTRYPOINT ./goapp

docker build -t go-big -f Dockerfile .
-------------------------------------------------
## Артефакт собирается в одном контейнере, а потом копируется отдельно в новый контейнер, в котором уже нет ненужной для его работы сборочной среды.

# build stage
FROM golang:alpine AS build-env
ENV GO111MODULE=auto
ADD . /src
RUN cd /src && go build -o goapp

# final stage
FROM alpine
WORKDIR /app
COPY --from=build-env /src/goapp /app/
ENTRYPOINT ./goapp

docker build -t go-ms -f Dockerfile-multistage .

Здесь размер образа сильно меньше, чем в первом варианте.

docker images
REPOSITORY   TAG        IMAGE ID       CREATED          SIZE
go-ms        latest     4c2973c2ab20   6 seconds ago    9.94MB
go-big       latest     f505a167955e   3 minutes ago    277MB
