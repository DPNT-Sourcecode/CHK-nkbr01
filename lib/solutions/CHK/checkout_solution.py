from collections import Counter


# noinspection PyUnusedLocal
# skus = unicode string

FULL_PRICES = {
    "A": 50, 
    "B": 30, 
    "C": 20, 
    "D": 15, 
    "E": 40, 
    "F": 10,
    "G": 20, 
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 70,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 20,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 17,
    "Y": 20, 
    "Z": 21,  
}

MULTIBUYS = {
    "A": [
        (3, 130),
        (5, 200), #required_amount, multibuy_price
    ],
    "B": [
        (2, 45)
    ],
    "H": [
        (5, 45),
        (10, 80),
    ],
    "K": [
        (2, 150),
    ],
    "P": [
        (5, 200),
    ],
    "Q": [
        (3, 80),
    ],
    "V": [
        (2, 90),
        (3, 130),
    ],
}

PROMOS = {
    "E": (2, "B"), 
    "F": (2, "F"),
    "N": (3, "M"),
    "R": (3, "Q"),
    "U": (3, "U"),
}

GROUP_DISCOUNT = {
    ("S","T","X","Y","Z") : [
        (3, 45)
    ],
}

class Cart:

    def __init__(self, s: str):
        self.total = 0
        self.cart = Counter(s)

    def calculate_cart_total(self):
        try:
            for product, quantity in self.cart.items():
                self.total += self._apply_full_price(product, quantity)
                if product in MULTIBUYS:
                    self.total -= self._apply_multibuy(product, quantity)
            self.total -= self._apply_promotion()
            self.total -= self._apply_group_discount()
            return self.total
        except KeyError:
            return -1
    
    def _apply_full_price(self, product, quantity):
        product_price = FULL_PRICES[product]
        total = quantity * product_price
        return total
    
    def _calculate_final_price(self, product, quantity):
        if product in MULTIBUYS:
            return self._apply_full_price(product, quantity) - self._apply_multibuy(product, quantity)
        else:
            return self._apply_full_price(product, quantity)
    
    def _calculate_multibuy(self, cart_quantity, req_quantity, disc_amount, total_discount):
        used_times = cart_quantity // req_quantity
        cart_quantity = cart_quantity % req_quantity
        total_discount += disc_amount * used_times
        return cart_quantity, total_discount

    def _apply_multibuy(self, product, cart_quantity):
        total_discount = 0
        while cart_quantity:
            multibuy_prices = sorted(MULTIBUYS[product], reverse=True)
            for req_quantity, multibuy_price in multibuy_prices:
                if cart_quantity >= req_quantity:
                    multibuy_discount = req_quantity * FULL_PRICES[product] - multibuy_price
                    cart_quantity, total_discount = self._calculate_multibuy(cart_quantity, req_quantity, multibuy_discount, total_discount)
            if cart_quantity:
                cart_quantity = 0
        return total_discount

    def _apply_promotion(self):
        total_discount = 0
        for product, promotion in PROMOS.items():
            req_quantity, promo_product = promotion
            if product == promo_product:
                req_quantity += 1
                cart_quantity = self.cart[product]
                disc_amount = FULL_PRICES[product]
                cart_quantity, discount = self._calculate_multibuy(cart_quantity, req_quantity, disc_amount, 0)
                total_discount += discount
            else:
                if product in self.cart and promo_product in self.cart:
                    used_times = self.cart[product] // req_quantity
                    cart_quantity = self.cart[promo_product]
                    updated_quantity = cart_quantity - used_times
                    previous_price = self._calculate_final_price(promo_product, cart_quantity)
                    updated_price = self._calculate_final_price(promo_product, updated_quantity)
                    discount = previous_price - updated_price
                    total_discount += discount
        return total_discount
    
    def _apply_group_discount(self):
        return 0

def checkout(skus: str) -> int:
    cart = Cart(skus)
    total = cart.calculate_cart_total()
    return total
