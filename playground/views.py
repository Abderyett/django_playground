from django.shortcuts import render
from django.db.models import Q, F,Value,Func,ExpressionWrapper
from store.models import Product,OrderItem, Order,Customer
from django.db.models.aggregates import Count,Min, Max


def say_hello(request):
    # product=Product.objects.get(pk=1)
    # query_set=Product.objects.all()
    
    # exist = Product.objects.filter(pk=1).exists()
    
    #* keyword__lookuptypes
    # queryset = Product.objects.filter(unit_price_gt=20)
    # queryset = Product.objects.filter(unit_price__range=(20,30))
    # queryset = Product.objects.filter(title__icontains='coffee')
    # queryset = Product.objects.filter(discription__isnull=True)
    # queryset = Product.objects.filter(discription__isnull=True)
    
    #* Product: inventory < 10 and unit_price < 20
    # queryset = Product.objects.filter(inventory__lt=20,unit_price__lt=20)
    
    #* Product: inventory < 10 OR unit_price < 20
    
    # queryset = Product.objects.filter(Q(inventory__lt=20) | ~Q(unit_price__lt=20))
    
    #* Product: inventory = unit_price
    
    # queryset=Product.objects.filter(inventory=F('unit_price'))
    
    #order by dec order
    # queryset=Product.objects.order_by('-unit_price')
    
    #* Limiting Result
    # 0,1,2,3,4
    # queryset=Product.objects.all()[:5]
    
    #* Selecting fields adm it return dictionary
    
    # queryset=Product.objects.values('id','title','collection__title')
    
    
    #? Select Product that have been ordered and sort them by title
    
    # queryset=Product.objects.filter(id__in=OrderItem.objects.values("product_id").distinct())
    
    
    #* . Selecting Related
    
    # We use prefetch related whne we have ManytoMany
    # queryset=Product.objects.select_related("collection").all()
    # We use select_related related whne we have ManytoMany
    # queryset=Product.objects.prefetch_related("promotions").select_related("collection").all()

    # queryset=Order.objects.select_related("customer").prefetch_related("orderitem_set__product").order_by("-placed_at")[:5]
    
    #* Agregate object
    
    # queryset=Product.objects.aggregate(count=Count('id'),max_price=Max("unit_price"))
    
    
    #* Annotate
    # queryset=Customer.objects.annotate(new_id=F('id'))
    
    #* Database function for
    # queryset=Customer.objects.annotate(full_name=Func(F('first_name'),Value(' '),F('last_name'),function='CONCAT'))
    
    #* Grouping data
    
    # queryset = Customer.objects.annotate(order_count=Count("order"))
    discounted_price= ExpressionWrapper(F('unit_price')* 0.8, output_field=DecimalField())
    queryset = Product.objects.annotate(discounted_price=discounted_price)
    # Expression Wrapper
    
    
    
    
    return render(request, "hello.html", {"name": "AbderYett","result":list(queryset)})
