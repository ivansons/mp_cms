#!/usr/bin/env bash
echo """
===============================================================
=====           Matterport CMS dev server setup           =====
===============================================================
"""
HOME="/home/vagrant"
MP_CMS_HOME="/mp_cms"
VENV="${HOME}/venv"
PIP_CMD="${VENV}/bin/pip"
PYTHON_CMD="${VENV}/bin/python"

sudo bash -c "echo \"deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main\" > /etc/apt/sources.list.d/pgdg.list"
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add - &> /dev/null
wget --quiet -O - https://deb.nodesource.com/setup_4.x | sudo bash &> /dev/null

sudo rm /etc/apt/apt.conf.d/70debconf
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y \
  build-essential zip unzip fabric ntp htop git-core \
  python-dev python-software-properties python-setuptools \
  postgresql-9.5 nodejs redis-server \
  libffi-dev libssl-dev libpq-dev libjpeg-dev libxml2-dev libxslt-dev

wget --quiet -O - https://www.browserstack.com/browserstack-local/BrowserStackLocal-linux-x64.zip | sudo bash -c "zcat > /usr/local/bin/BrowserStackLocal"

sudo sed -i "/postgres/! s/ peer/ md5/g" /etc/postgresql/9.5/main/pg_hba.conf
sudo service postgresql restart
sudo -u postgres bash -c "psql -c \"CREATE ROLE mp_cms WITH LOGIN CREATEDB PASSWORD 'matterport';\""
PGPASSWORD="matterport" createdb -U mp_cms mp_cms

wget --quiet -O - https://bootstrap.pypa.io/get-pip.py | sudo -H python
sudo -H pip install pyOpenSSL ndg-httpsclient pyasn1
sudo -H pip install -U pip setuptools
sudo -H pip install virtualenv

sudo rm -rf ${VENV}
virtualenv ${VENV}
${PIP_CMD} list --outdated --format=legacy | sed 's/(.*//g' | xargs ${PIP_CMD} install -U
${PIP_CMD} install -r ${MP_CMS_HOME}/requirements/dev.txt

ln -sf ${MP_CMS_HOME}/vagrant/.bashrc ${HOME}/.bashrc
. ${HOME}/.bashrc

${PYTHON_CMD} ${MP_CMS_HOME}/manage.py migrate --noinput

echo """
===============================================================
=====         Matterport CMS dev server is ready!         =====
===============================================================
"""
