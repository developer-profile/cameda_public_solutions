# Cilium status version 1.12.9

```
kubectl exec -ti cilium-5tlc2 -n kube-system -- cilium status
Defaulted container "cilium-agent" out of: cilium-agent, clean-cilium-state (init), install-cni-binaries (init)
KVStore:                 Ok   Disabled
Kubernetes:              Ok   1.30 (v1.30.1) [linux/amd64]
Kubernetes APIs:         ["cilium/v2::CiliumClusterwideNetworkPolicy", "cilium/v2::CiliumEndpoint", "cilium/v2::CiliumLocalRedirectPolicy", "cilium/v2::CiliumNetworkPolicy", "cilium/v2::CiliumNode", "core/v1::Namespace", "core/v1::Node", "core/v1::Pods", "core/v1::Service", "discovery/v1::EndpointSlice", "networking.k8s.io/v1::NetworkPolicy"]
KubeProxyReplacement:    Strict   [eth0 10.143.0.20]
Host firewall:           Disabled
CNI Chaining:            none
Cilium:                  Ok   1.12.9 (v1.12.9-e0bb30a)
NodeMonitor:             Listening for events on 2 CPUs with 64x4096 of shared memory
Cilium health daemon:    Ok
IPAM:                    IPv4: 108/254 allocated from 10.11.1.0/24,
BandwidthManager:        EDT with BPF [CUBIC] [eth0]
Host Routing:            Legacy
Masquerading:            IPTables [IPv4: Enabled, IPv6: Disabled]
Controller Status:       443/443 healthy
Proxy Status:            OK, ip 10.11.1.101, 0 redirects active on ports 10000-20000
Global Identity Range:   min 256, max 65535
Hubble:                  Ok   Current/Max Flows: 4095/4095 (100.00%), Flows/s: 14.85   Metrics: Ok
Encryption:              Disabled
Cluster health:          4/4 reachable   (2024-09-25T09:52:20Z)
```

Для большего вывода можно использовать ключ --verbose.
```
kubectl exec -ti cilium-5tlc2 -n kube-system -- cilium status --verbose
```
