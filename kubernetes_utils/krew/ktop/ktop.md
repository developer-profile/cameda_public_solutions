# ktop

<h1 align="center">
    <img src="./ktop.png" alt="ktop">
</h1>

## Описание.
`ktop`- инструмент, похожий визуально на htop. Можно использовать для анализа загрузки нод кластера. 

### Показывает.
* Количество нод в кластере;
* Версию Kubernetes;
* Адрес API Server;
* Версию ОС:
* Количество подов и имиджей на нодах;
* Сколько ram/cpu занимают поды на нодах;
* Сколько всего pod/deployment/namespace/sts/ds/jobs в кластере;
* Контекст и имя пользователя;
* Сколько ресурсов занимает каждый под.

## Установка.
```
kubectl krew search ktop
kubectl krew install ktop
```

## Пример использования.
```
kubectl ktop --namespace my-app --context web-cluster
kubectl ktop

Выход - Esc.
```
