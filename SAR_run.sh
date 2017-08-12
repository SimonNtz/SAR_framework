#!/bin/bash

set -o pipefail

# Bash script launching the the SlipStream application.
# The parameters are the cloud service choosed by the client
# and its Github repository (optional) following the SAR_proc model at
# https://github.com/SimonNtz/SAR_proc.
# Input data is stored in file list "product_list.cfg".

# Connector instance name as defined on https://nuv.la for which user has
# provided credentials in its profile.


SS_ENDPOINT=https://nuv.la

python -u `which ss-execute` \
    --endpoint $SS_ENDPOINT \
    --wait 60 \
    --keep-running="never" \
    --parameters="
    $SLIPSTREAM_USERNAME,
    $SLIPSTREAM_PASSWORD"
    EO_Sentinel_1/ELK-server
