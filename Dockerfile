FROM python:rc-slim
WORKDIR /usr/src/app
RUN set -ex && apt-get update
COPY . /usr/src/app
ENTRYPOINT ["python"]
CMD ["start_server.py"]
