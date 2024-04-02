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
                ("B" * 2, 45),
                ("B" * 3, 75),
                ("B" * 4, 90),
                ("AB", 80),
                ("AAABBBBBCC", 290),
            ],
    )
    def test_multiple_item_base_skus(self, skus, total):
        assert checkout_solution.checkout(skus) == total

    @pytest.mark.parametrize(
            "skus, total",
            [
                ("EE", 80),
                ("EEB", 80),
                ("EEEB", 120),
                ("EEEEBB", 160),
                ("BEBEEE", 160),
                ("ABCDEABCDE", 280),
                ("CCADDEEBBA", 280),
                ("AAAAAEEBAAABB", 455),
                ("ABCDECBAABCABBAAAEEAA", 665),
                ("F" * 2, 20),
                ("F" * 3, 20),
                ("F" * 4, 30),
                ("F" * 5, 40),
                ("F" * 6, 40),
            ],
    )
    def test_multiple_item_promo(self, skus, total):
        assert checkout_solution.checkout(skus) == total

    @pytest.mark.parametrize(
            "skus, total",
            [
                ("NNNM", 120),
                ("RRRQ", 150),
                ("UUUU", 120),
                ("HHHHH", 45),
                ("HHHHHHHHHH", 80),
                ("PPPPP", 200),
                ("QQQ", 80),
                ("VV", 90),
                ("VVV", 130),
                ("NNN", 120),
                ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 837),
                ("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ", 1602),
            ],
    )
    def test_multiple_item_new_promo_and_multibuy(self, skus, total):
        assert checkout_solution.checkout(skus) == total

    @pytest.mark.parametrize(
            "skus, total",
            [
                ("STX", 45),
                ("SSS", 45),
                ("STXYZS", 90),
                ("XYZAB", 125),
                ("STXYZ", 82),
                ("SSZYZ", 85)
            ],
    )
    def test_multiple_item_groupbuy(self, skus, total):
        assert checkout_solution.checkout(skus) == total