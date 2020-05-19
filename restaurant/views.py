from django.http import HttpResponse
from django.shortcuts import render
from .models import Menu
# Create your views here.



def index(request):
    context = {
        'menus': Menu.objects.all()
    }
    return render(request, 'restaurant/main.html', context)

def order(request):
    return render(request, 'restaurant/order.html')