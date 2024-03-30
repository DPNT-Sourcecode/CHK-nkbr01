from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string

price_map = {"A": 50, "B": 30, "C": 20, "D": 15, "E":40}

discount_map = {"A": (3, 130), "B": (2, 45)}

promotion_map = {"E": (2, "B")}


class Cart:
    cart = {}
    total = 0

    def __init__(self, s: str):
        self.cart = Counter(s)

    def calculate_cart_total(self):
        # total = 0
        try:
            for item, quantity in self.cart.items():
                """check for applicable discounts"""
                if item in discount_map:
                    full_price = price_map[item]
                    sale_quantity, sale_price = discount_map[item]
                    self.total += calculate_discounted_price(quantity, full_price, sale_quantity, sale_price)
                else:
                    self.total += price_map[item] * quantity
                """check for applicable promotions"""
                if item in promotion_map:
                    apply_promotions

        except KeyError:
            return -1
        return self.total
    
    # def apply_promotions(cart_quantity: int, promotion_item: str, promotion_item_price: int):
    #     pass 


def calculate_discounted_price(cart_quantity: int, full_price: int, sale_quantity: int, sale_price: int):
    quantity = cart_quantity // sale_quantity
    remainder = cart_quantity % sale_quantity
    total_price = quantity * sale_price + remainder * full_price
    return total_price



                

def checkout(skus: str) -> int:
    cart = Cart(skus)
    total = cart.calculate_cart_total()
    return total


