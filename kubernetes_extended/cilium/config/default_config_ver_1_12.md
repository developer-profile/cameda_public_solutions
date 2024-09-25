# Дефолтный конфиг cilium для версии 1.12.9

```
data:
  auto-direct-node-routes: "false"
  bpf-lb-map-max: "65536"
  bpf-map-dynamic-size-ratio: "0.0025"
  bpf-policy-map-max: "16384"
  cilium-endpoint-gc-interval: 5m0s
  cluster-name: default
  debug: "false"
  enable-auto-protect-node-port-range: "true"
  enable-bandwidth-manager: "true"
  enable-bpf-clock-probe: "true"
  enable-bpf-masquerade: "false"
  enable-endpoint-routes: "false"
  enable-health-check-nodeport: "true"
  enable-health-checking: "true"
  enable-host-firewall: "false"
  enable-hubble: "true"
  enable-ip-masq-agent: "false"
  enable-ipv4: "true"
  enable-ipv6: "false"
  enable-l7-proxy: "true"
  enable-local-node-route: "true"
  enable-local-redirect-policy: "true"
  enable-metrics: "true"
  enable-policy: default
  enable-remote-node-identity: "true"
  enable-session-affinity: "true"
  enable-well-known-identities: "false"
  enable-xt-socket-fallback: "true"
  hubble-disable-tls: "false"
  hubble-listen-address: :4244
  hubble-metrics: dns drop tcp flow icmp http port-distribution
  hubble-metrics-server: :9091
  hubble-socket-path: /var/run/cilium/hubble.sock
  hubble-tls-cert-file: /var/lib/cilium/tls/hubble/server.crt
  hubble-tls-client-ca-files: /var/lib/cilium/tls/hubble/client-ca.crt
  hubble-tls-key-file: /var/lib/cilium/tls/hubble/server.key
  identity-allocation-mode: crd
  install-iptables-rules: "true"
  ipam: kubernetes
  k8s-api-server: https://10.143.0.4
  k8s-require-ipv4-pod-cidr: "true"
  k8s-require-ipv6-pod-cidr: "false"
  kube-proxy-replacement: strict
  kube-proxy-replacement-healthz-bind-address: :10256
  masquerade: "false"
  monitor-aggregation: medium
  monitor-aggregation-flags: all
  monitor-aggregation-interval: 5s
  node-port-bind-protection: "true"
  operator-api-serve-addr: 127.0.0.1:9234
  operator-prometheus-serve-addr: :6942
  preallocate-bpf-maps: "false"
  prometheus-serve-addr: :9090
  proxy-prometheus-port: "9095"
  sidecar-istio-proxy-image: cilium/istio_proxy
  tunnel: vxlan
  wait-bpf-mount: "false"
kind: ConfigMap
```
