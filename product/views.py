from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Bid, Product
from .forms import CreateProductForm
from account.models import Account
from django.db.models import Q


def home(request):
	products = Product.objects.all()
	context={'products':products}
	return render(request, "products/products.html", context)


@login_required
def create(request):
	if request.method=='POST':
	    title = request.POST['title']
	    image = request.FILES['image']
	    minBidPrice = request.POST['minBidPrice']
	    end_date = request.POST['end_date']
	    details = request.POST['details']
	    user = request.user
	    product =Product(user=user,title=title, image=image, minBidPrice=minBidPrice, end_date=end_date, details=details)
	    product.save()
	    messages.success(request,'New product added.')
	    return redirect('home')
	else:
		return render(request,'products/createProduct.html')

		




def singleproduct(request, pk):
	
	# product = get_object_or_404(Product, id=pk)
	# bids=get_object_or_404(Bid,product=pk)
	product=Product.objects.get(id=pk)
	bids=Bid.objects.filter(product=product)
	winner = bids.order_by('-bidAmount')[0]
	if request.method=='POST':
		if request.user.is_authenticated:
		    bid=Bid
		    product=product
		    bidmoney=request.POST['bidamount']
		    if bid.objects.filter(user=request.user,product=product).exists():
			    biduser=Bid.objects.filter(Q(user=request.user) & Q(product=product)).update(bidAmount=bidmoney)
			    # biduser.bidAmount=bidmoney
			    # biduser.save()
			    return redirect ('singleproduct',pk=product.id)
		    else:
			    newbid=Bid(user=request.user,product=product,bidAmount=bidmoney)
			    newbid.save()
			    return redirect('singleproduct',pk=product.id)
		else:
			return redirect('login')

	context = {'product':product,'bids':bids,'winner':winner}
	return render(request, 'products/singleproduct.html', context)


@login_required
def myproducts(request):
	products = Product.objects.filter(user=request.user)
	context={'products':products}

	return render(request, "products/my_products.html", context)