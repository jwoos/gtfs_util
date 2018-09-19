FROM python:3

RUN apt update && \
	apt upgrade -y && \
	apt install -y protobuf-compiler

COPY . /opt

WORKDIR /opt

RUN pip install -r requirements.txt

CMD bash
