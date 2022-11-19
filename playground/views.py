from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
   return render(request, 'hello.html', {'name':'Abderyett'})


def products(request):
   return render(request, 'products.html',{"name":"Chicken brest"})

