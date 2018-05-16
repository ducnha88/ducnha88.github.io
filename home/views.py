from django.shortcuts import render
from shop.models import Category, Product
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from .models import Slider


# Create your views here.
def home_page(request):
    slider = Slider.objects.all()[0]
    categories = Category.objects.all()
    category3 = Category.objects.all()[1:4]
    products = Product.objects.filter(available=True, new = True)
    product20 = products[:20]
    product10 = Product.objects.filter(hot=True)[:10]
    return render(request, 'homepage.html', { 'slider': slider,'categories':categories,'category3':category3, 'product20':product20, 'product10':product10,})

def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/')
    return render(request, 'register.html', {'form':form})

def user_page(request):
     return render(request, 'user.html')
