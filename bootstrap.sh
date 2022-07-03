#!/usr/bin/env bash
python3 -m venv venv
source venv/bin/activate

echo "Installing requirements..."
pip3 install -r requirements.txt

python3 -m ipykernel install --user --name python-cadlabs-eth-model --display-name "Python (CURRENTS)"
sleep 1
jupyter notebook