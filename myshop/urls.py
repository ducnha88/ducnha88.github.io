
from django.conf.urls import include, url, handler404, handler500
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^contact/', include('contact.urls', namespace='contact')),
    url(r'^shop/', include('shop.urls', namespace='shop')),
    url(r'^', include('home.urls', namespace='home')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^search/', include('search.urls', namespace='search')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler404 = 'shop.views.error'
handler500 = 'shop.views.error'
