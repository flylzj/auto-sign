FROM python:3.7-alpine

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
RUN apk add --no-cache --update gcc libc-dev openssl-dev

RUN echo "Asia/Shanghai" > /etc/timezone

WORKDIR /

COPY requirements.txt /req.txt

COPY . /app

RUN pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple -r req.txt

COPY endpoint.sh /endpoint.sh

RUN chmod +x /endpoint.sh

WORKDIR /app

CMD ["python3", "index.py"]

