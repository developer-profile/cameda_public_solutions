# GitLab-Runner

## Описание.
Приложение с открытым исходным кодом, которое выполняет задания конвейерной обработки GitLab CI/CD по инструкциям из специального файла .gitlab-ci.yml. Оно позволяет запускать автоматизированные сборки внутри кластера Managed Service for Kubernetes.

## Установка.
```
export HELM_EXPERIMENTAL_OCI=1 && \
helm pull oci://cr.yandex/yc-marketplace/yandex-cloud/gitlab-org/gitlab-runner/chart/gitlab-runner \
  --version 0.54.0-8 \
  --untar && \
helm install \
  --namespace gitlab \
  --create-namespace \
  --set gitlabDomain=https://xxx.gitlab.yandexcloud.net \
  --set runnerRegistrationToken=glrt-J6rHVwyxUehCC2_jVy7F \
  gitlab-runner ./gitlab-runner/
```

Token получаем в инсталляции GitLab. Для этого: Settings->CI/CD->Runners->Expand->New Project Runner.
Файл .gitlab-ci.yml создаём по пути Code->Repository.
