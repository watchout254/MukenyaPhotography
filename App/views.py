from django.shortcuts import render
from .models import Destination

# Create your views here.

def homepage(request):
    dest1 = Destination()
    dest1.name = 'Personal'
    dest1.desc = 'Capture every moment'
    dest1.price = 1500
    #dest1.img = 'destination.jpg'
    #dest1.offer = False

    #dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dest1': dest1})

def about(request):
    return HttpResponse 
def faqs(request):
    return HttpResponse
def strategy(request):
    return HttpResponse
    
