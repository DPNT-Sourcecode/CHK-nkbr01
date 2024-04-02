from collections import Counter, defaultdict


# noinspection PyUnusedLocal
# skus = unicode string

FULL_PRICES = {
    "A": 50, 
    "B": 30, 
    "C": 20, 
    "D": 15, 
    "E": 40, 
    "F": 10,
}

MULTIBUY_DISCOUNTS = {
    "A": [
        (5, 250 - 200), #required_amount, total_discount_amount
        (3, 150 - 130),
    ],
    "B": [
        (2, 45)
    ],
}

PROMOS = {
    "E": (2, "B"), 
    "F": (2, "F")}

class Cart:

    def __init__(self, s: str):
        self.total = 0
        self.cart = Counter(s)

    def calculate_cart_total(self):
        try:
            for item, quantity in self.cart.items():
                self.total = self._apply_full_price(item, quantity)
                if item in MULTIBUY_DISCOUNTS:
                    self.total -= self._apply_multibuy(item, quantity)
                    # self.total += multibuy_total
                else:
                    full_total = self.apply_full_price(item, quantity)
                    self.total += full_total
        except KeyError:
            return -1
        self.total -= self.apply_promotion()
        return self.total
    
    def _apply_full_price(self, item, quantity):
        total = quantity * FULL_PRICES[item]
        return total

    def apply_promotion(self):
        total_discount = 0
        for item, promotion in PROMOS.items():
            required_quantity, promo_item = promotion[0], promotion[1]
            if item in self.cart and promo_item in self.cart:
                promo_quantity = self.cart[item] // required_quantity
                cart_quantity = self.cart[promo_item]
                updated_quantity = cart_quantity - promo_quantity
                if promo_item in MULTIBUY_DISCOUNTS:
                    previous_price = self._apply_multibuy(promo_item, cart_quantity)
                    updated_price = self._apply_multibuy(promo_item, updated_quantity)
                else:
                    previous_price = self.apply_full_price(promo_item, cart_quantity)
                    updated_price = self.apply_full_price(promo_item, updated_quantity)
                discount = previous_price - updated_price
                total_discount += discount
        return total_discount
    
    def apply_full_price(self, item, quantity):
        item_price = FULL_PRICES[item]
        total = quantity * item_price
        return total
    
    # def apply_multibuy(self, item, quantity):
    #     total = 0
    #     cart_quantity = quantity
    #     multibuy_promos = MULTIBUY_DISCOUNTS[item]
    #     while cart_quantity:
    #         for promo in multibuy_promos:
    #             promo_quantity, promo_price = promo[0], promo[1]
    #             if cart_quantity >= promo_quantity:
    #                 used_promo = cart_quantity // promo_quantity
    #                 remainder = cart_quantity % promo_quantity
    #                 total += promo_price * used_promo
    #                 cart_quantity = remainder
    #         if cart_quantity:
    #             total += cart_quantity * FULL_PRICES[item]
    #             cart_quantity = 0
    #     return total

    def _calculate_multibuy(self, cart_quantity, req_quantity, disc_amount, total_discount):
        if cart_quantity >= req_quantity:
            used_times = cart_quantity // req_quantity
            cart_quantity = cart_quantity % req_quantity
            total_discount += disc_amount * used_times
        return cart_quantity, total_discount

    def _apply_multibuy(self, item, cart_quantity):
        total_discount = 0
        while cart_quantity:
            for req_quantity, disc_amount in MULTIBUY_DISCOUNTS[item]:
                if cart_quantity >= req_quantity:
                    cart_quantity, total_discount = self._calculate_multibuy(cart_quantity, req_quantity, disc_amount, total_discount)
            if cart_quantity:
                # total_discount += cart_quantity * FULL_PRICES[item]
                cart_quantity = 0
        return total_discount
    

def checkout(skus: str) -> int:
    cart = Cart(skus)
    total = cart.calculate_cart_total()
    # cart.apply_promotion()

    return total




