from django.shortcuts import render, redirect

from .forms import MovieForm
from .models import Film


# Create your views here.
def home(request):
    a = Film.objects.all()
    return render(request, 'home.html', {'obj': a})


def detail(request, id):
    mo = Film.objects.get(id=id)
    return render(request, 'details.html', {'mo': mo})


def form(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        year = request.POST.get('year', )
        img = request.FILES['image']
        desc = request.FILES['description']

        m = Film(name=name, year=year, image=img, description=desc)
        m.save()
        return redirect('/')
    return render(request, 'forms.html')


def update(request, id):
    c = Film.objects.get(id=id)
    forms = MovieForm(request.POST or None, request.FILES, instance=c)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    else:
        forms = MovieForm(instance=c)
        return render(request, 'update.html', {'forms': forms})

def delete(request, id):
    if request.method == 'POST':
        c = Film.objects.get(id=id)
        c.delete()
        return redirect('/')
    return render(request, 'delete.html')