FROM python:3-slim

WORKDIR /tests
COPY . /tests/

RUN pip3 install -U pip wheel
RUN pip3 install -r requirements.txt

CMD nose2
