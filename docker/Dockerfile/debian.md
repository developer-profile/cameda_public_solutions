# Debian

```
FROM debian:bullseye-20220822-slim
RUN apt-get update && apt-get -y install curl && apt-get clean
ENV URL https://httpbin.org/post
RUN useradd -m worker
RUN rm -rf /bin/bash && rm -rf /usr/bin/apt && rm -rf /usr/bin/apt-get
CMD ["sh", "-c", "curl -d @/data/payload.json -X POST -H \"Content-Type: application/json\" -H \"Token: $TOKEN\" ${URL}"]
USER worker
```
