from django.conf.urls import url
from . import views

app_name = 'news'
urlpatterns = [
    url(r'^$', views.list_news, name = 'list_news'),
    url(r'^(?P<slug>[\w-]+)/$', views.detail_news, name = 'detail_news'),
]
