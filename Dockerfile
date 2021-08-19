FROM --platform=linux/amd64 python:3.9.6-slim
RUN apt-get update && apt-get upgrade -y
WORKDIR /postgres-pubsub
COPY . .
RUN pip install psycopg2-binary=="2.9.1" wait-for-it=="2.2.0"

ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["python"]
