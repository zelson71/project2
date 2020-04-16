"""wine_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import wine_list.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wine_list.views.index, name='home' ),
    path('wine_data/',wine_list.views.w_data, name='wine_data'),
    path('accounts/', include('accounts.urls')), 
    path('wine/',wine_list.views.wine,name='wine'),
    path('types/',wine_list.views.types,name='types'),
    path('deets/', wine_list.views.deets, name='details')
   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
