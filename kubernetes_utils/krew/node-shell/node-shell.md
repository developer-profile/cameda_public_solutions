# Node-shell

## Описание.
Данный плагин предназначен для получения доступа к файловой системе ноды из пода. Монтирует файловую систему root в под.

## Установка.
```
kubectl krew index add kvaps https://github.com/kvaps/krew-index
kubectl krew install kvaps/node-shell
```

## Примеры использования.
```
kubectl node-shell <node> -- echo 123
kubectl node-shell <node>
```

## Полезные ссылки.
GitHUB проекта: https://github.com/kvaps/kubectl-node-shell
