"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from books import views


urlpatterns = [
  path("character/",views.get_all_characters),
  path("character/<str:ids>/",views.get_character_info),
  path("character/<int:id>/book/",views.get_character_book),

  path("book/",views.get_all_books),
  path("book/<str:ids>/",views.get_book_info),

  path("book/cover",views.get_books_cover),
  path("book/<str:book_ids>/cover",views.get_cover),
]
