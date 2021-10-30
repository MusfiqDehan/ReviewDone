from django.http import HttpResponse
from django.shortcuts import render
from movies.models import Movie


def index(request):
    '''
    View function for home page
    '''
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)
