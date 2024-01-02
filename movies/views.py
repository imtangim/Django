from django.http import HttpResponse
from django.shortcuts import render


data = {'movies': [
    {
        'uid': 5,
        "title": "Jose",
        'year': 1669,
    },
    {
        'uid': 6,
        "title": "American Pie",
        'year': 1769,
    },
    {
        'uid': 7,
        "title": "Meg",
        'year': 1969,
    },
]}


def movies(request):
    return render(request, 'movies/movies.html', data)


def home(request):
    return HttpResponse("Home")
