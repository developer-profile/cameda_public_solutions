# Helm example

## Описание.
Здесь даётся пример по:

*  созданию своего чарта;
*  различным проверкам чарта; 
*  пушу чарта в реджистри;
*  скачиванию чарта из реджистри;
*  распаковке и инсталляции релиза на основе данного чарта;
*  просмотру установленных релизов;
*  апгрейду ревизии у релиза;
*  удалению релиза.

## Поехали!

### Создадим свой чарт.
```
helm create alpine_curl
```

После этого удаляем всё содержимое из директории templates. И всё содержимое файла values.yaml.

Далее в templates создаём две сущности: Deployment, PriorityClass.

Файл values.yaml приводим к виду:
```
# Deployment
deployment:
  imagePullPolicy: IfNotPresent
  restartPolicy: OnFailure
  port: 80

# PriorityClass
priorityClass:
  value: 10
```
В соответствующих местах сущностей Deployment, PriorityClass проставляем переменные в стиле {{.Values.xxxx.xxxx}}, например, imagePullPolicy в Deployment будет определяться так:
imagePullPolicy: {{.Values.deployment.imagePullPolicy}}

### Проверим чарт.

* Выполняем из той же директории где лежит файл Chart.yaml. Команда покажет все сущности с уже подставленными значениями.
```
helm template .
```

* Простенький линтер. Помогает найти явные ошибки в логике и нарушения RFC. Ничего сверх.
```
helm lint .
```

### Регаемся в реджистри.
helm registry login cr.yandex -u iam
