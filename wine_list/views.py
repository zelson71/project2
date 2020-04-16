from django.shortcuts import render, get_object_or_404

from .models import AllWines
from wine_list.choices import wine_rating, country, category_options

# Create your views here.
def index(request):
    return render(request, 'wine_list/index.html')

def w_data(request):
    # my_wine = AllWines.objects.all() [:5000]
    # context = {"title": "title" , "my_wine": my_wine}
    # return render(request, 'wine_list/wine_data.html', context)
    queryset_list = AllWines.objects.all()    

    if 'rating' in request.GET:
        rating = request.GET['rating']
        if rating:
            queryset_list = queryset_list.filter(rating__gte=rating)
    
    # if 'country' in request.GET:
    #     country = request.GET['country']
    #     if country:
    #         queryset_list = queryset_list.filter(country__iexact=country)
    
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__gte=price)

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            queryset_list = queryset_list.filter(category__icontains=category)

    context = {
    'title': 'title' ,
    'my_wine': queryset_list,     
    'country': country,
    'wine_rating':wine_rating,
    # 'category':category,
    'values': request.GET
     }
    return render(request, 'wine_list/rating.html', context)

def deets(request,):
    # details = get_object_or_404()
    return render(request, 'wine_list/deets.html')

def wine(request):
    wine_info = AllWines.objects.all() [:5000]
    context = {"title": "title" , "my_wine": wine_info}
    return render(request, 'wine_list/wine.html', context)

def types(request):
    types = AllWines.objects.all() [:5000]
    context = {"title": "title" , "my_wine": types}
    return render(request, 'wine_list/types.html', context)


    
   



