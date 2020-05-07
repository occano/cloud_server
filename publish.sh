#!/bin/bash
DOCKER_IMAGE=occano/cloud-server
#gcloud auth configure-docker

docker build -t $DOCKER_IMAGE .
docker push $DOCKER_IMAGE
docker-compose down
docker-compose up
