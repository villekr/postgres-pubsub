FROM python:3.8.1-slim
RUN apt-get update && apt-get upgrade -y
WORKDIR /postgres-pubsub
COPY . .
RUN pip install psycopg2-binary=="2.8.6"

ENTRYPOINT ["python"]
