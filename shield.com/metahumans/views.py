from django.shortcuts import render
from metahumans import models

# Create your views here.

def view_all_heroes(request):
    return render(request, 'not_imp.html', )
