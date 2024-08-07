# Addon Manager

## Описание.
Аддон, отслеживающий состояние компонентов и позволяющий привести их к ожидаемому состоянию.
Работает на мастере кубера.

## Следит за компонентами.

```
    core/v1/ConfigMap
    core/v1/Endpoints
    core/v1/Namespace
    core/v1/PersistentVolumeClaim
    core/v1/PersistentVolume
    core/v1/Pod
    core/v1/ReplicationController
    core/v1/Secret
    core/v1/Service
    batch/v1/Job
    batch/v1/CronJob
    apps/v1/DaemonSet
    apps/v1/Deployment
    apps/v1/ReplicaSet
    apps/v1/StatefulSet
    networking.k8s.io/v1/Ingress
```
## Задачи, которые выполняет.

* Проверяет объекты из списка выше раз в 60 секунд, на предмет их изменений;
* Используется для приведения объектов за которыми следит к первоначальному состоянию. В случае использования политики Reconcile.

## Особенности.

* Работает в бесконечном цикле;
* Следит за объектами у которых установлен label: addonmanager.kubernetes.io/mode:
* Устанавливается в директорию аддонов: /etc/kubernetes/addons
* Ставится по-умолчанию в kube-system;
* Написан на bash.

## Начинает следить за объектом если добавить в label одну из двух меток.

* addonmanager.kubernetes.io/mode=Reconcile
* addonmanager.kubernetes.io/mode=EnsureExists

В первом случае приводит к заданному шаблону настройки ресурсов.
Во втором случае просто проверяет наличие ресурсов. 

## Полезные ссылки.
https://github.com/kubernetes/kubernetes/tree/master/cluster/addons/addon-manager
