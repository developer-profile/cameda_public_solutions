# Trivy

## Описание.
Утилита для сканирования образов на предмет наличия уязвимостей.

## Установка.
```
apt -y update
apt -y install wget apt-transport-https gnupg lsb-release
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | sudo tee -a /etc/apt/sources.list.d/trivy.list

#Update Repo and Install trivy
apt -y update
apt -y install trivy
```

## Использование.
```
trivy image --severity HIGH  --output /root/python.txt python:3.10.0a4-alpine
trivy image nginx
trivy image --input alpine.tar --format json --output /root/alpine.json
```

## Полезные ссылки.

https://www.aquasec.com/products/trivy/
