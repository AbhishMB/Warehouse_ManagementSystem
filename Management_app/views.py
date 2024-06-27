from django.shortcuts import render,redirect
from .models import Product, Stock, Delivery
from .forms import StockForm

def list_products(request):
    location = request.GET.get('location')
    priority = request.GET.get('priority')
    product_name = request.GET.get('product_name')
    category = request.GET.get('category')

    products = Product.objects.all()

    if location:
        products = products.filter(stock__warehouse__location__address__icontains=location)
    if priority:
        products = products.filter(delivery__priority=priority)
    if product_name:
        products = products.filter(name__icontains=product_name)
    if category:
        products = products.filter(category__icontains=category)

    return render(request, 'list_products.html', {'products': products})



def stock_up_product(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Replace with your success URL
    else:
        form = StockForm()
    return render(request, 'stock_up.html', {'form': form})

