#!/bin/sh

# Note: this script is intended to use the meltano command without a python virtual environment.
# docker run --env-file .env.example --user $(id -u):$(id -g) -v $(pwd):/projects -w /projects meltano/meltano "$@"
docker-compose exec --user $(id -u):$(id -g) -w /code meltano-pipeline meltano "$@"
