from django.shortcuts import render
from testapp.forms import MovieForm
from testapp.models import movie
# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def addmovie(request):
    form=MovieForm()
    if request.method=="POST":
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index(request)
    return render(request,'testapp/addmovie.html',{'form':form})

def listview(request):
    movie_list=movie.objects.all()
    return render(request,'testapp/listmovies.html',{'movie_list':movie_list})
