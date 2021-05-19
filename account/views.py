from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.http import HttpResponse
from .models import Account
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST['email']
        password ='0'
        user = Account
        if user.objects.filter(email=email).exists():
                user = authenticate(email=email, password=password)
                login(request, user)
                messages.error(request, 'Username is already taken')
                return redirect('home')
        else:
            user = user.objects.create_user( email=email,password=password)
            user.save()
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
    
    else:
        return render(request, 'registration/register.html')


@login_required
def userlogout(request):
    logout(request)
    return redirect('home')

def userlogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST['email']
        password = '0'
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            user=Account
            user = user.objects.create_user( email=email,password=password)
            user.save()
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
    else:
        return render(request, 'registration/login.html')

