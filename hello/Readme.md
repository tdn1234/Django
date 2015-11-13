***Installation instructions**
**Please follow these step below**
**install pip tool for python**
sudo apt-get install python-pip

sudo apt-get install fabric

sudo pip install virtualenv

mkdir django

cd django

virtualenv django

source django/bin/activate

pip install Django==1.7
**install postgresql**

sudo apt-get install libpq-dev python-dev

sudo apt-get install postgresql postgresql-contrib

**start working with postgre **
sudo su - postgres
**create new database named assignment**
createdb assignment
**Now create your database user named djangon with the following command**
createuser -P django

GRANT ALL PRIVILEGES ON DATABASE assignment TO django

**In order for Django to be able to talk to our database we need to install a backend for Postgresql**
pip install psycopg2

sudo apt-get install ruby
sudo apt-get install ruby-dev

sudo apt-get install nodejs
sudo apt-get install npm
sudo ln -s /usr/bin/nodejs /usr/bin/node

npm install
sudo npm install -g grunt-cli
sudo apt-get install fontforge ttfautohint 


gem install sass
gem install compass

pip install coverage

pip install django-nose

pip install flake8==2.1.0
pip install flake8-import-order==0.5.1

sudo apt-get install libjpeg-dev zlib1g-dev libpng12-dev

pip install pillow


django-admin.py startproject hello

cd hello/

python manage.py migrate
python manage.py createsuperuser

python manage.py runserver




