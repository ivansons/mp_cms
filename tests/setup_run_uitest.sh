#!/bin/bash

echo """
===============================================================
=====           Matterport CMS Setup For UI Automation    =====
===============================================================
"""
cd $HOME # start from home directory

# remove broken repo
sudo rm /etc/apt/sources.list.d/google.list
sudo rm /etc/apt/sources.list.d/google-chrome.list

# fix a missing key 
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 1397BC53640DB551

# upgrade compiler
sudo add-apt-repository -y ppa:ubuntu-toolchain-r/test
sudo apt-get update
sudo apt-get install python-software-properties
sudo apt-get install gcc-5 g++-5
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 80 --slave /usr/bin/g++ g++ /usr/bin/g++-5
sudo update-alternatives --config gcc

# install nodejs 4
curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -
sudo apt-get install -y nodejs

# setup database
sudo -u postgres sh -c "psql -c \"CREATE ROLE mp_cms WITH LOGIN CREATEDB PASSWORD 'matterport';\""
PGPASSWORD="matterport" createdb -U mp_cms mp_cms

# migrate database and create superuser for tests
cd ~/mp_cms
./venv/bin/python manage.py migrate --settings=project.settings.dev

# Troubleshoot note:  if fail to log into site and read back user name this line is first to check
echo "from django.contrib.auth.models import User;"``"User.objects.create_superuser("``"    'matterport',"``"    'matterport@matterport.com','mP_cm$')" | ./venv/bin/python manage.py shell --settings=project.settings.dev

# install BrowserStackLocal to enable remote browser accessing local server
wget https://www.browserstack.com/browserstack-local/BrowserStackLocal-linux-ia32.zip
unzip BrowserStackLocal-linux-ia32.zip

# start server;  # Troubleshoot note: comment out >/dev/null 2>&1& to see http req/response in terminal
./venv/bin/python manage.py runserver 0.0.0.0:8000 --settings=project.settings.dev  >/dev/null 2>&1 &


# make a connection between remote browser and local box
./BrowserStackLocal NSQXQzYb5Cr2NWyqgYXG &

cd ./tests

# install all dependencies for integration tests
/usr/bin/npm install

# test cases, hostname, configuration
# report location


# run tests
pwd
mv circle_conf.js conf.js  # since package.json has "test" point to protractor conf.js
/usr/bin/npm test

echo """
===============================================================
=====         Matterport CMS UI Automation Test Done!     =====
===============================================================
"""
