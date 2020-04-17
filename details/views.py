from django.shortcuts import render, get_object_or_404, redirect
from wine_list.models import AllWines

# Create your views here.
def wine_detail(request, wine_id):
    winedetail = get_object_or_404(AllWines, pk=wine_id)
    return render(request, 'details/detail.html', {'wine': winedetail})