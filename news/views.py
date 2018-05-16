from django.shortcuts import render
from .models import News
from django.core.paginator import Paginator


# Create your views here.

def list_news(request):
    list_news = News.objects.all().order_by('-datetime')
    page = request.GET.get('page', 1)

    paginator = Paginator(list_news, 10)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    return render(request, 'list_news.html', {'news':news})



def detail_news(request, slug):
    new = News.objects.get(slug = slug)
    return render(request, 'detail_news.html', {'new':new})
