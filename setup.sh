#!/usr/bin/env bash
echo "before starting make sure python -3 have been installed"
echo "path also have bin set to enviroment"
echo "Do you have required Pakages ? Y/N"
read a
if [ $a == "N" ]
then
pip install django
pip install pillow
pip install matplotlib
pip install numpy
pip install pandas
pip install seaborn
pip install mysqlclient
pip install geopy
pip install geocoder
pip install ipywidgets
cls
clear
fi
cd OnlineParkingSystem
python manage.py makemigrations
python manage.py migrate
cls
clear
python manage.py runserver
cls
echo "any key to left"
read d