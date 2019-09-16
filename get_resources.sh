#!/bin/bash
SERVICE_NAME=trainer
mkdir -p resources/head_models/
gsutil cp -r -n gs://occano-resources/ds-resources/$SERVICE_NAME/* resources/
gsutil cp -r -n gs://occano-resources/ds-resources/head_models/* resources/head_models/

