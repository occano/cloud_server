#!/bin/bash
DOCKER_IMAGE=eu.gcr.io/vessel-engine-monitor/cloud-server
gcloud auth configure-docker

docker build -t $DOCKER_IMAGE .
docker push $DOCKER_IMAGE
