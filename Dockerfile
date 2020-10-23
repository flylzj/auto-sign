FROM python:3.7-alpine

WORKDIR /

COPY requirements.txt /req.txt

COPY . /app

RUN pip -r install req.txt

COPY endpoint.sh /endpoint.sh

WORKDIR /app

ENTRYPOINT ["/endpoint.sh"]

