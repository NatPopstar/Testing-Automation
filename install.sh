#!/bin/bash
mkdir environments
cd environments
python3 -m venv selenium_env
cd ..
source environments/selenium_env/bin/activate
pip install -r requirements.txt
ln -s ../../../chromedriver environments/selenium_env/bin/chromedriver
