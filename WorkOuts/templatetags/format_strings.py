from django import template

register = template.Library()


@register.filter
def price_comma_separate(value: int):
    return "{:,}".format(value)
