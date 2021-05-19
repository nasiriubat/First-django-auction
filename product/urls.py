
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name='create'),
    path('myproducts', views.myproducts, name='myproducts'),
    path('singleproduct/<str:pk>', views.singleproduct, name='singleproduct')
]