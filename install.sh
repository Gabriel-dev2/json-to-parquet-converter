#!/bin/bash

echo "Installing pip..."
echo "-------------------------------------------------"
python -m install pip
echo "pip installed successfully"
echo "-------------------------------------------------"
echo "Installing pipenv..."
pip install pipenv
echo "pipenv installed successfully"
echo "-------------------------------------------------"
echo "Adding pipenv to PATH..."
export PATH=$PATH/root/.local/bin
export PATH=$PATH/root/.local/bin/pipenv
echo $PATH
echo "Added pipenv to PATH..."
echo "-------------------------------------------------"
echo "Installing dependencies..."
pipenv install --dev
echo "Installed successfully"
echo "-------------------------------------------------"