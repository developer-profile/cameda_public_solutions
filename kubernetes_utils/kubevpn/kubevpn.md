# KubeVPN

## Описание.
VPN для подключения к внутренним ресурсам кластера k8s. Рабочая машина получает адрес из подсети подов.

## Установка.
```
kubectl krew index add kubevpn https://github.com/kubenetworks/kubevpn.git
kubectl krew install kubevpn/kubevpn
```

## Подключение.
``` 
kubectl kubevpn connect
В графе пароль вводим пароль от своего пользователя. У которого есть права sudo на машину.
Ждём когда соединение будет установлено.
```

### Проверим соединение.
```
kubectl kubevpn status
ID Mode Cluster                             Kubeconfig                 Namespace Status
0  full yc-managed-k8s-catat0kjnkbivtbdu98n /Users/cameda/.kube/config default   Connected
```

### Примеры.
```
curl 10.11.1.15
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>

ping 10.11.2.149
PING 10.11.2.149 (10.11.2.149): 56 data bytes
64 bytes from 10.11.2.149: icmp_seq=0 ttl=64 time=9.634 ms
```

### Разрываем соединение.
```
kubectl kubevpn disconnect --all=true
```

## Полезные ссылки.
https://github.com/kubenetworks/kubevpn
