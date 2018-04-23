git checkout ssh://git@github.com:jnguyen1195/experiment.git

sudo pip install virtualenv
virtualenv venv
cd venv/

source bin/activate
pip install pip --upgrade
pip install django
pip install djangorestframework
pip install django-cors-headers
