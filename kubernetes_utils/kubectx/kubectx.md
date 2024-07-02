# Kubectx

## Описание.
Утилита предназначена для быстрого переключения между контекстами в кластере Kubernetes.

## Установка.
```
wget https://raw.githubusercontent.com/ahmetb/kubectx/master/kubectx
chmod +x kubectx
sudo mv kubectx /usr/local/bin
```

## Пример команд.
```
kubectx yc-cam-cillium # По дефолту подключаемся к кластеру yc-cam-cillium
kubectx -d yc-cam-test1 # Удаляем контекст yc-cam-test1
```
