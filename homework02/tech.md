## шпаргалка
создание  и активация виртуального окружения

    python -m venv venv
    venv\Scripts\activate.ps1

установка django

    python.exe -m pip install --upgrade pip
    pip install django

создание проекта (project_hw2) и приложения (myapp) django

    django-admin startproject project_hw2
    python manage.py startapp myapp

в progect_hw2\settings.py INSTALLED_APPS добавляется  myapp (созданое приложение)

в файле \project_hw2\project_hw2\urls.py  в urlpatterns указывается путь для приложения myapp

в myapp создается файл urls.py  где  описываются urlpatterns для  views

в файле \project_hw2\myapp\views.py , создаются представления

в папке \project_hw2\myapp\management\commands\ создаются команды для консоли (также добавить__init__.py)

в файле \project_hw2\myapp\models.py создаются модели

создание миграций

    python manage.py makemigrations
    python manage.py migrate

в файле \project_hw2\myapp\forms.py создаются формы для html шаблонов

Создаем суперюзера

    python manage.py createsuperuser





