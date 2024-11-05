#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
SPEC_DIR="${SCRIPT_DIR}/../biosim_client/api_specs"
LIB_DIR="${SCRIPT_DIR}/../biosim_client/api_clients"

# Generate client1
openapi-generator generate -i ${SPEC_DIR}/simdata.json -g python -o ${LIB_DIR}/simdata

