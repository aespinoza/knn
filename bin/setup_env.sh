#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

python3.8 -m venv venv
source venv/bin/activate
pip install pip setuptools --upgrade
pip install -r requirements.dev.txt
pip install -r requirements.txt

deactivate
