from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    context = {}
    links = models.Link.objects.all()
    context['links'] = links


    return render(request, 'index.html', context)