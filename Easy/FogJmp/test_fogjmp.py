from solution import solution
import unittest


class TestCyclicRotation(unittest.TestCase):

    def test_1(self):
        X = 10
        Y = 85
        D = 30
        self.assertEqual(solution(X, Y, D), 3)

    def test_2(self):
        X = 15
        Y = 60
        D = 5
        self.assertEqual(solution(X, Y, D), 9)

    def test_3(self):
        X = 2
        Y = 60
        D = 3
        self.assertEqual(solution(X, Y, D), 20)

    def test_4(self):
        X = 20
        Y = 60
        D = 8
        self.assertEqual(solution(X, Y, D), 5)

    def test_5(self):
        X = 19
        Y = 50
        D = 5
        self.assertEqual(solution(X, Y, D), 7)


if __name__ == "__main__":
    unittest.main()
