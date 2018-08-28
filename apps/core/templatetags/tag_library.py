from django import template

register = template.Library()


@register.filter()
def to_float_persent(value):
    return round(float(value) - 1, 2)
