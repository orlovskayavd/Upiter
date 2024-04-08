"""upiter_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include  # Импорт функции include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Подключение URL-маршрутов приложения home
    path('search/', include('search.urls')),  # Подключение URL-маршрутов приложения search
    path('about_drug/', include('about_drug.urls')),  # Подключение URL-маршрутов приложения about_drug
]





