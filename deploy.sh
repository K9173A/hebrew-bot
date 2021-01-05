#!/bin/bash

if [[ -d venv ]]; then
  rm -rf venv
fi

virtualenv -p $(which python3) venv
source ./venv/bin/activate
pip install -r requirements.txt

python -m src.bot