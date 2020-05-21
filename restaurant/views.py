from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Menu, Order
from django.contrib import messages
# Create your views here.



def index(request):
    context = {
        'menus': Menu.objects.all()
    }
    return render(request, 'restaurant/main.html', context)

def order(request):
    if request.method == 'POST':
        order = Order()
        order.orderer_name = request.POST.get('name')
        order.orderer_surname = request.POST.get('surname')
        order.orderer_email = request.POST.get('email')
        order.orderer_phone = request.POST.get('phone')
        order.orderer_address = request.POST.get('address')
        order.order_price = request.POST.get('newOrder')
        order.order_detail = request.POST.get('comeOrder')
        order.save()
        messages.success(request, "Siparisiniz basariyla alindi")
    return render(request, 'restaurant/order.html')