import unittest
from HTTP_request import GetValue

class Tests(unittest.TestCase):
    """Class for test methods"""
    def test_get_data(self):
        """Function for test methods get_data"""
        self.assertEqual(GetValue('/usd-rub?value=1').resp_dat(), {'start_currency': 'usd', 'final_currency': 'rub', 'start_value': 1, 'final_value': 75.8375, })