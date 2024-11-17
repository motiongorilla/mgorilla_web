from django.urls import path

from app.views import create_article, home

urlpatterns = [
    path("", home, name="home"),
    path("articles/create/", create_article, name="create_article"),
]
