from django import template
from shop.models import *

register = template.Library()
@register.filter
def getPro(cateId):
    return Product.objects.filter(category=cateId)
