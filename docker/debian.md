



# используем тонкий `slim` образ с тегом, указывающим именно на этот образ (цифры 20220822)
FROM debian:bullseye-20220822-slim
# уменьшим количество слоев и тем самым избавимся от временных файлов в образе
RUN apt-get update && apt-get -y install curl && apt-get clean
# удалим инструкцию COPY data/ /data. Вместо этого будем использовать build volume
ENV URL https://httpbin.org/post
# добавим обычного пользователя
RUN useradd -m worker
# оставим только sh, нужный для работы curl
RUN rm -rf /bin/bash && rm -rf /usr/bin/apt && rm -rf /usr/bin/apt-get
# значение токена теперь берем из переменной окружения TOKEN
CMD ["sh", "-c", "curl -d @/data/payload.json -X POST -H \"Content-Type: application/json\" -H \"Token: $TOKEN\" ${URL}"]
USER worker
