import unittest
from solution import Solution

class TestLetterCombinations(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        digits = "23"
        expected = sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
        result = sorted(self.sol.letterCombinations(digits))
        self.assertEqual(result, expected)

    def test_empty_input(self):
        digits = ""
        expected = []
        result = self.sol.letterCombinations(digits)
        self.assertEqual(result, expected)

    def test_single_digit(self):
        digits = "2"
        expected = ["a", "b", "c"]
        result = sorted(self.sol.letterCombinations(digits))
        self.assertEqual(result, expected)

    def test_digit_with_4_letters(self):
        digits = "7"
        expected = ["p", "q", "r", "s"]
        result = sorted(self.sol.letterCombinations(digits))
        self.assertEqual(result, expected)

    def test_long_input(self):
        digits = "234"
        result = self.sol.letterCombinations(digits)
        self.assertEqual(len(result), 27)

if __name__ == "__main__":
    unittest.main()
