import unittest
from solution import Solution

class TestLetterCombinations(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        n = 3
        expected = sorted(["((()))","(()())","(())()","()(())","()()()"])
        result = sorted(self.sol.generateParenthesis(n))
        self.assertEqual(result, expected)

    def test_example2(self):
        n = 1
        expected = ['()']
        result = self.sol.generateParenthesis(n)
        self.assertEqual(result, expected)
