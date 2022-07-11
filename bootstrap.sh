#!/usr/bin/env bash
set -euo pipefail
#PYTHON=venv/bin/python
#PYTHON_BIN=venv/bin

if ! [ -d venv ]; then
  mkdir -p venv
  virtualenv -p "$(which python3)" venv
  # shellcheck disable=SC1091
   source venv/bin/activate
#  python3 -m pip install --ignore-installed -r requirements.txt
pip3 install -r requirements.txt

python3 -m ipykernel install --user --name python-cadlabs-eth-model --display-name "Python (NOTEBOOKS)"
jupyter notebook
exit 0
fi
# shellcheck disable=SC1091
source venv/bin/activate

echo "Installing requirements..."
pip3 install -r requirements.txt

python3 -m ipykernel install --user --name python-cadlabs-eth-model --display-name "Python (NOTEBOOKS)"
sleep 1

jupyter notebook

exit 0
