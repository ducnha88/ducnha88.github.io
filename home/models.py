from django.db import models

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length = 100)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='slider/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
