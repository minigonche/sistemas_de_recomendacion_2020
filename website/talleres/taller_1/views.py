from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    
    context = {}
    return render(request, 'taller_1/index.html', context)
