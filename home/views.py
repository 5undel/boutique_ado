from django.shortcuts import render

# Create your views here.

def index(requerd):
    """ A view to return the index page """

    return render(requerd, 'home/index.html')
