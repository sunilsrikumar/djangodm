__author__ = 'NESCODE'

from django import template

register = template.Library()

from ..models import Product, THUMB_CHOICES

@register.filter
def get_thumbnail(obj, arg):
    """
    obj == Product instance

    """
    arg = arg.lower()
    if not isinstance(obj, Product):
        raise TypeError("This is not a valid product model.")

    choice = dict(THUMB_CHOICES)
    if not choice.get(arg):
        raise TypeError("This is not a valid type for model.")
    try:
        return obj.thumbnail_set.filter(type=arg).first().media.url
    except:
        return None
