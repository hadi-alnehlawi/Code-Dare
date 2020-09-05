from solution import Solution
import unittest


class TestLargestTime(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test1_largest(self):
        A = [2, 9, 5, 0]
        self.assertEqual(self.solution.largestTimeFromDigits(A), [2, 0, 5, 9])

    def test2_largest(self):
        A = [0, 0, 1, 0]
        self.assertEqual(self.solution.largestTimeFromDigits(A), [1, 0, 0, 0])

    def test3_largest(self):
        A = [7, 0, 1, 2]
        self.assertEqual(self.solution.largestTimeFromDigits(A), [2, 1, 0, 7])

    def test4_largest(self):
        A = [8, 2, 5, 2]
        self.assertEqual(self.solution.largestTimeFromDigits(A), [2, 2, 5, 8])

    def test5_largest(self):
        A = [6, 6, 0, 2]
        self.assertEqual(self.solution.largestTimeFromDigits(A), "")

    def test6_largest(self):
        A = [6, 1, 0, 2]
        self.assertEqual(self.solution.largestTimeFromDigits(A), [2, 1, 0, 6])


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite)
