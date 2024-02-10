import logging
from django.shortcuts import render
from django.http import HttpResponse

logger=logging.getLogger(__name__)

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
    logger.info("MAIN page page was visited ")
    return HttpResponse(html)

def about(request):

    html="""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Обо мне</title>
    </head>
    <body>
        <h2>Привет, я Valentin.</h2>
        <p>Я обучаюсь веб-разработке и решил начать свой путь с Django. Я увлеченный программист, который стремится к изучению новых технологий и созданию крутых проектов.</p>
    </body>
    </html>
        
    """
    logger.info("ABOUT page page was visited ")
    return HttpResponse(html)


# Create your views here.
