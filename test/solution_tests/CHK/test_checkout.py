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
        assert checkout_solution.checkout("AAAAAAAAA") == 380

    def test_discount_applied_multiple_item(self):
        assert checkout_solution.checkout("AAABBBBBCC") == 290

    def test_discount_applied_multiple_item_1(self):
        assert checkout_solution.checkout("EE") == 80

    def test_discount_applied_multiple_item_2(self):
        assert checkout_solution.checkout("EEB") == 80

    def test_discount_applied_multiple_item_3(self):
        assert checkout_solution.checkout("EEEB") == 120

    def test_discount_applied_multiple_item_4(self):
        assert checkout_solution.checkout("EEEEBB") == 160

    def test_discount_applied_multiple_item_5(self):
        assert checkout_solution.checkout("BEBEEE") == 160

    def test_discount_applied_multiple_item_6(self):
        assert checkout_solution.checkout("B") == 30

    def test_discount_applied_multiple_item_7(self):
        assert checkout_solution.checkout("BB") == 45

    def test_discount_applied_multiple_item_8(self):
        assert checkout_solution.checkout("BBB") == 75

    def test_discount_applied_multiple_item_9(self):
        assert checkout_solution.checkout("BBBB") == 90

    def test_discount_applied_multiple_item_10(self):
        assert checkout_solution.checkout("ABCDEABCDE") == 280

    def test_discount_applied_multiple_item_11(self):
        assert checkout_solution.checkout("CCADDEEBBA") == 280

    def test_discount_applied_multiple_item_12(self):
        assert checkout_solution.checkout("AAAAAEEBAAABB") == 455

    def test_discount_applied_multiple_item_13(self):
        assert checkout_solution.checkout("ABCDECBAABCABBAAAEEAA") == 665

    # def test_discount_applied_multiple_item_14(self):
    #     assert checkout_solution.checkout("FFF") == 20

    # def test_discount_applied_multiple_item_15(self):
    #     assert checkout_solution.checkout("FF") == 20
