from django.shortcuts import render

# Create your views here.
# posts/views.py
from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Главная страница')


# Страница, на которой посты отфильтрованные по группам;
# view-функция принимает параметр slug из path()
def group_posts(request, slug):
    return HttpResponse(f'Группа постов: {slug}')
