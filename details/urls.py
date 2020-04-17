from django.urls import path
from . import views

urlpatterns = [
    path('<int:wine_id>/', views.wine_detail, name='detail'),
]