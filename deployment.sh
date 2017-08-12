  #!/bin/bash
set -e
set -x


_ss_set_hostname() {
  echo "`ss-get hostname`    $(hostname)" >> /etc/hosts
  ss-set machine-hn `hostname`
}

_instal_server_module() {
  pip install Flask
  pip install boto
  pip install requests
}

_install_python_APIs() {
  pip install slipstream-api
  pip install elasticsearch
}

 _ss_set_hostname
 _install_python_APIs
_instal_server_module

cd ~/SAR_framework/
python server3.py
