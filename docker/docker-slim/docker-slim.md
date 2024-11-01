# Docker-slim

## Описание.
Данная утилита позволяет сильно уменьшить размер образа.

## Установка.
```
curl -sL https://raw.githubusercontent.com/slimtoolkit/slim/master/scripts/install-slim.sh | sudo -E bash -
```

## Поехали!

Запускаем анализ имиджа go-big с помощью утилиты slim. В момент работы она попросит запустить контейнер на основе этого образа. После запуска контейнера (в другом терминале) жмём ENTER.
```
slim build --http-probe=false --target go-big
docker run go-big
```
