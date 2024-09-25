# Helm commands

## Работа с репозиторием.
```
helm repo add <repo_name> <repo_address>
helm repo update
helm repo list
helm repo remove <repo_name>
```

## Скачать чарт, поправить файл values и установить релиз со значениями из values.
```
export HELM_EXPERIMENTAL_OCI=1 && \
helm pull <address> \
  --version <chart version> \
  --untar
```
```
helm upgrade <release-name> --install --atomic --namespace <name> --create-namespace ./<directory>/
```
## Поиск чарта в репозитории.
```
helm search repo <chart_name>
helm search repo <chart_name> --versions # Все версии чарта 
helm search hub <chart_name> # Поиск чарта в Artifact Hub
```

## Установка релиза.
```
helm install <release_name> <chart_name> -n <namespace>
helm upgrade --install <release_name> <chart_name> -n <namespace> --create-namespace
```

## Просмотр информации об установленных релизах.
```
helm list -A
```

## Удаление релиза.
```
helm uninstall <release_name> -n <namespace>
```

# Examples.
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
helm repo list
helm search repo grafana/grafana
helm install my-grafana grafana/grafana --namespace monitoring
helm pull traefik/traefik --version 26.1.0 --untar
