# Pluto

## Описание.

Приложение для поиска устаревших версий API в helm релизах, репозиториях, кластере k8s.

## Установка в Mac.

```
brew install FairwindsOps/tap/pluto
```

## Сайт проекта.

https://github.com/FairwindsOps/pluto/blob/master/docs/README.md

quickstart: https://github.com/FairwindsOps/pluto/blob/master/docs/quickstart.md

installation: https://github.com/FairwindsOps/pluto/blob/master/docs/installation.md 

## Примеры использования.

```
pluto detect-files -d <DIRECTORY YOU WANT TO SCAN>
pluto detect-helm -owide
pluto detect-all-in-cluster -o wide 2>/dev/null
```
