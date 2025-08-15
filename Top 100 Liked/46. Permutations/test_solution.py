import unittest
from solution import Solution

class TestPermute(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        nums = [1, 2, 3]
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
        result = self.sol.permute(nums)
        self.assertEqual(expected, result)

    def test2(self):
        nums = [0,1]
        expected = [[0,1],[1,0]]
        result = self.sol.permute(nums)
        self.assertEqual(expected, result)

    def test3(self):
        nums = [1]
        expected = [[1]]
        result = self.sol.permute(nums)
        self.assertEqual(expected, result)
