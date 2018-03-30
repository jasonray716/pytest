# Django demo app for interview

[![Build Status: Linux](https://travis-ci.org/trevordonnelly/pytest.svg?branch=master)](https://travis-ci.org/trevordonnelly/pytest)


## Environment Setup

First you will need to install python package manager `pip`
```
sudo apt-get update
sudo apt-get install python3-pip python-dev
source /pass/to/virtualenv/bin/activate
```

## Run webserver
The next step is to clone the repository and install python packages.
```
git clone https://github.com/trevordonnelly/pytest.git
cd pytest
pip install -r requirements.txt
```
Then migrate database and run server.
```
python manage.py migrate
python manage.py runserver
```
