FROM python:3-slim

RUN apt update && apt upgrade -y && apt install -y curl && rm -rf /var/cache/apt/*

WORKDIR /service
COPY app /service/app
COPY requirements.txt /service/

RUN pip3 install -U pip wheel
RUN pip3 install -r requirements.txt

CMD flask run
