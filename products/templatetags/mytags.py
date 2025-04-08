from django import template

register = template.Library()


@register.simple_tag
def get_heart_icon(request, product):
    if request.user in product.wishlist.all():
        return 'fa-solid fa-heart'
    return 'far fa-heart'
