from solution import solution
import unittest


class TestCyclicRotation(unittest.TestCase):

    def test_1(bself):
        A = [3, 8, 9, 7, 6]
        K = 3
        self.assertEqual(solution(A, K), [9, 7, 6, 3, 8])

    def test_2(self):
        A = [0, 0, 0]
        K = 1
        self.assertEqual(solution(A, K), [0, 0, 0])

    def test_3(self):
        A = [1, 2, 3, 4]
        K = 4
        self.assertEqual(solution(A, K), [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
