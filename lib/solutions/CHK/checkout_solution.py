

# noinspection PyUnusedLocal
# skus = unicode string

price_map = {"A": 50, "B": 30, "C": 20, "D": 15}

discount_map = {"A": (3, 130), "B": (2, 45)}

from collections import defaultdict
    
def convert_string_to_cart(s: str) -> dict:
    cart = defaultdict(int)
    n = 0
    while s:
        c = s[0]
        if c.isdigit():
            if n:
                n += c
            else:
                n = c
        else:
            if n:
                cart[c] = int(n)
                n = 0
            else:
                cart[c] = 1
        s = s[1:]
    return cart


def calculate_discounted_price(cart_quantity, full_price, sale_quantity, sale_price):
    quantity = cart_quantity // sale_quantity
    remainder = cart_quantity % sale_quantity
    total_price = quantity * sale_price + remainder * full_price
    return total_price
            

def checkout(skus: str) -> int:
    cart = convert_string_to_cart(skus)
    total = 0
    try:
        for item, quantity in cart.items():
            if item in discount_map:
                full_price = price_map[item]
                sale_quantity, sale_price = discount_map[item]
                total += calculate_discounted_price(quantity, full_price, sale_quantity, sale_price)
            else:
                total += price_map[item] * quantity
    except KeyError:
        return -1
    return total


