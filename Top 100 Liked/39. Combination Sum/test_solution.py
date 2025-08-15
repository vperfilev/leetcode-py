import unittest
from solution import Solution

class TestCombinationSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        candidates = [2, 3, 6, 7]
        target = 7
        expected = [[2,2,3],[7]]
        result = self.sol.combinationSum(candidates, target)
        self.assertEqual(result, expected)

    def test2(self):
        candidates = [2,3,5]
        target = 8
        expected = [[2,2,2,2],[2,3,3],[3,5]]
        result = self.sol.combinationSum(candidates, target)
        self.assertEqual(result, expected)

    def test3(self):
        candidates = [2]
        target = 1
        expected = []
        result = self.sol.combinationSum(candidates, target)
        self.assertEqual(result, expected)
