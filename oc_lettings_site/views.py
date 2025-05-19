from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def test_500(request):
    raise Exception('Erreur de pour le 500')