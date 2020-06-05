#!/usr/bin/env bash
pip install django
pip install pillow
pip install matplotlib
pip install numpy
pip install pandas
pip install seaborn
pip install mysqlclient
pip install geopy
pip install geocoder
python manage.py makemigrations
python manage.py migrate
python manage.py runserver