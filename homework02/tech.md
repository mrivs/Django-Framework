## шпаргалка

python -m venv venv
venv\Scripts\activate.ps1 
python.exe -m pip install --upgrade pip
pip install django

django-admin startproject project_hw2
python manage.py startapp myapp

в progect_hw2\settings.py INSTALLED_APPS добавляется  myapp

в файле \project_hw2\project_hw2\urls.py  в urlpatterns указывается путь для приложения myapp

в myapp создается файл urls.py  где  описываются urlpatterns для  views

в файле \project_hw2\myapp\views.py , создаются представления

в файле \project_hw2\myapp\models.py создаются модели


python manage.py makemigrations
python manage.py migrate

