
from django.urls import path
from . import views


urlpatterns = [
    path('', views.register, name='register'),
    path('adminview', views.adminView, name='adminview'),
    path('completed', views.completed, name='completed'),
    path('running', views.running, name='running'),
    path('login', views.userlogin, name='login'),
    path('logout', views.userlogout, name='logout'),
]