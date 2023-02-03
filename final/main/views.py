from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Product, Category, OrderUser
from .forms import OrderForm
from django.views.generic import CreateView


def index(request):
    products = Product.objects.all()
    cats = Category.objects.all()

    context = {
        'products': products,
        'cats': cats,
        'title': 'Main page',
        'cat_selected': 0,
    }

    return render(request, 'main/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found!!!</h1>')


def show_product(request, product_id):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = OrderForm()
    return render(request, 'main/order.html', {'product_id': product_id, 'form': form})

    # return HttpResponse(f"Order product: id = {product_id}")


def success(request):
    return HttpResponse('Order complete!')


def show_category(request, cat_id):
    products = Product.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(products) == 0:
        raise Http404()

    context = {
        'products': products,
        'cats': cats,
        'title': 'Category filter',
        'cat_selected': cat_id,
    }

    return render(request, 'main/index.html', context=context)
