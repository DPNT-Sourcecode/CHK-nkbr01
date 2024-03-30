from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string

price_map = {"A": 50, "B": 30, "C": 20, "D": 15, "E":40}

discount_map = {"A": (3, 130), "B": (2, 45)}

promotion_map = {"E": (2, "B")}

class Cart:
    cart = {}
    total = 0
    
    def convert_string_to_cart(self, s: str) -> dict:
        self.cart = Counter(s)
        return self.cart


    def calculate_discounted_price(self, cart_quantity: int, full_price: int, sale_quantity: int, sale_price: int):
        quantity = cart_quantity // sale_quantity
        remainder = cart_quantity % sale_quantity
        total_price = quantity * sale_price + remainder * full_price
        return total_price
                

def checkout(skus: str) -> int:
    cart = Cart.convert_string_to_cart(skus)
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