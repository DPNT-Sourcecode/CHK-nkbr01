from solutions.CHK import checkout_solution


class TestCheckout():
    def test_single_item_returns_single_price(self):
        assert checkout_solution.checkout("A") == 50

    def test_multiple_items_returns_total_price(self):
        assert checkout_solution.checkout("AB") == 80

    def test_convert_string_to_cart_returns_cart(self):
        assert checkout_solution.convert_string_to_cart("ABBCCC") == {"A":1, "B":2, "C":3}

    def test_illegal_item_returns_minus_one(self):
        assert checkout_solution.checkout("ABX") == -1

    def test_discount_applied_single_item(self):
        assert checkout_solution.checkout("AAA") == 130

    def test_discount_applied_two_A(self):
        assert checkout_solution.checkout("AA") == 100

    def test_discount_applied_four_A(self):
        assert checkout_solution.checkout("AAAA") == 180

    def test_discount_applied_multiple_item(self):
        assert checkout_solution.checkout("AAABBBBBCC") == 290

    def test_free_B_with_two_E(self):
        assert checkout_solution.checkout("AEE") == 130
        assert checkout_solution.checkout.cart("AEE") == {"A": 1, "B": 1, "E": 2}
