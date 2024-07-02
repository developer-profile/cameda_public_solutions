# Krew

## Описание.
Данная утилита позволяет устанавливать многочисленные плагины к утилите kubectl.

## Установка krew.
```
(
  set -x; cd "$(mktemp -d)" &&
  OS="$(uname | tr '[:upper:]' '[:lower:]')" &&
  ARCH="$(uname -m | sed -e 's/x86_64/amd64/' -e 's/\(arm\)\(64\)\?.*/\1\2/' -e 's/aarch64$/arm64/')" &&
  KREW="krew-${OS}_${ARCH}" &&
  curl -fsSLO "https://github.com/kubernetes-sigs/krew/releases/latest/download/${KREW}.tar.gz" &&
  tar zxvf "${KREW}.tar.gz" &&
  ./"${KREW}" install krew
)
```
```
export PATH="${KREW_ROOT:-$HOME/.krew}/bin:$PATH"
```

## Полезные ссылки.
* Установка krew: https://krew.sigs.k8s.io/docs/user-guide/setup/install/
* Список плагинов krew: https://krew.sigs.k8s.io/plugins/
