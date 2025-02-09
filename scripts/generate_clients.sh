#!/bin/bash

ROOT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && cd .. && pwd )"

#generatorCliImage=openapitools/openapi-generator-cli:v7.1.0

# make a clean ROOT_DIR without .. (hint, use dirname or something like that)
SPEC_DIR="${ROOT_DIR}/biosim_client/api/api_specs"
LIB_DIR="${ROOT_DIR}"

# Generate simdata-api client
# TODO: improve Python typing for Mypy
# TODO: make attributes dictionaries - easier to work with
PACKAGE="biosim_client.api.simdata"
openapi-generator generate -i "${SPEC_DIR}/simdata.json" -g python -o "${LIB_DIR}" --additional-properties=packageName=${PACKAGE},generateSourceCodeOnly=true

# Generate biosim-api client
# TODO: improve Python typing for Mypy
PACKAGE="biosim_client.api.biosim"
openapi-generator generate -i "${SPEC_DIR}/biosim.yaml" -g python -o "${LIB_DIR}" --additional-properties=packageName=${PACKAGE},generateSourceCodeOnly=true
