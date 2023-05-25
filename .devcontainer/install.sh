#!/bin/bash
python3 -m pip install --upgrade pip setuptools wheel build twine
python3 -m pip install --user pipenv
pip3 install --user -r .devcontainer/requirements.txt