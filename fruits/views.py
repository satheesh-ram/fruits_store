from django.shortcuts import render
from .models import Fruit


def index(request):
    search_term = request.GET.get('search')
    if search_term:
        fruits = Fruit.objects.filter(name__icontains=search_term)
    else:
        fruits = Fruit.objects.all()
    template_data = {}
    template_data['title'] = 'Fruits'
    template_data['fruits'] = fruits
    return render(request, 'fruits/index.html', {'template_data':template_data})

def show(request, id):
    fruit = Fruit.objects.get(id=id)
    template_data = {}
    template_data['title'] = fruit.name
    template_data['fruit'] = fruit
    return render(request, 'fruits/show.html', {'template_data':template_data})
