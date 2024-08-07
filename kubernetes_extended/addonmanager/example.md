# Addon Manager

## Примеры использования в манифестах.

```
labels:
    addonmanager.kubernetes.io/mode: Reconcile
    k8s-app: kube-dns
    kubernetes.io/name: CoreDNS
---
labels:
    addonmanager.kubernetes.io/mode: Reconcile
    app.kubernetes.io/instance: metrics-server
    app.kubernetes.io/name: metrics-server
    app.kubernetes.io/version: 0.6.1
---
labels:
    addonmanager.kubernetes.io/mode: Reconcile
---
labels:
    addonmanager.kubernetes.io/mode: EnsureExists
    k8s-app: cilium
```
