
class LuhnCheck:
    """Class to run a standard Luhn check on a credit card number"""


    def __init__(self) -> None:
        """ initializer for the class """

    def valid(self, card: str) -> bool:
        """Given card number as a string, return a bool if that card is valid or not

        Parameters
        ----------
        card : string
            the card number to be validated

        Returns
        -------
        bool
            True or False


        :param card: str
        :return: bool

        >>> LuhnCheck().valid("4242424242424242")
        True

        >>> LuhnCheck().valid("1111111111111111")
        False

        """

        self.card_string = card
        self.card = list(card)
        self.check_digit = self.card.pop()
        self.card.reverse()

        processed_digits = []

        for index, digit in enumerate(self.card):
            if index % 2 == 0:
                doubled_digit = int(digit) * 2

                if doubled_digit > 9:
                    doubled_digit -= 9

                processed_digits.append(doubled_digit)
            else:
                processed_digits.append(int(digit))

        total = int(self.check_digit) + sum(processed_digits)

        if total % 10 == 0:
            #print(f"{self.card_string} is valid")
            return True
        else:
            #print(f"{self.card_string} is not valid")
            return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
