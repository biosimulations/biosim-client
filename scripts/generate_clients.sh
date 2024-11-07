#!/bin/bash

ROOT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && cd .. && pwd )"

# make a clean ROOT_DIR without .. (hint, use dirname or something like that)
SPEC_DIR="${ROOT_DIR}/biosim_client/api_specs"
LIB_DIR="${ROOT_DIR}"
PACKAGE="biosim_client.simdata_api"

# Generate simdata-api client
# TODO: improve Python typing for Mypy
# TODO: make attributes dictionaries - easier to work with
openapi-generator generate -i "${SPEC_DIR}/simdata.json" -g python -o "${LIB_DIR}" --additional-properties=packageName=${PACKAGE},generateSourceCodeOnly=true

