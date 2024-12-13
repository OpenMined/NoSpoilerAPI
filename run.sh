#!/bin/sh

set -e

if [ ! -d .venv ]; then
  uv venv
fi

. .venv/bin/activate

uv pip install --upgrade syftbox 
uv pip install git+https://github.com/OpenMined/syftbox-sdk.git

echo "Running 'dont_spoiler' with $(python3 --version) at '$(which python3)'"
python3 main.py

deactivate
