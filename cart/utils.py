def calculate_cart_total(cart, fruits_in_cart):
    total = 0
    for fruit in fruits_in_cart:
        quantity = cart[str(fruit.id)]
        total += fruit.price * int(quantity)
    return total