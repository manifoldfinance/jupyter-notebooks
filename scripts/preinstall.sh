#!/usr/bin/env bash
echo "Setting up Virtual Environment"
python3 -m venv ~/venv
source ~/venv/bin/activate
pip3 install -r binder/requirements.txt