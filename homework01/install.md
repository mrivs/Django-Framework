    python -m venv venv
    venv\Scripts\activate.ps1 
    python.exe -m pip install --upgrade pip
    pip install django

    django-admin startproject project_hw1
    python manage.py startapp myapp_hw1

    в progect_hw1/settings.py INSTALLED_APPS добавляется  myapp_hw1

    в файле  myapp_hw1/views.py, создаются представления