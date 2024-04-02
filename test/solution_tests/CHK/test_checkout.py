from solutions.CHK import checkout_solution
import pytest

class TestCheckout():

    @pytest.mark.parametrize(
            "skus, total",
            [
                ("A", 50), 
                ("B", 30), 
                ("C", 20), 
                ("D", 15), 
                ("E", 40), 
                ("F", 10),
                ("G", 20), 
                ("H", 10),
                ("I", 35),
                ("J", 60),
                ("K", 70),
                ("L", 90),
                ("M", 15),
                ("N", 40),
                ("O", 10),
                ("P", 50),
                ("Q", 30),
                ("R", 50),
                ("S", 20),
                ("T", 20),
                ("U", 40),
                ("V", 50),
                ("W", 20),
                ("X", 17),
                ("Y", 20), 
                ("Z", 21),  
            ],
    )
    def test_single_item(self, skus, total):
        assert checkout_solution.checkout(skus) == total

    @pytest.mark.parametrize(
            "skus, total",
            [
                ("@", -1),
                ("~", -1),
                ("A!", -1),
            ],
    )
    def test_illegal_input(self, skus, total):
        assert checkout_solution.checkout(skus) == total

    @pytest.mark.parametrize(
            "skus, total",
            [
                ("A" * 2, 100),
                ("A" * 3, 130),
                ("A" * 4, 180),
                ("A" * 5, 200),
                ("A" * 6, 250),
                ("A" * 7, 300),
                ("A" * 8, 330),
                ("A" * 9, 380),
                ("AB") == 80,
                ("BB") == 45,
                ("BBB") == 75,
                ("BBBB") == 90
                ("AAABBBBBCC") == 290,
            ],
    )
    def test_multiple_item_base_skus(self, skus, total):
        assert checkout_solution.checkout(skus) == total




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


