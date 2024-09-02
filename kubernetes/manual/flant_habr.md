# Статьи компании Флант на Хабр

## Kubernetes 1.30. Что нового?
https://habr.com/ru/companies/flant/articles/808055/

## Внутреннее устройство Kubernetes-кластера простым языком.
https://habr.com/ru/companies/flant/articles/583660/

## Сравнение ingress контроллеров.
Сравниваются между собой: ingress-nginx, nginx-ingress, istio, contour, haproxy, traefik, kong, ambassador.

1. Какие протоколы поддерживаются;
2. Есть ли поддержка JWT;
3. Алгоритмы балансировки;
4. Способы аутентификации;
5. Способы распределения трафика (canary, blue-green, etc);
6. Базовая ddos защита;
7. WAF;
8. Графический интерфейс.

Ingress nginx - норм по функционалу;
Istio - самые богатые возможности.

https://habr.com/ru/companies/flant/articles/447180/

## Так что же такое pod в Kubernetes?
https://habr.com/ru/companies/flant/articles/427819/
Довольно старая статья 2018 года.

## Жизнь пода.
Про статусы пода.
https://habr.com/ru/companies/flant/articles/415393/

## Про обеспечение высокой доступности мастеров.
Перед мастерами стоит LB. В момент времени есть только 1 ведущий и ведомые у: Scheduler, Controller Manager.

https://habr.com/ru/companies/flant/articles/427283/

## Kubernetes — это как океанариум.
Сравниваем работу k8s с океанариума. На примере сущностей кубера и рыбок.

https://habr.com/ru/companies/flant/articles/544306/
