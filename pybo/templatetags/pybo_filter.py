from django import template

register = template.Library()


@register.filter
def sub(self, arg):
    return self - arg