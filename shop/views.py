
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    list_products = Product.objects.filter(available=True)
    page = request.GET.get('page', 1)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        list_products = list_products.filter(category=category)
    paginator = Paginator(list_products, 20)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'shop/product/list.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products,})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

def error(request):
    return render(request,'shop/error.html' )
