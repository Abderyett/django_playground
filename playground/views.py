from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


def say_hello(request):
    # product=Product.objects.get(pk=1)
    # query_set=Product.objects.all()
    
    # exist = Product.objects.filter(pk=1).exists()
    
    # queryset = Product.objects.filter(unit_price_gt=20)
    # queryset = Product.objects.filter(unit_price__range=(20,30))
    queryset = Product.objects.filter(title__icontains='coffee')
    # queryset = Product.objects.filter(discription__isnull=True)
    
    

    return render(request, "hello.html", {"name": "AbderYett","products":list(queryset)})
