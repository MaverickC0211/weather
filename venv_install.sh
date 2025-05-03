#/bin/bash

# install python virtual env
sudo apt install python3-venv 

# create a virtual environment
python3 -m venv venv 

# activate the virtual env
source venv/bin/activate 

# within the virtual env, install packages 
pip install flask
