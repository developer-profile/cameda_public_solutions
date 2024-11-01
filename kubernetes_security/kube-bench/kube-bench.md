# Kube-bench

## Описание.
Инструмент от Aqua Security для оценки защищённости кластера Kubernetes. Помимо описания проблем есть и рекомендации по их устранению.

## Установка.
```
curl -L https://github.com/aquasecurity/kube-bench/releases/download/v0.7.0/kube-bench_0.7.0_linux_amd64.tar.gz -o kube-bench_0.7.0_linux_amd64.tar.gz
tar -xvf kube-bench_0.7.0_linux_amd64.tar.gz
```

## Использование.
```
./kube-bench --config-dir `pwd`/cfg --config `pwd`/cfg/config.yaml
kube-bench > 1.txt
```

