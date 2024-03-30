from solutions.CHK import checkout_solution


class TestCheckout():
    def test_single_item_returns_single_price(self):
        assert checkout_solution.checkout("A") == 50

    def test_multiple_items_returns_total_price(self):
        assert checkout_solution.checkout("AB") == 80

    def test_convert_string_to_cart_returns_cart(self):
        cart = checkout_solution.Cart("ABBCCC")
        assert cart.cart == {"A":1, "B":2, "C":3}

    def test_illegal_item_returns_minus_one(self):
        assert checkout_solution.checkout("ABX") == -1

    def test_discount_applied_single_item(self):
        assert checkout_solution.checkout("AAA") == 130

    def test_discount_applied_two_A(self):
        assert checkout_solution.checkout("AA") == 100

    def test_discount_applied_four_A(self):
        assert checkout_solution.checkout("AAAA") == 180

    def test_discount_applied_five_A(self):
        assert checkout_solution.checkout("AAAAA") == 200

    def test_discount_applied_six_A(self):
        assert checkout_solution.checkout("AAAAAA") == 250

    def test_discount_applied_seven_A(self):
        assert checkout_solution.checkout("AAAAAAA") == 300

    def test_discount_applied_eight_A(self):
        assert checkout_solution.checkout("AAAAAAAA") == 330

    def test_discount_applied_nine_A(self):
        assert checkout_solution.checkout("AAAAAAAA") == 380

    def test_discount_applied_multiple_item(self):
        assert checkout_solution.checkout("AAABBBBBCC") == 290

    def test_free_B_with_two_E(self):
        cart = checkout_solution.Cart("EEB")
        # cart.apply_promotion()
        assert cart.calculate_cart_total() == 110
        assert cart.cart == {"B": 2, "E": 2}

    def test_free_B_with_two_E_1(self):
        cart = checkout_solution.Cart("EE")
        # cart.apply_promotion()
        assert cart.calculate_cart_total() == 80
        assert cart.cart == {"B": 1, "E": 2}

    def test_free_B_with_two_E_total(self):
        assert checkout_solution.checkout("AEEEBB") == 215
    
    def test_free_B_with_two_E_cart(self):
        cart = checkout_solution.Cart("AEEEBB")
        cart.calculate_cart_total()
        # cart.apply_promotion()
        assert cart.cart == {"A": 1, "B": 3, "E": 3}
