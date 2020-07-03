from binary_gap import solution

import unittest

class TestStringMethods(unittest.TestCase):

    def test_solution_5(self,):
        N = 5
        assert solution(N) == 1

    def test_solution_51712(self):
        N = 51712
        assert solution(N) == 2

    def test_solution_561892(self):
        N = 561892
        assert solution(N) == 3

    def test_solution_66561(self):
        N = 66561
        assert solution(N) == 9

    def test_solution_6291457(self):
        N = 6291457
        assert solution(N) == 20

    def test_solution_74901729(self):
        N = 74901729
        assert solution(N) == 4

    def test_solution_1376796946(self):
        N = 1376796946
        assert solution(N) == 5

    def test_solution_1610612737(self):
        N = 1610612737
        assert solution(N) == 28

if __name__ == '__main__':
    unittest.main()
