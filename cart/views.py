from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from fruits.models import Fruit
from .utils import calculate_cart_total
from .models import Order, Item
from django.contrib.auth.decorators import login_required

def index(request):
    cart_total = 0
    fruits_in_cart = []
    cart = request.session.get('cart', {})
    fruit_ids = list(cart.keys())
    if (fruit_ids != []):
        fruits_in_cart = Fruit.objects.filter(id__in=fruit_ids)
        cart_total = calculate_cart_total(cart, fruits_in_cart)
    template_data = {}
    template_data['title'] = 'Cart'
    template_data['fruits_in_cart'] = fruits_in_cart
    template_data['cart_total'] = cart_total
    return render(request, 'cart/index.html',{'template_data':template_data})

def add(request, id):
    get_object_or_404(Fruit, id=id)
    cart = request.session.get('cart',{})
    cart[id] = request.POST['quantity']
    request.session['cart'] = cart
    return redirect('home.index')

def add_to_cart(request, id):
    get_object_or_404(Fruit, id=id)
    cart = request.session.get('cart',{})
    cart[id] = request.POST['quantity']
    request.session['cart'] = cart
    return redirect('cart.index')

def clear(request):
    request.session['cart'] = {}
    return redirect('cart.index')

@login_required
def purchase(request):
     cart = request.session.get('cart', {})
     fruit_ids = list(cart.keys())
     if (fruit_ids == []):
         return redirect('cart.index')
     fruits_in_cart = Fruit.objects.filter(id__in=fruit_ids)
     cart_total = calculate_cart_total(cart, fruits_in_cart)
     order = Order()
     order.user = request.user
     order.total = cart_total
     order.save()
     for fruit in fruits_in_cart:
         item = Item()
         item.fruit = fruit
         item.price = fruit.price
         item.order = order
         item.quantity = cart[str(fruit.id)] 
         item.save()
     request.session['cart'] = {}
     template_data = {}
     template_data['title'] = 'Purchase confirmation'
     template_data['order_id'] = order.id
     return render(request, 'cart/purchase.html', {'template_data': template_data})