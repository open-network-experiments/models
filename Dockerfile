# to build this docker image (any time do.py changes): docker build --tag onex-build-env:latest .
# additional flags: https://docs.docker.com/engine/reference/commandline/build/

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

# to run: docker run -it --rm -v $PWD:/tmp onex-build-env:latest bash -c "source /onex/.env/bin/activate && cd /tmp && python3 generate.py"