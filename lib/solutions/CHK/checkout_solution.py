

# noinspection PyUnusedLocal
# skus = unicode string

price_map = {"A": 50, "B": 30, "C": 20, "D": 15}

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

def checkout(skus):
    cart = convert_string_to_cart(skus)
    total = 0
    for item, quantity in cart.items():
        total += price_map[item] * quantity
    return total
