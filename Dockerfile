FROM python:3

RUN apt update && \
	apt upgrade -y && \
	apt install -y protobuf-compiler

COPY . /opt

CMD bash
