# Здесь собираются статьи про лучшие практики в работе с Kubernetes.

## Лучшие практики Kubernetes. 

* Создание небольших контейнеров.
Здесь рассказывается про практики, позволяющие уменьшить размер имиджа. Например, использование Alpine.
https://habr.com/ru/companies/ua-hosting/articles/502052/

* Организация Kubernetes с пространством имен.
Про практики использования namespace в Kubernetes. 
https://habr.com/ru/companies/ua-hosting/articles/502320/

* Настройка запросов и лимитов ресурсов.
Про необходимость установки ресурсов в подах. ResourceQuota. LimitRange.
https://habr.com/ru/companies/ua-hosting/articles/502614/

* Проверка жизнеспособности Kubernetes с помощью тестов Readiness и Liveness.
Про необходимость задавать пробы.
https://habr.com/ru/companies/ua-hosting/articles/502430/

* Корректное отключение Terminate.
Про необходимость заложить в приложение корректную отработку SIGTERM.
И про terminationGracePeriodSeconds.
https://habr.com/ru/companies/ua-hosting/articles/503488/

* Маппинг внешних сервисов.
Про плюсы от использования внешних сервисов при работе с рсурсами извне кластера.
https://habr.com/ru/companies/ua-hosting/articles/503612/

## Перестаньте использовать лимиты на cpu.
https://home.robusta.dev/blog/stop-using-cpu-limits

## Набор старых рекомендаций от Фланта.

1. Защита внутреннего контура с помощью инструментов ingress-nginx (basic-auth).
2. Использование OpenVPN внутри кластера для доступа к его внутренним ресурсам с помощью VPN.

https://habr.com/ru/companies/flant/articles/427745/

------------------------------------------------------------------------------------------------
## Архитектура kubelet.
https://www.sobyte.net/post/2022-03/kubelet-pod-creation-workflow/
