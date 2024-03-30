from solutions.CHK import checkout_solution


class TestCheckout():
    def test_single_item_returns_single_price(self):
        assert checkout_solution.checkout("A") == 50

    def test_multiple_items_returns_total_price(self):
        assert checkout_solution.checkout("AB") == 80

    def test_convert_string_to_cart_returns_cart(self):
        assert checkout_solution.convert_string_to_cart("A2B45C") == {"A":1, "B":2, "C":45}

    def test_illegal_item_returns_minus_one(self):
        assert checkout_solution.checkout("ABX") == -1

    def test_discount_applied(self):
        assert checkout_solution.checkout("3A") == 130



