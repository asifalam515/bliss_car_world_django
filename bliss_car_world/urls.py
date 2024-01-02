"""
URL configuration for bliss_car_world project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(),name='home'),
    path('', include('brand.urls')),
    path('', include('car.urls')),
    path('register/',views.Register.as_view(),name='register'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('purchase/<int:car_id>/', views.purchase_car, name='purchase_car'),
    # path('details/<int:car_id>/', views.details_car, name='view_details'),
    path('profile/', views.profile, name='profile'),
    path('add_comment/<int:car_id>/', views.add_comment, name='add_comment'),
    path('car_detail/<int:car_id>/', views.car_detail, name='car_detail'),
    # path('car_detail/<int:car_id>/', views.DetailCarView.as_view(), name='car_detail'),

    

    
    
]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
