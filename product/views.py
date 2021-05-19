from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import CreateProductForm
from account.models import Account


def home(request):
	products = Product.objects.all()
	context={'products':products}
	return render(request, "products/products.html", context)

		# title = request.POST['title']
        # image = request.POST['image']
        # minBidPrice = request.POST['minBidPrice']
        # end_date = request.POST['end_date']
        # details = request.POST['details']
        # user = Account
        # user = user.objects.create_user(title=title, image=image, minBidPrice=minBidPrice, end_date=end_date, details=details)
        # user.save()
        # return redirect('home')

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
	    return redirect('home')
	else:
		return render(request,'products/createProduct.html')

		




def singleproduct(request, pk):
	context = {}
	product = get_object_or_404(Product, id=pk)
	context['product'] = product

	return render(request, 'products/singleproduct.html', context)


@login_required
def myproducts(request):
	products = Product.objects.filter(user=request.user)
	context={'products':products}

	return render(request, "products/my_products.html", context)