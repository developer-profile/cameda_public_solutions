# Kubectl

## Описание.
CLI утилита для взаимодействия с API Kubernetes.

## Info commands.

### Просмотр информации по Pod, Deployment, DaemonSet, etc. И во всех namespace.
```
kubectl get po
kubectl get po -A

kubectl get deploy
kubectl get deploy -A

kubectl get ds
kubectl get ds -A

kubectl get svc
kubectl get svc -A

kubectl get sts
kubectl get sts -A

kubectl get ing
kubectl get ing -A

kubectl gey pc
kubectl get pdb
kubectl get quota
kubectl get limits
kubectl get np
```

### Просмотр информации по всем ресурсам в namespace. И во всех namespace.
```
kubectl get all
kubectl get all -A
```

## Общие команды.
```
kubectl api-versions
kubectl api-resources
kubectl version
kubectl cluster-info
kubectl explain po
kubectl explain deploy
kubectl explain ds
kubectl explain sts
```

## Работа с подами.
```
kubectl run nginx --image=nginx
kubectl expose po nginx --port 80
kubectl set image po nginx nginx=nginx:alpine

kubectl run httpd --image=httpd:alpine --port=80 --expose # создаём под и сервис
kubectl run --restart=Never --image=busybox:1.28.4 static-busybox --dry-run=client -o yaml --command — sleep 1000 > static-busybox.yaml

kubectl get po -owide
kubectl get po -oyaml
kubectl get po -ojson
kubectl get po -oname
kubectl get po -owide -A
kubectl get po --no-headers=true

kubectl get po --show-labels
kubectl get po -owide -w # Смотрим на поды в режиме watch.
kubectl get po -owide --sort-by='.metadata.creationTimestamp'

kubectl describe po nginx -n default
kubectl get po nginx -n default -oyaml
kubectl logs nginx -n default
kubectl top po
kubectl get po --show-labels
kubectl get po -owide -w # Смотрим на поды в режиме watch.
kubectl get po -owide --sort-by='.metadata.creationTimestamp'

kubectl exec -ti -n default nginx -- bash
```

## Работа с нодами.
```
kubectl get no
kubectl get no -owide
kubectl describe no <nodeName>
kubectl describe no <nodeName>

kubectl drain <nodeName> --ignore-daemonsets=true --force --grace-period=0
kubectl cordon <nodeName>
kubectl uncordon <nodeName>

kubectl taint nodes <nodeName> cam=test:NoSchedule
kubectl taint nodes <nodeName> cam=test:NoSchedule-
kubectl taint nodes <nodeName> cam=test:NoExecute
kubectl taint nodes <nodeName> cam=test:NoExecute-
```

## Работа с Deployment.
```
kubectl create deploy cam-nginx --image=nginx:latest
kubectl scale deploy cam-nginx --replicas=2 #увеличиваем кол-во реплик до двух
kubectl expose deploy cam-nginx --type=LoadBalancer --port=80 #создаём для него Service типа LB  с открытым портом 80.
kubectl set image deploy cam-nginx nginx=nginx:1.23

kubectl rollout history
kubectl rollout undo deploy cam-nginx
kubectl rollout undo deploy cam-nginx --to-revision=1
```
