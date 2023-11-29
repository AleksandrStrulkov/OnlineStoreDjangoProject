from django import template

register = template.Library()


@register.filter()
def mymedia(validate):
    if validate:
        return f'/media/{validate}'
    return ''


@register.filter()
def split(str_, splitter):
    return str_.split(splitter)
