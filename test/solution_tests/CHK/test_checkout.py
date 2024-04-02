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
        assert checkout_solution.checkout("AB~") == -1

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

    def test_discount_applied_multiple_item_14(self):
        assert checkout_solution.checkout("FFF") == 20

    def test_discount_applied_multiple_item_15(self):
        assert checkout_solution.checkout("FF") == 20

    def test_discount_applied_multiple_item_16(self):
        assert checkout_solution.checkout("FFFF") == 30

    def test_discount_applied_multiple_item_17(self):
        assert checkout_solution.checkout("FFFFF") == 40

    def test_discount_applied_multiple_item_18(self):
        assert checkout_solution.checkout("FFFFFF") == 40

    def test_discount_applied_multiple_item_19(self):
        assert checkout_solution.checkout("NNNM") == 120

    def test_discount_applied_multiple_item_20(self):
        assert checkout_solution.checkout("RRRQ") == 150

    def test_discount_applied_multiple_item_21(self):
        assert checkout_solution.checkout("UUUU") == 120

    def test_discount_applied_multiple_item_22(self):
        assert checkout_solution.checkout("HHHHH") == 45

    def test_discount_applied_multiple_item_23(self):
        assert checkout_solution.checkout("HHHHHHHHHH") == 80

    def test_discount_applied_multiple_item_24(self):
        assert checkout_solution.checkout("PPPPP") == 200

    def test_discount_applied_multiple_item_25(self):
        assert checkout_solution.checkout("QQQ") == 80

    def test_discount_applied_multiple_item_26(self):
        assert checkout_solution.checkout("VV") == 90

    def test_discount_applied_multiple_item_27(self):
        assert checkout_solution.checkout("VVV") == 130

    def test_discount_applied_multiple_item_28(self):
        assert checkout_solution.checkout("NNN") == 120

    def test_discount_applied_multiple_item_29(self):
        assert checkout_solution.checkout("G") == 20

    def test_discount_applied_multiple_item_30(self):
        assert checkout_solution.checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 837

    def test_discount_applied_multiple_item_31(self):
        assert checkout_solution.checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ") == 1602

    def test_discount_applied_multiple_item_32(self):
        assert checkout_solution.checkout("STX") == 45

    def test_discount_applied_multiple_item_33(self):
        assert checkout_solution.checkout("SSS") == 45

    def test_discount_applied_multiple_item_34(self):
        assert checkout_solution.checkout("STXYZS") == 90

    def test_discount_applied_multiple_item_35(self):
        assert checkout_solution.checkout("XYZAB") == 125

    def test_discount_applied_multiple_item_36(self):
        #choose the most expensive for the group discount
        assert checkout_solution.checkout("STXYZ") == 82

    def test_discount_applied_multiple_item_37(self):
        assert checkout_solution.checkout("SSZYZ") == 85