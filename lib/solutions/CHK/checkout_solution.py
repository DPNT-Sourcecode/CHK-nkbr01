from collections import Counter, defaultdict


# noinspection PyUnusedLocal
# skus = unicode string

price_map = {"A": 50, "B": 30, "C": 20, "D": 15, "E":40, "F":10}

multibuy_map = {"A": [(5, 200), (3, 130)], "B": [(2, 45)]}

promotion_map = {"E": (2, "B"), "F": (2, "F")}

class Cart:

    def __init__(self, s: str):
        self.total = 0
        self.cart = Counter(s)

    def calculate_cart_total(self):
        try:
            for item, quantity in self.cart.items():
                if item in multibuy_map:
                    multibuy_promos = multibuy_map[item]
                    for promo in multibuy_promos:
                    promo_quantity, promo_price = multibuy_map[item][0], multibuy_map[item][1]
                    multibuy_total = self.apply_multibuy(item, quantity, promo_quantity, promo_price)
                    self.total += multibuy_total
                else:
                    full_total = self.apply_full_price(item, quantity)
                    self.total += full_total
        except KeyError:
            return -1
        self.total -= self.apply_promotion()
        return self.total
    
    def apply_promotion(self):
        total_discount = 0
        for item, promotion in promotion_map.items():
            required_quantity, promo_item = promotion[0], promotion[1]
            if item in self.cart and promo_item in self.cart:
                promo_quantity = self.cart[item] // required_quantity
                cart_quantity = self.cart[promo_item]
                updated_quantity = cart_quantity - promo_quantity
                if promo_item in multibuy_map:
                    previous_price = self.apply_multibuy(promo_item, cart_quantity)
                    updated_price = self.apply_multibuy(promo_item, updated_quantity)
                else:
                    previous_price = self.apply_full_price(promo_item, cart_quantity)
                    updated_price = self.apply_full_price(promo_item, updated_quantity)
                discount= previous_price - updated_price
                total_discount += discount
        return total_discount
    
    def apply_full_price(self, item, quantity):
        item_price = price_map[item]
        total = quantity * item_price
        return total
    
    def apply_multibuy(self, item, quantity, promo_quantity, promo_price):
        total = 0
        cart_quantity = quantity
        multibuy_promos = multibuy_map[item]
        while cart_quantity:
            for promo in multibuy_promos:
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
