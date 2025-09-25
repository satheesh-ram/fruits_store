from django import template
register = template.Library()
@register.filter(name='get_quantity')

def get_cart_quantity(cart, fruit_id):
    return cart[str(fruit_id)]
