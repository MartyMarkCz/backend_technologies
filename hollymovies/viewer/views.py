from django.http import HttpResponse
from django.shortcuts import render
from viewer.models import *


# Create your views here.
def home(request):
    return render(request,'home.html')


def hello(request, s):
    adjectives = ['wonderful', 'nice', 'blue', s]
    context = {'adjectives': adjectives, 'name': 'Martin'}
    return render(request, 'moviehello.html', context)
    # return HttpResponse(f"Hello, {s} world!")


def hello2(request):
    s = request.GET.get('s', '')
    return HttpResponse(f"Hello, {s} world!")


def movies(request):
    movies = Movie.objects.all()
    context = {'movie': movies}
