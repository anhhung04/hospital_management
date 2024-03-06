#! /bin/sh
pip3 install virtualenv
virtualenv hostpital_management_backend
source hostpital_management_backend/bin/activate
pip3 install -r requirements.txt