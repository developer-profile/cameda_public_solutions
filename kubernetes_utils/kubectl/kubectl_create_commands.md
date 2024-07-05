# Kubectl. Создание ресурсов и добавление мета информации.

## Запускаем какой-то манифест.
```
cat <<<EOF | kubectl apply -f -
...
EOF
```

## Создание ресурсов.
```
kubectl run nginx --image=nginx
kubectl run httpd --image=httpd:alpine --port=80 --expose # создаём под и сервис
kubectl run --restart=Never --image=busybox:1.28.4 static-busybox --dry-run=client -o yaml --command — sleep 1000 > manifest.yaml

kubectl create deployment nginx --image=nginx:latest # создаём деплоймент
kubectl create secret generic cam-secret --from-literal=cameda=goodPa$word # создаём секрет
kubectl create cm nginx-config --from-file /etc/nginx/site-available/default
kubectl create sa cameda-sa
kubectl create ns prod
```

## Добавление меток и аннотаций.
```
kubectl label no cl1k0lmd1e01fb8jfc48-ofit cam=taint
kubectl label no cl1k0lmd1e01fb8jfc48-ofit cam-

kubectl annotate no cl1k0lmd1e01fb8jfc48-ofit author=cameda
kubectl annotate no cl1k0lmd1e01fb8jfc48-ofit author-

kubectl label po nginx cam=taint
kubectl label po nginx cam-

kubectl annotate po nginx author=cameda
kubectl annotate po nginx author-
```


