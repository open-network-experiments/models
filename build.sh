#!/bin/bash
docker build -t onex-build-env -f Dockerfile .
docker run -it --rm -v $PWD:/tmp onex-build-env:latest bash -c "source /onex/.env/bin/activate && cd /tmp && python3 generate.py"