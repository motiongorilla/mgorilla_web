import requests
from django.core.management import call_command
from django.http import HttpResponseServerError
from django.shortcuts import redirect


def uememparser_view(request):
    app_url = "http://127.0.0.1:8501"
    return redirect(app_url)

