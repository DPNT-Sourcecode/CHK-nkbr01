

# noinspection PyUnusedLocal
# skus = unicode string

from collections import defaultdict
def checkout(skus):
    
    price_map = {"A": 50, "B": 30, "C": 20, "D": 15}

def convert_string_to_cart(s: str) -> dict:
    cart = defaultdict(int)
    n = 0
    #A2B4C23D
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