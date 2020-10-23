FROM python:3.7-alpine

WORKDIR /

COPY requirements.txt /req.txt

COPY . /app

RUN pip install -r req.txt

COPY endpoint.sh /endpoint.sh

RUN chmod +x /endpoint.sh

WORKDIR /app

ENTRYPOINT ["/endpoint.sh"]

