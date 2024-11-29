# Python + Flask

## Создаём имидж.
```
FROM python:3.8
RUN pip install flask
COPY . /opt/
EXPOSE 8080
WORKDIR /opt
ENTRYPOINT ["python3", "app.py"]
```
```
docker build -t pyflask -f Dockerfile .
```
