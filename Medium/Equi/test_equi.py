from solution import Equi
import unittest


class TestTabularArray(unittest.TestCase):

    def test_calculate(self):
        A = [-1, 3, -4, 5, 1, -6, 2, 1]
        example = Equi(A)
        index = 1 # index = 1 ; right = -4+5+1-6+2+1 = 7 ; left = -1
        self.assertEqual(example.calculate(1,"right"),-1)
        self.assertEqual(example.calculate(1,"left"),-1)
        index = 2 # index = 2 ; right = 3 ; left = 3
        self.assertEqual(example.calculate(2,"right"),3)
        self.assertEqual(example.calculate(2,"left"),2)
        index = 3 # index = 3 ; right = 3 ; left = 3
        self.assertEqual(example.calculate(3,"right"),-2)
        self.assertEqual(example.calculate(3,"left"),-2)
        index = 4 # index = 4 ; right = 3 ; left = 3
        self.assertEqual(example.calculate(4,"right"),-3)
        self.assertEqual(example.calculate(4,"left"),3)

if __name__ == "__main__":
    unittest.main()
