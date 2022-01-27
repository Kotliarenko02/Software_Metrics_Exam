
"""Program with gamma function"""
import unittest
import math

POS = "Positive gamma"
NEG = "Negative gamma"
INV = "Not valid input"

def results(x):
    print("Input: ",x)
    result = ""
    if (isinstance(x) == int or isinstance(x) == float):
        num = math.gamma(float(x))
        if num> 0:
            result = POS
        else:
            result = NEG
    else:
        result = INV
    print(result,"\n")
    return result


class TestDevisionResults(unittest.TestCase):
    """input testing"""
    def test_positive_gamma(self):
        """for positive"""
        self.assertEqual(results(8), POS)

    def test_invalid(self):
        """for invalid input"""
        self.assertEqual(results("d"), INV)

    def test_negative_gamma(self):
        """for negative"""
        self.assertEqual(results(-0.1), NEG)


if __name__ == '__main__':
    unittest.main()
