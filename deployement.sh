#!/bin/bash
set -e
set -x

echo "`ss-get hostname`    $(hostname)" >> /etc/hosts
ss-set machine-hn `hostname`
