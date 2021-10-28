FROM ubuntu:latest

WORKDIR /onex

RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt install -y curl
RUN apt install -y unzip

ENV PATH="${PATH}:/root/go/bin:/root/go/go/bin"

COPY do.py setup/

RUN python3 setup/do.py setup_ext
RUN python3 setup/do.py setup
RUN python3 setup/do.py init

# usage:
# docker run -it --rm -v $PWD:/onex onex-model-build python3 do.py generate