FROM python:3.7-alpine

WORKDIR /

COPY requirements.txt /req.txt

COPY . /app

RUN pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple -r req.txt

COPY endpoint.sh /endpoint.sh

RUN chmod +x /endpoint.sh

WORKDIR /app

ENTRYPOINT ["/endpoint.sh"]

