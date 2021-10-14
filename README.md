# LuhnCheck
Standard Luhn Check algorithm as Python

ref https://en.wikipedia.org/wiki/Luhn_algorithm

## Testing

```shell
# run Doctests
python3 luhncheck.py -v

# run UnitTests
python3 test/luhncheck_test.py
```

## Usage
```python

from luhncheck import LuhnCheck
card_string_to_check = "1234567890123"
is_valid = LuhnCheck().valid(card_string)

```
