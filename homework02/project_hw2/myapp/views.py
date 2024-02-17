from django.shortcuts import render

# Create your views here.
import logging
from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    html="""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Мой Django-сайт</title>
    </head>
    <body>
        <h2>Добро пожаловать на мой первый Django-сайт!</h2>
        <p>Здесь я планирую разместить свои проекты, изученные технологии и другую интересную информацию.</p>
    </body>
    </html>
    
    """
    
    return HttpResponse(html)