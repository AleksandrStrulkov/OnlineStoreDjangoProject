from django import template
from django.conf import settings

register = template.Library()


@register.filter()
def mymedia(validate):
    if validate:
        return f'/media/{validate}'
    return ''


# @register.simple_tag()
# def mediapath(validate):
#     if validate:
#         return f'/media/{validate}'
#     return 'НЕТ ФОТО'

@register.simple_tag()
def mediapath(path):
    return f'{settings.MEDIA_URL}{path}'
