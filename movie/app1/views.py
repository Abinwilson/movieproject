from django.shortcuts import render
from app1.models import Movie
from app1.forms import movieform


# Create your views here.


def movie_list(request):
    m = Movie.objects.all()
    return render(request, 'movie.html', {'movie': m})


def add_movies(request):
    if request.method == "POST":
        title = request.POST['title']
        year = request.POST['year']
        about = request.POST['about']
        cover = request.FILES['cover']
        m = Movie.objects.create(title=title, year=year, about=about, cover=cover)
        m.save()
        return movie_list(request)
    return render(request, 'add_movies.html')


def view(request, id):
    m = Movie.objects.get(id=id)
    return render(request, 'detail.html', {'movie': m})


def update(request, id):
    m = Movie.objects.get(id=id)
    form = movieform(instance=m)
    if request.method == "POST":
        form = movieform(request.POST, request.FILES, instance=m)
        if form.is_valid():
            form.save()
            return movie_list(request)
    return render(request, 'update.html', {'form': form})


def delete(request, id):
    m = Movie.objects.get(id=id)
    m.delete()
    return movie_list(request)
