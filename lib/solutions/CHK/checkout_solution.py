

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

def calculate_discounted_price():
    

def checkout(skus: str) -> int:
    cart = convert_string_to_cart(skus)
    total = 0
    try:
        for item, quantity in cart.items():
            total += calculate_discounted_price(item, quantity)
    except KeyError:
        return -1
    return total

