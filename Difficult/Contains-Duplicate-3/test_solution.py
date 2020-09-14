import unittest
from solution  import Solution
class TestContains(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        pass

    def test_case_1(self):
        s = "abab"
        self.assertEqual(self.solution.repeated_strings(s=s), True)
   
    def test_case_2(self):
        s = "abcabcabcabc"
        self.assertEqual(self.solution.repeated_strings(s=s), True)

    def test_case_3(self):
        s = "aba"
        self.assertEqual(self.solution.repeated_strings(s=s), False)

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite)
# unittest.main()