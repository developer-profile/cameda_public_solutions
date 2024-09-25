# OpenKruise

## Описание.
`OpenKruise`- это проект, созданный под эгидой cncf. Фокусируется на работе с приложениями. В зону интересов проета входят: deployment, upgrade, ops and availability protection.

## Дополнительные абстракции.
* CloneSet. Альтернатива для Deployment;
* Advanced StatefulSet;
* Advanced DaemonSet;
* BroadcastJob;
* Advanced CronJob

## Архитектура.
Вся магия этого решения базируется на CRD.
Сайт проекта: https://openkruise.io/
Arhitecture: https://openkruise.io/docs/core-concepts/architecture

## Возможности решения.
* In place update. Позволяет обновлять имиджи и энвайронмент контейнера, не пересоздавая под.

## Установка OpenKruise.
```
Firstly add openkruise charts repository if you haven't do this.
helm repo add openkruise https://openkruise.github.io/charts/

Upgrade to the latest version.
helm upgrade kruise openkruise/kruise --version 1.5.2 [--force]
helm upgrade kruise openkruise/kruise --install -n kruise --create-namespace
```
