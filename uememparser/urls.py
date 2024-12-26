from django.urls import path

from uememparser import views

urlpatterns = [
    path("", views.uememparser_view, name="uememparser"),
]
