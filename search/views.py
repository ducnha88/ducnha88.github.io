from django.shortcuts import render
from itertools import chain
from django.views.generic import ListView
# Create your views here.
from shop.models import Category, Product
from news.models import News


class SearchView(ListView):
    template_name = 'view.html'
    paginate_by = 10
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            news_results        = News.objects.search(query)
            category_results    = Category.objects.search(query)
            product_results     = Product.objects.search(query)

            # combine querysets
            queryset_chain = chain(
                    news_results,
                    category_results,
                    product_results,
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs) # since qs is actually a list
            return qs
        return News.objects.none() # just an empty queryset as default
