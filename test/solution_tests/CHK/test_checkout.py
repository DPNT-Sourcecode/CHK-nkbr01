from solutions.CHK import checkout_solution


class TestCheckout():
    def test_single_item_returns_single_price(self):
        assert checkout_solution.checkout("A") == 50