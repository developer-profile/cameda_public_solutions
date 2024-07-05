# Kubectl. Редкие команды.

## Открываем доступ к контейнеру извне через форвардинг портов.
```
kubectl port-forward pod_name hostPort:podPort
kubectl port-forward cam-nginx 8080:80
```

## Смена namespace для текущего контекста.
```
kubectl config set-context $(kubectl config current-context) --namespace=dev
```
## Создание дебаг пода с hostPath root хоста.
```
kubectl debug node/mynode -it --image=busybox
```

## Вывод env/date из группы подов.
```
for pod in $(kubectl get po --output=jsonpath={.items..metadata.name}); do echo $pod && kubectl exec -it $pod -- env; done
for pod in $(kubectl get po -oname); do echo $pod && kubectl exec -it $pod -- env; done
for pod in $(kubectl get po -oname); do echo $pod && kubectl exec -it $pod -- date; done
```

## Копируем файл в под и из пода.
```
kubectl cp file my-pod:/mnt/file
kubectl cp my-pod:/mnt/file.txt file.txt
```
