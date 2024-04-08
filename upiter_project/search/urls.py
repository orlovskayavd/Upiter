from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_page, name='search_page'),  # Страница поиска
    #path('about_drug/', views.about_drug_page, name='about_drug_page'),  # Страница о лекарстве
]
