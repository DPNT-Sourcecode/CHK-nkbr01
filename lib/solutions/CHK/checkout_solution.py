from collections import Counter, defaultdict


# noinspection PyUnusedLocal
# skus = unicode string

price_map = {"A": 50, "B": 30, "C": 20, "D": 15, "E":40}

multibuy_map = {"A": [(5, 200), (3, 130)], "B": [(2, 45)]}

promotion_map = {"E": (2, "B")}


class Cart:

    def __init__(self, s: str):
        self.total = 0
        self.cart = Counter(s)

    def calculate_cart_total(self):
        try:
            for item, quantity in self.cart.items():
                """check for applicable discounts"""
                if item in multibuy_map:
                    multibuy_total = self.apply_multibuy(item, quantity, multibuy_map, price_map)
                    self.total += multibuy_total
                else:
                    full_total = self.apply_full_price(item, quantity, price_map)
                    self.total += full_total
        except KeyError:
            return -1
        self.apply_promotion()
        return self.total
    
    def apply_promotion(self):
        for item, promotion in promotion_map.items():
            if item in self.cart:
                promo_quantity, promo_item = promotion[0], promotion[1]
                quantity = self.cart[item] // promo_quantity
                self.cart[promo_item] += quantity

    def apply_full_price(self, item, quantity, price_map):
        item_price = price_map[item]
        total = quantity * item_price
        return total
    
    def apply_multibuy(self, item, quantity, multibuy_map, price_map):
        total = 0
        cart_quantity = quantity
        multibuy_promos = multibuy_map[item]
        while cart_quantity:
            for promo in multibuy_promos:
                promo_quantity, promo_price = promo[0], promo[1]
                if cart_quantity >= promo_quantity:
                    used_promo = cart_quantity // promo_quantity
                    remainder = cart_quantity % promo_quantity
                    total += promo_price * used_promo
                    cart_quantity = remainder
            if cart_quantity:
                total += cart_quantity * price_map[item]
                cart_quantity = 0
        return total                

def checkout(skus: str) -> int:
    cart = Cart(skus)
    total = cart.calculate_cart_total()
    # cart.apply_promotion()

    return total



