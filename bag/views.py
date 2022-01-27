from django.shortcuts import render

# Create your views here.

def view_bag(requerd):
    """ A view to return the bag contents page """

    return render(requerd, 'bag/bag.html')
