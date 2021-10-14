import unittest

from luhncheck import LuhnCheck


class LuhnTest(unittest.TestCase):

    def test_known_card_is_valid(self):
        card_string = "4242424242424242"
        self.assertIs(LuhnCheck().valid(card_string), True)
        print(f"{card_string} is valid")

    def test_known_card_is_not_valid(self):
        card_string = "1111111111111111"
        self.assertIs(LuhnCheck().valid(card_string), False)
        print(f"{card_string} is not valid")

if __name__ == "__main__":
    unittest.main()
