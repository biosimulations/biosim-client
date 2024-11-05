#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
SPEC_DIR="${SCRIPT_DIR}/../biosim_client/api_specs"
LIB_DIR="${SCRIPT_DIR}/../biosim_client/api_clients"

# Generate simdata-api client
# TODO: need to customize the package name
# TODO: improve Python typing for Mypy
# TODO: make attributes dictionaries - easier to work with
openapi-generator generate -i ${SPEC_DIR}/simdata.json -g python -o ${LIB_DIR}/simdata

