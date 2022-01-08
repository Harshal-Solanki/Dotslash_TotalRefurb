from django.shortcuts import render
from .models import *
from EWApp.models import SellerForm
from django.http import JsonResponse

# Create your views here.
def store(request):
    products= Product.objects.all()
    context = {'products' :products}
    return render(request,'EWApp/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []  
        order = {'get_cart_total':0, 'get_cart_items':0}  

    context = {'items':items, 'order':order}    
    return render(request,'EWApp/cart.html',context)

def order(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []  
        order = {'get_cart_total':0, 'get_cart_items':0}
          
    context = {'items':items, 'order':order}
    return render(request,'EWApp/order.html',context)

def seller(request):
    # print(request.POST)
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        address = request.POST.get('address')
        comments = request.POST.get('comments')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')

        sellerform = SellerForm(name=name, email=email, number=number, address=address, comments=comments, city=city, state=state, pincode=pincode)
        sellerform.save()
    return render(request, 'EWApp/seller.html')

def aboutus(request):
    return render(request, 'EWApp/aboutus.html')

def updateitem(request):
    return JsonResponse('Item was added', safe=False)    