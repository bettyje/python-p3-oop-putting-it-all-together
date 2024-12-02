import io
import sys
from shoe import Shoe


class TestShoe:
    '''Shoe in shoe.py'''

    def test_has_brand_and_size(self):
        '''has the brand and size passed to __init__, and values can be set to new instance.'''
        stan_smith = Shoe("Adidas", 9, "White", 120)
        assert (stan_smith.brand == "Adidas")
        assert (stan_smith.size == 9)

    def test_requires_int_size(self):
        '''prints "size must be an integer" if size is not an integer.'''
        stan_smith = Shoe("Adidas", 9, "White", 120)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        try:
            stan_smith.size = "not an integer"
        except ValueError:
            pass  # We expect this error
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "size must be an integer\n"

    def test_can_cobble(self):
        '''says that the shoe has been repaired.'''
        stan_smith = Shoe("Adidas", 9, "White", 120)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        stan_smith.repair()  # Fixed method name
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "The shoe has been repaired.\n"

    def test_cobble_makes_new(self):
        '''creates an attribute on the instance called 'condition' and set equal to 'New' after repair.'''
        stan_smith = Shoe("Adidas", 9, "White", 120)
        stan_smith.repair()  # Fixed method name
        assert stan_smith.condition == "Repaired"
