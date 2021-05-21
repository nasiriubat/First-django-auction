from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponse
from .models import Account
from product.models import Product,Bid
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
            messages.success(request, 'This email alreay exists and you are logged in')
            return redirect('home')
        else:
            user = user.objects.create_user( email=email,password=password)
            user.save()
            login(request, user)
            messages.success(request, 'Your Account has been created.')
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
            messages.success(request,'You are now logged in.')
            return redirect('home')
        else:
            user=Account
            user = user.objects.create_user( email=email,password=password)
            user.save()
            login(request, user)
            messages.success(request, 'New account is created as the email did not exist.')
            return redirect('home')
    else:
        return render(request, 'registration/login.html')




@login_required
def adminView(request):
    if not request.user.is_superuser:
        messages.success(request,'not allowed')
        return redirect('home')
    products=Product.objects.all()
    user=Account.objects.all()
    bid=Bid.objects.all()
    running=0
    completed=0
    for product in products:
        if timezone.now()>product.end_date:
            completed+=1
        else:
            running+=1        
    context={'products':products,'user':user,'bid':bid,'running':running,'completed':completed}
    return render(request,'adminview/adminview.html',context)

@login_required
def completed(request):
    if not request.user.is_superuser:
        messages.success(request,'not allowed')
        return redirect('home')
    products=Product.objects.all()
    user=Account.objects.all()
    bid=Bid.objects.all()

    completedbid=Product.objects.filter(end_date__lt=timezone.now()) 
    running=0
    completed=0
    for product in products:
        if timezone.now()>product.end_date:
            completed+=1
        else:
            running+=1           
    context={'products':products,'user':user,'bid':bid,'running':running,'completed':completed,'completedbid':completedbid}
    return render(request,'adminview/completed.html',context)


@login_required
def running(request):
    if not request.user.is_superuser:
        messages.success(request,'not allowed')
        return redirect('home')
    products=Product.objects.all()
    user=Account.objects.all()
    bid=Bid.objects.all()

    runningbid=Product.objects.filter(end_date__gt=timezone.now()) 
    running=0
    completed=0
    for product in products:
        if timezone.now()>product.end_date:
            completed+=1
        else:
            running+=1           
    context={'products':products,'user':user,'bid':bid,'running':running,'completed':completed,'runningbid':runningbid}
    return render(request,'adminview/running.html',context)

    

