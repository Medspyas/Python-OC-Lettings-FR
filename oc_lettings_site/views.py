from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    Affiche la page d'accueil du site.

    Rend le template 'index.html' sans contexte particulier.
    """
    return render(request, "index.html")


def test_500(request):
    raise Exception('Erreur de pour le 500')


def test_error(request):
    division_by_zero = 1 / 0