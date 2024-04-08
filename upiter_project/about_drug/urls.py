from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_drug_page, name='about_drug_page'),  # Страница о лекарстве
]
