from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),  # Страница домашней страницы
    #path('', views.search_page, name='search_page'),  # Страница поиска
]
