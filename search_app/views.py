# from django.shortcuts import render,HttpResponse
# from shop . models import Product
# from django.db.models import Q
#
# def SearchResult(request):
#     products = None
#     query = None
#     if 'q' in request.GET:
#         query = request.GET.get('q')
#         products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
#         return render(request,'search.html',{'query':query,'products':products})
#     return render(request,'search.html')
#

from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

def SearchResult(request):
    query = request.GET.get('q')
    products = []

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'search.html', {'query': query, 'products': products})




