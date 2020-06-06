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
echo "Performing system checks..."

echo "System check identified no issues (0 silenced)."
echo "June 06, 2020 - 09:39:26"
echo "Django version 3.0.1, using settings 'OnlineParkingSystem.settings"
echo "Starting development server at http://127.0.0.1:8000/"
python manage.py runserver
echo ""
cls
clear
echo ""
echo ""
echo "Any Key To Exit"
read d
