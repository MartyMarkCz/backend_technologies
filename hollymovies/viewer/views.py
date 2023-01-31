from django.shortcuts import render
from django.http import HttpResponse
from viewer.models import *


# Create your views here.
def home(request):
    return render(request, 'home.html')


def hello(request, s):
    adjectives = ['wunderfull', 'nice', 'blue', s]
    context = {'adjectives': adjectives, 'name': 'Petr'}
    return render(request, 'hello.html', context)
    # return HttpResponse(f"Hello, {s} world!")


def hello2(request):
    s = request.GET.get('s', '')
    return HttpResponse(f"Hello, {s} world!")


def movies(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies.html', context)


def movie(request, pk):
    movie = Movie.objects.get(id=pk)
    countries = Country.objects.filter(movies=movie)
    genres = Genre.objects.filter(movies=movie)
    images = Image.objects.filter(movies=movie)
    directors = Staff.objects.filter(directing=movie)
    actors = Staff.objects.filter(acting=movie)
    context = {'movie': movie, 'countries': countries,
               'genres': genres, 'images': images,
               'directors': directors, 'actors': actors}
    return render(request, 'movie.html', context)


def staff(request, pk):
    staff = Staff.objects.get(id=pk)
    awards = Award.objects.filter(staff=staff)
    directing_movies = Movie.objects.filter(directing_movie=staff)
    acting_in_movies = Movie.objects.filter(acting_in_movie=staff)
    context = {'staff': staff, 'awards': awards,
               'directing_movies': directing_movies,
               'acting_in_movies': acting_in_movies}
    return render(request, 'staff.html', context)


def actors(request):
    staff_set = Staff.objects.all()
    actors = []
    for staff in staff_set:
        if Movie.objects.filter(acting_in_movie=staff).count() > 0:
            actors.append(staff)
    context = {'actors': actors}
    return render(request, 'actors.html', context)


def search(request):
    if request.method == 'POST':  # pokud jsme poslali dotaz z formuláře
        search = request.POST.get('search')
        search = search.strip()
        if len(search) > 0:
            movies_title_orig = Movie.objects.filter(title_orig__contains=search)
            movies_title_cz = Movie.objects.filter(title_cz__contains=search)
            movies_title_sk = Movie.objects.filter(title_sk__contains=search)
            movies_descr = Movie.objects.filter(description__contains=search)
            staff_names = Staff.objects.filter(name__contains=search)
            staff_surnames = Staff.objects.filter(surname__contains=search)

            context = {'search': search, 'movies_title_orig': movies_title_orig,
                       'movies_title_cz': movies_title_cz, 'movies_title_sk': movies_title_sk,
                       'movies_descr': movies_descr,
                       'staff_names': staff_names, 'staff_surnames': staff_surnames}
            return render(request, 'search.html', context)
    return render(request, 'home.html')
