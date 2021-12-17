# to build this docker image (any time do.py changes): 
#   docker build --user $(id -u):$(id -g) --tag onex-build-env:latest .
#
# to build all artifacts this docker image: 
#   docker run -it --rm --user $(id -u):$(id -g) -v $PWD:/tmp onex-build-env:latest bash -c "source /onex/.env/bin/activate && cd /tmp && python3 generate.py"
# to run tests with this docker image:
#   docker run -it --rm --user $(id -u):$(id -g) -v $PWD:/tmp onex-build-env:latest bash -c "source /onex/.env/bin/activate && cd /tmp && python3 do.py test"

# to build pypi packages
#   docker run -it --rm --user $(id -u):$(id -g) -v $PWD:/tmp onex-build-env:latest bash -c "source /onex/.env/bin/activate && cd /tmp && python3 do.py dist"

FROM ubuntu:latest

WORKDIR /onex

RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt install -y curl
RUN apt install -y unzip
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash
RUN apt-get install nodejs
RUN npm install redoc-cli -g

ENV PATH="${PATH}:/root/go/bin:/root/go/go/bin"

COPY do.py setup/

RUN python3 setup/do.py setup_ext
RUN python3 setup/do.py setup
RUN python3 setup/do.py init

