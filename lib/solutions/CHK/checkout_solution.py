

# noinspection PyUnusedLocal
# skus = unicode string

from collections import defaultdict
def checkout(skus):
    
    price_map = {"A": 50, "B": 30, "C": 20, "D": 15}

    def convert_string_to_cart(s: str) -> dict:
        cart = defaultdict(int)
        #A2B4C23D
        while s:
            c = s[0]
            if c.isdigit():

            else:


            s = s[1:]


