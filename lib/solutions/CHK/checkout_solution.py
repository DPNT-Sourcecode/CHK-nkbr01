from collections import Counter, defaultdict


# noinspection PyUnusedLocal
# skus = unicode string

price_map = {"A": 50, "B": 30, "C": 20, "D": 15, "E":40}

multibuy_map = {"A": [(5, 200), (3, 130)], "B": [(2, 45)]}

promotion_map = {"E": (2, "B")}


class Cart:

    def __init__(self, s: str):
        self.total = 0
        # self.applied_promotions = 0
        self.cart = Counter(s)

    def calculate_cart_total(self):
        try:
            for item, quantity in self.cart.items():
                """check for applicable discounts"""
                if item in multibuy_map:
                    full_price = price_map[item]
                    sale_quantity, sale_price = multibuy_map[item]
                    self.total += calculate_discounted_price(quantity, full_price, sale_quantity, sale_price)
                else:
                    self.total += price_map[item] * quantity

                    # if promo_item in self.cart:
                    #     discount = (self.cart[item] // promotion_map[item][0]) * price_map[promo_item]
                    #     self.total -= discount
        except KeyError:
            return -1
        # self.total -= self.applied_promotions
        self.apply_promotion()
        return self.total
    
    # promotion_map = {"E": (2, "B")}

    def apply_promotion(self):
        for item, promotion in promotion_map.items():
        # for item, quantity in self.cart.items():
            if item in self.cart:
                promo_quantity, promo_item = promotion[0], promotion[1]
                quantity = self.cart[item] // promo_quantity
                self.cart[promo_item] += quantity
                # self.applied_promotions = price_map[promo_item] * quantity


def calculate_discounted_price(cart_quantity: int, full_price: int, sale_quantity: int, sale_price: int):
    quantity = cart_quantity // sale_quantity
    remainder = cart_quantity % sale_quantity
    total_price = quantity * sale_price + remainder * full_price
    return total_price
                

def checkout(skus: str) -> int:
    cart = Cart(skus)
    total = cart.calculate_cart_total()
    # cart.apply_promotion()

    return total