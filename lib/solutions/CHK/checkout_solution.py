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
        (2, 60 - 45)
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
            for product, quantity in self.cart.items():
                self.total += self._apply_full_price(product, quantity)
                if product in MULTIBUY_DISCOUNTS:
                    self.total -= self._apply_multibuy(product, quantity)
                    # self.total += multibuy_total
                # else:
                #     full_total = self.apply_full_price(product, quantity)
                #     self.total += full_total
            self.total -= self._apply_promotion()
            return self.total
        except KeyError:
            return -1
    
    def _apply_full_price(self, product, quantity):
        product_price = FULL_PRICES[product]
        total = quantity * product_price
        return total

    def _apply_promotion(self):
        total_discount = 0
        for product, promotion in PROMOS.items():
            req_quantity, promo_product = promotion
            if product == promo_product:
                pass
            else:
                if product in self.cart and promo_product in self.cart:
                    used_times = self.cart[product] // req_quantity
                    cart_quantity = self.cart[promo_product]
                    updated_quantity = cart_quantity - used_times
                    previous_price = self._apply_full_price(promo_product, cart_quantity) - self._apply_multibuy(promo_product, cart_quantity)
                    updated_price = self._apply_full_price(promo_product, updated_quantity) - self._apply_multibuy(promo_product, updated_quantity)
                    discount = previous_price - updated_price
                    # if promo_product in MULTIBUY_DISCOUNTS:
                    #     previous_price = self._apply_multibuy(promo_product, cart_quantity)
                    #     updated_price = self._apply_multibuy(promo_product, updated_quantity)
                    # else:
                    #     previous_price = self.apply_full_price(promo_product, cart_quantity)
                    #     updated_price = self.apply_full_price(promo_product, updated_quantity)
                    # discount = previous_price - updated_price
                    total_discount += discount
        return total_discount

    def _calculate_multibuy(self, cart_quantity, req_quantity, disc_amount, total_discount):
        # if cart_quantity >= req_quantity:
        used_times = cart_quantity // req_quantity
        cart_quantity = cart_quantity % req_quantity
        total_discount += disc_amount * used_times
        return cart_quantity, total_discount

    def _apply_multibuy(self, product, cart_quantity):
        total_discount = 0
        while cart_quantity:
            for req_quantity, disc_amount in MULTIBUY_DISCOUNTS[product]:
                if cart_quantity >= req_quantity:
                    cart_quantity, total_discount = self._calculate_multibuy(cart_quantity, req_quantity, disc_amount, total_discount)
            if cart_quantity:
                cart_quantity = 0
        return total_discount
    

def checkout(skus: str) -> int:
    cart = Cart(skus)
    total = cart.calculate_cart_total()
    # cart.apply_promotion()

    return total
