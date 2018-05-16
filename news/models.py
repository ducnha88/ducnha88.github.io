from django.db import models
from django.urls import reverse
from django.db.models import Q

class PostManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) |
                         Q(content__icontains=query)|
                         Q(slug__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs

class News(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add = True)
    thumb = models.ImageField(default = 'default.png', blank = True)

    objects = PostManager()

    def reduce(self):
        if len(self.content)>500:
            return self.content[:500] + "..."
        else:
            return self.content



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:detail_news', args=[self.slug])
