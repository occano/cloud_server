#!/bin/bash
DOCKER_IMAGE=occano/cloud-server
#gcloud auth configure-docker

docker build -t $DOCKER_IMAGE .
docker push $DOCKER_IMAGE
ssh enbys@office.occano.io -p 2214 "cd dev/cloud-server && docker-compose pull && docker-compose down && docker-compose up"
